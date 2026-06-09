#!/usr/bin/env python3
"""Search the bundled Serenity corpus for ticker/theme evidence."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "references" / "corpus"
TEXT_EXTS = {".md", ".txt", ".csv", ".json"}


def iter_files() -> list[Path]:
    return sorted(
        p
        for p in CORPUS.rglob("*")
        if p.is_file() and p.suffix.lower() in TEXT_EXTS and p.name != ".DS_Store"
    )


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:  # pragma: no cover - defensive CLI path
        return f"[unreadable: {exc}]"


def extract_title(text: str, path: Path) -> str:
    for line in text.splitlines()[:30]:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
        if line.lower().startswith("title:"):
            return line.split(":", 1)[1].strip()
    return path.stem


def extract_date(text: str) -> str:
    patterns = [
        r"Date UTC:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})",
        r"日期[:：]\s*([0-9]{4}-[0-9]{2}-[0-9]{2})",
        r"([0-9]{4}-[0-9]{2}-[0-9]{2})",
    ]
    head = "\n".join(text.splitlines()[:80])
    for pattern in patterns:
        match = re.search(pattern, head)
        if match:
            return match.group(1)
    return ""


def extract_symbols(text: str, path: Path) -> list[str]:
    head = "\n".join(text.splitlines()[:120])
    symbols: set[str] = set()
    explicit = re.search(r"Symbols:\s*([A-Z0-9, $]+)", head)
    if explicit:
        for part in re.split(r"[, $]+", explicit.group(1)):
            if 1 <= len(part) <= 6:
                symbols.add(part)
    for token in re.findall(r"\$([A-Z][A-Z0-9]{0,5})\b", text):
        symbols.add(token)
    for token in re.findall(r"\b[A-Z]{2,5}\b", path.name):
        symbols.add(token)
    return sorted(symbols)


def term_pattern(term: str) -> re.Pattern[str] | None:
    if re.fullmatch(r"[A-Za-z0-9]{1,6}", term):
        return re.compile(rf"(?<![A-Za-z0-9])\$?{re.escape(term)}(?![A-Za-z0-9])", re.I)
    return None


def make_snippet(text: str, terms: list[str], width: int = 180) -> str:
    positions = []
    lower = text.lower()
    for term in terms:
        pattern = term_pattern(term)
        if pattern:
            match = pattern.search(text)
            if match:
                positions.append(match.start())
        else:
            pos = lower.find(term.lower())
            if pos >= 0:
                positions.append(pos)
    pos = min(positions) if positions else 0
    start = max(0, pos - width // 2)
    end = min(len(text), pos + width // 2)
    snippet = re.sub(r"\s+", " ", text[start:end]).strip()
    return snippet


def score_text(text: str, path: Path, terms: list[str]) -> int:
    haystack = f"{path.name}\n{text}".lower()
    original = f"{path.name}\n{text}"
    score = 0
    for term in terms:
        pattern = term_pattern(term)
        if pattern:
            count = len(pattern.findall(original))
        else:
            t = term.lower()
            count = haystack.count(t)
        score += count * max(1, len(term))
        name_text = path.name
        if pattern:
            if pattern.search(name_text):
                score += 50
        elif term.lower() in name_text.lower():
            score += 50
    if score > 0 and ("raw" in path.parts or path.suffix.lower() in {".json", ".csv"}):
        score = max(1, int(score * 0.5))
    if score > 0 and "posts" in path.parts:
        score += 30
    return score


def search(query: str, top_k: int) -> list[dict[str, object]]:
    terms = [t for t in re.split(r"[\s,;/]+", query.strip()) if t]
    if not terms:
        return []
    results = []
    for path in iter_files():
        text = read_text(path)
        score = score_text(text, path, terms)
        if score <= 0:
            continue
        results.append(
            {
                "score": score,
                "path": str(path.relative_to(ROOT)),
                "title": extract_title(text, path),
                "date": extract_date(text),
                "symbols": extract_symbols(text, path),
                "snippet": make_snippet(text, terms),
            }
        )
    results.sort(key=lambda row: (-int(row["score"]), str(row["path"])))
    return results[:top_k]


def main() -> None:
    parser = argparse.ArgumentParser(description="Search bundled Serenity corpus.")
    parser.add_argument("--query", required=True, help="Ticker, company, theme, or keyword.")
    parser.add_argument("--top-k", type=int, default=8, help="Number of results to show.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()

    results = search(args.query, args.top_k)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    print(f"# Serenity corpus search: {args.query}\n")
    if not results:
        print("No direct matches. Try related sector/component/customer keywords.")
        return
    for i, row in enumerate(results, 1):
        symbols = ", ".join(row["symbols"]) if row["symbols"] else "-"
        print(f"## {i}. {row['title']}")
        print(f"- Path: `{row['path']}`")
        print(f"- Date: {row['date'] or '-'}")
        print(f"- Symbols: {symbols}")
        print(f"- Score: {row['score']}")
        print(f"- Snippet: {row['snippet']}\n")


if __name__ == "__main__":
    main()

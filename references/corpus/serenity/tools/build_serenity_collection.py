#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import textwrap
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path("/Users/wushaojian/Downloads/serenity")
RAW = ROOT / "raw"
POSTS = ROOT / "posts"
PULLPUSH_URL = (
    "https://api.pullpush.io/reddit/search/submission/"
    "?author=AleaBito&size=100&sort=desc"
)


MANUAL_RECENT = [
    {
        "id": "1pyghud",
        "created_utc": 1766995211,
        "subreddit": "wallstreetbets",
        "title": "The Entire AI Buildout (Google, NVDA, MSFT) Is dependent on this $700m Monopoly - $15 -> $150 PT.",
        "permalink": "/r/wallstreetbets/comments/1pyghud/the_entire_ai_buildout_google_nvda_msft_is/",
        "source": "reddit_profile_json_manual",
        "selftext": """I drew colossus from Starcraft 2 to represent laser beams. And prepared a whole thesis but kept getting automodded for "low quality". So here's the more TLDR version of my thesis:

The Entire AI Industry is shifting to photonics from Google TPU to optical interconnects.

The entire AI "Growth" story ends in 2026 if there's no InP substrates + materials.

BUT GUESS WHO CONTROLS IT ALL? One Company: $AXTI.

There's two bottlenecks:

InP Substrates -

- Hyperscaler optics (TPU pods, etc)
- Optical transceivers (5g, data)
- LiDAR (robotaxis, drones, military)
- Optical Modules (interconnect clusters)
- Silicon photonics laser dies (Nvidia's future co-packaged optics and Intel/Broadcom SiPh engines use InP CW laser arrays.)

This is a DUOPOLY from
- AXTI (est. ~30-35%)
- Sumitomo (est. ~30%)
- JX Nippon (est. 10-15%)

Indium Phosphide (the source material for everything):

Vital Materials - 35%
AXT - 25%

Before, this was a commodity with low TAM just for telecom.

Now they're used for the entire AI buildout.

Just to give u an example $AXTI -> $LITE -> $GOOGL TPU. without any of these members, the program shuts down.

Google would literally pay $5B (50 TIMES prices + ~$140m TAM from 2024) DIRECTLY to one of these suppliers -> hand to COHR just so their whole TPU program doesn't stall because Meta decided to buy them out. And this would only be a like a 3-4% added cost to their BOM because this thing was so cheap. If Meta does it first, then Google's TPU program stalls. If Google does it first Microsoft's ASIC problem stalls.

THE WORLD IS AT MAX CAPACITY RIGHT NOW (demand > supply by multiple factors pre-ramp) AND THIS IS GAME THEORY on materials supply chains.

Guess who shows up twice in the WHOLE AI bottleneck? Both as the duopoly bottleneck and the duopoly bottleneck of the bottleneck

AXTI.

This is the holy grail of supply chain analysis + materials research. Nobody's posted about this stock here in the past 5 years, you're welcome.

Anyway I decided to max OTM some spare change on Calls last Friday, because there's a low chance this goes from $15 to $150 if we see the same memory supply stock in 2026. I will buy more shares on Monday when markets open up but wanted to share this at the start as proof.

NFI, there's a chance China sends this to $0 with export controls so don't follow along I just wanted to share my thoughts. But if this goes to $0 so does the entire growth phase of the AI buildout.

I just thought this could also easily be a $7B company given they control 1/3rd of the world's entire substrate capacity and then 1/4th of the world's entire materials used for AI buildout.

It's a monopoly in mining -> refining -> substrate production. And a duopoly for InP substrate production and Indium Phosphide.

I just wanted to share as proof in case this becomes legendary.

TLDR: THE ENTIRE AI INDUSTRY IS BOTTLENECKED TWO TIMES BY THE SAME COMPANY.

FOUND THE SINGLE POINT OF FAILURE OF THE ENTIRE MANY TRILLION USD WESTERN AI BUILDOUT IS SOME $700m COMPANY CALLED AXTI, WORTH LESS THAN SOME PRE REVENUE LLM STARTUP.""",
    },
    {
        "id": "1ooyuav",
        "created_utc": 1762336655,
        "subreddit": "wallstreetbets",
        "title": "Meta Level 100 Charizard TA Analysis - Flamethrower Super Effective, $800+ Breakout",
        "permalink": "/r/wallstreetbets/comments/1ooyuav/meta_level_100_charizard_ta_analysis_flamethrower/",
        "source": "reddit_profile_json_manual",
        "selftext": """People have been waiting for the Charizard Pattern to appear like on Google back at $156.

Well. It's appeared again. But on Meta. Meta sounds like an evolution so it's actually META Charizard X this time instead of the regular Charizard - the Black Charizard.

If we look at the TA, the automated magnemite saw a chance to use explosion on a weak Charmander after Charmander decided to file its quarterly returns to Officer Jenny.

They thought the Charmander was low on funds and wanted to collect its taxes. But in reality Charmander is stinking rich, Celadon City casino was just holding all its funds temporarily from Charmander's day job gambling behind the casino dumpsters.

In fact, Charmander was actually rich because of 0dte on Ultra Ball derivatives. With all the proceeds after, charmander, bought all the rare candies on the market, and then leveled up to 100.

You can see this in the chart. It starts off with the tail. Then you can see the belly. And now we have a fully formed Black Charizard, the fear of every male when you talk about exs.

And because of this, Charmander Is back for revenge against the magnemites. Steel is weak against steel, so it's gonna get vaporized. Charizard will flamethrower and fly back to $800+

For that reason I bought $100k+ in Meta calls and plan to get more.""",
    },
    {
        "id": "1obuj2z",
        "created_utc": 1760996013,
        "subreddit": "wallstreetbets",
        "title": "$50k into T1 Energy - Faker DD - $7+ Breakout",
        "permalink": "/r/wallstreetbets/comments/1obuj2z/50k_into_t1_energy_faker_dd_7_breakout/",
        "source": "reddit_profile_json_manual",
        "selftext": """So I've been watching League of Legends 2025 worlds currently.

T1 did really well in the past, maybe let's ignore 2022 because of the E-girl Faker was rumored to date.

But if we jump to 2023, T1 Won Worlds then so their stock price did well reaching $15 a share because of increased skin sales.

In 2024, T1 won worlds again and their stock performance was questionable. Even though Faker had 2 new skins he was able to sell, leading to increased revenue growth, it doesn't look like people were a fan of Yone or Sylas. Mainly because there's two guys, an E-girl skin would sell very well.

It's 2025 now, T1 is in the bring of elimination. But because Faker is known to be clutch I believe T1 will win, causing the T1 energy stock-rice to breakout to $7.00 because of new skin sales.

Even if they dont win, I've also done an analysis on similar companies like TSM. TSM has reached an all time high stock price of $300 a share.

But the important thing to note is THEY ONLY did that after they got delisted from the North American League and after their AD carry doubellift retired.

So even if Faker doesn't perform or retires, T1 energy will likely do well anyway. You can see this by the plots above the graph.

Which is why I bought $50k worth of calls.

I normally do shares, but everyone told me I'm a loser, so I did calls this time.""",
    },
    {
        "id": "1o2op9m",
        "created_utc": 1760064000,
        "subreddit": "wallstreetbets",
        "title": "$200k in FLY - Reusable Rocket Chairman Kim TA - $50+ Recovery",
        "permalink": "/r/wallstreetbets/comments/1o2op9m/200k_in_fly_reusable_rocket_chairman_kim_ta_50/",
        "source": "recovered_reddit_public_html",
        "selftext": """I was looking for RKLB and SpaceX competitors, and I found Fly or Firefly Aerospace, a new rocket company building reusable Medium-Lift Rockets with Northrop Grumman and the US governments.

This piqued my interest because anything Space and Rocket go up right? Turned out not to be true.

Firefly actually went down, and over 50%, so I looked at why by drawing the TA.
Recently Japan has been doing good, and then that sea of red looked like an inverse Japan flag. The flag is typically White with a Red dot but no, this graph was Red with a White Dot. So, when you plot the inverse Nihon flag over the graph, it all made sense why it went down 50%+ since IPO.

But around this price at $30 where the flag ended. I also saw a meme of Chairman Kim on X, and then I put his photo over the edge, and the price went down probably because of him. So it all made sense.
But, from my new knowledge about Space and Rockets, even if they go down, they must go back up because they're reusable? I also learned they had the medium lift rockets in 2026 and 2026 isn't too far away and that they're going to the moon again with Nasa.

Because of this insight and because I like rockets, I realized that $FLY will head back $50+ to the moon and I bought $200k+ worth of shares.""",
    },
    {
        "id": "1nzp9nl",
        "created_utc": 1759708800,
        "subreddit": "wallstreetbets",
        "title": "$150K+ in Snap, Upward Doggy Style Ghost Bull Formation, $10+ Breakout",
        "permalink": "/r/wallstreetbets/comments/1nzp9nl/150k_in_snap_upward_doggy_style_ghost_bull/",
        "source": "recovered_reddit_public_html",
        "selftext": """This is why I'm buying Snapchat.
It all started with Aerodyne international. I watched Wulf of Wall Street and ever since then, stock has been going down.

I was thinking either it was because the stock was bad or because I wasn't Leonardo Davicni or Decaprio. Both are the same to me, but I think it's the latter.

Either way, I started using the Snapchat dancing hotdog filter, and then it dawned on me. It wasn't the person that made Decpario cool. It was his girlfriends.
So I went to ask our Miranda Kerr, she said no. Coincidentally, the stock went down even more.

Maybe it wasn't meant to be? So I Dmed Sydney Sweeney. She laughed as I bought her bath water, but at least I had a shot. So stock went up.

Then, the government shutdown happened. I wanted to ask out Nancy Pelosi, but she wasn't at work anymore. So stock price went down.
I realized, maybe it had to do with my appearance. So I used the dog filter on myself, and I suddenly became attractive. Then I went to Google to confirm, but randomly saw a Ghost Bull on the images.

Bull means stock go up. Ghost means like Snapchat. And then it also had a halloween costume, and it's October now. That means this next two months is meant to be.

I'm peak attractiveness, Ghost Bull means the stars are aligned, and the next person I ask out will say yes and the stock price will go up.
For all those reasons, Snap will breakout above $10 and I bought $150k worth.""",
    },
    {
        "id": "1nqjmwv",
        "created_utc": 1758758400,
        "subreddit": "wallstreetbets",
        "title": "$750k in NBIS, Nezuko Body Pillow Formation, $150+ PT",
        "permalink": "/r/wallstreetbets/comments/1nqjmwv/750k_in_nbis_nezuko_body_pillow_formation_150_pt/",
        "source": "recovered_bitbbq_reddit_mirror",
        "selftext": """I just came back from Japan-desu and watched the Demon Slayer Movie. And then I realized, Nebius rhymes with Weebius.

And at that point I knew there was something up with the Nebius chart that I had to do DD on.
And then I realized the it was like when Sword Art Online came out. It was off to a good start then fell off season 2, which is why the chart declined.

Then we see star symbols of waifs. I can't read Japanese, but I know it's cute. So stock price went up.
Then it got replaced when demon slayer came out. the movie was great. And that's when we get serious with the TA. Tanjiro's hairline is spotted on the 1 month chart. That means it does have something to do with Demon Slayer. And because if we analyze the macro environment of the spike of Nezuko Body pillows by 80% after the Demon Slayer movie, we should also see a 80% spike in WEebius group.
Tanjiro always gets up after he gets beaten up, which is just manic character anime plot armor. Even despite a drop today, NBIUS will keep getting back up and going up because it's overpowered. There might have been some resistance because of weed haters, but we should follow body pillow sales, not what other people think.

For that reason I decided to put $750K into NBIS.

https://www.reddit.com/gallery/1nqjmwv""",
    },
    {
        "id": "1nkqqi6",
        "created_utc": 1758153600,
        "subreddit": "wallstreetbets",
        "title": "GRRR - Dan Da Dan Turbo Granny Formation, $100k YOLO",
        "permalink": "/r/wallstreetbets/comments/1nkqqi6/grrr_dan_da_dan_turbo_granny_formation_100k_yolo/",
        "source": "search_result_deleted_manual",
        "selftext": "",
        "removed_by_category": "moderator",
    },
    {
        "id": "1nd9fpz",
        "created_utc": 1757462400,
        "subreddit": "wallstreetbets",
        "title": "$100k+ in HIMS - Gym Bro Formation Spotted - $60+ Breakout",
        "permalink": "/r/wallstreetbets/comments/1nd9fpz/100k_in_hims_gym_bro_formation_spotted_60_breakout/",
        "source": "recovered_search_index_reddit",
        "selftext": """I was at the gym today, and I saw that 50% at 24 hour fitness were too jacked. That basically represents half of America and a huge target audience, which means revenue growth of half of America. Hims is doing 544m in revenue, but there's 170 million men in America. So if each man spends $10 a year, that's 1.7B in revenue to hims. Since each man wants to be jacked, and then the existing 50% want to stay jacked.
And then I realized, if you plotted the gym bro on top of the graph, it shows consolidation. From the first arm day, into a break, then the rest day before the next pump.
And then that's where I realized, HIMS will also break through that plateau as well because of performance enhancing drugs. And then just keep going without needing more rest days. The guy I saw at the bench press was watching the anime "Onegai Muscle", which means HIMS will too get the same anime plot armor from the muscle growth.
If you look at the lines, it shows the muscle growth TA formation, which means a breakout above $50+ and onward to $60.
So therefore HIMS stock should breakout beyond $60+ and why I bought $100k+ in hims.""",
    },
    {
        "id": "1nbtn61",
        "created_utc": 1757289600,
        "subreddit": "wallstreetbets",
        "title": "$100k+ in Sweetgreen. Sydney Sweeney Jeans formation spotted, $10+ Recovery.",
        "permalink": "/r/wallstreetbets/comments/1nbtn61/100k_in_sweetgreen_sydney_sweeney_jeans_formation/",
        "source": "recovered_search_index_reddit",
        "selftext": """Hello again friends.
Today I looked at Sweetgreen's chart when it dropped to $8.21 and saw the Sydney Sweeney Jeans commercial from American Eagle.
That's when I realized the chart extends to the legs of her jeans.
Given American obesity and how AEO did well on its earnings to shoot up 35%, I realized this was the same with Sweetgreen because the chart looks similar. Americans will likely buy more salad and change their diet cause people like to look hot again.
At the tail ends of the jeans, the TA means it's time for recovery. Not just any recovery, making Sweetgreen Great Again.
So I bought $100k in Sweetgreen for $10+ recovery.""",
    },
    {
        "id": "1lpsbxa",
        "created_utc": 1751414400,
        "subreddit": "wallstreetbets",
        "title": "$150k+ in Upwork - Nine Tailed Fox/Naruto Plot Armor Pattern Spotted - $17+ Breakout",
        "permalink": "/r/wallstreetbets/comments/1lpsbxa/150k_in_upwork_nine_tailed_foxnaruto_plot_armor/",
        "source": "recovered_search_index_reddit",
        "selftext": """Hello friends, I'm back. Here is UPWORK, UPWK and my explanation on why I bought $150k+ in shares.
At first, you see what looks like a CAT. It starts off with the two ears. Looks like a cat right?
Wrong. This is the NINE TAILED FOX Pattern, not just any cat. So as usual with the destruction of the hidden leaf village, UPWK had some rebuilding to do. A massive dump candle hits like Pain himself.
But what they don’t see… is that the chart needed this. Naruto HAS ARRIVED. You can see his hairline being formed in the chart. Which means, Naruto/UPWK is about to have some serious plot armor in the upcoming weeks and months.
You know what comes next. Naruto meets Tsunade. They didn't show this in the show but there's a bouncy entrance and the Chakara Massage Experience. Everyone knows there's a happy ending to Naruto because of his plot armor.
For that reason I believe Upwork will breakout $17+ and bought a decent amount. This is fully shown in the TA of the chart for anyone with a PHD such as myself.""",
    },
    {
        "id": "1l6dm8d",
        "created_utc": 1749340800,
        "subreddit": "wallstreetbets",
        "title": "Godzilla and Shower Formation spotted on Bitcoin Chart, Bought $350k in IBIT Calls",
        "permalink": "/r/wallstreetbets/comments/1l6dm8d/godzilla_and_shower_formation_spotted_on_bitcoin/",
        "source": "recovered_search_index_reddit",
        "selftext": """Hello again. After a few drinks, I have bought $350k+ in Bitcoin December 2027 ITM calls and plan to buy another few hundred thousand worth of 2026 ITM calls.
Why you might ask? Godzilla. That's all, Bitcoin looks like Godzilla.
That little wiggle in 2024? That's the tail of Godzilla.
The current bump? You think that's resistance? No. That's just its hunched back. Godzilla just wanted to buy Sydney Sweeney's bathwater and had bad posture while glued to the checkout screen.
And from now until 2027? He's gotten his order shipped and he's ready to terrorize the bears again. That's when the bulky neck and forms.
Godzilla literally shoots laser beams and fire. People debate about 100 men vs 1 gorilla, but it's not even a debate that 21 million Bears can't even scratch this monstrosity.
Because Bitcoin looks like Godzilla on the chart, I expect IBIT to reach $100+ and bought ITM calls to make a few hundred percent. Sydney Sweeney taking a shower formation also means IBIT is a buy.""",
    },
    {
        "id": "1ky326s",
        "created_utc": 1749168000,
        "subreddit": "wallstreetbets",
        "title": "Oscar Due Diligence - Crab Pattern Spotted $22+ Breakout",
        "permalink": "/r/wallstreetbets/comments/1ky326s/oscar_due_diligence_crab_pattern_spotted_22/",
        "source": "recovered_reddit_public_html",
        "selftext": """OKAY EVERYONE. THIS IS A BIG DEAL. You know Mr. Crabs and how he likes money right? Meet Oscar, the son in law of Mr Crabs.
Oscar barely ever shows up. This is rarer than Squidward playing clarinet well. But when he shows up, he PRINTS money. Today, Oscar the Crab emerged from Bikini Bottom and onto OSCR's 3 month chart.

Here's an analysis of the chart:

  1. Oscar's left claw formed. It's a very masculine claw like the ones on Larry the Lobster.

  2. Then comes the shallow retracement to form its belly. It was simply chilling and getting fat after eating too many crabby patties.
  3. Then the BOOM. The right claw spikes up. AND WILL Keep going up after seeing Sandy the squirrel. This isn't just any normal claw. It's a biological response from Oscar the Crab.

With Oscar's right claw now ready to reach Sandy's Cheeks, he's not here to mess around. He's here to FULLY extend his right claw to $22.

So I did what any logical investor would do after seeing Oscar the Crab on the chart - I bought a modest 7k shares or $100k worth in Oscar.""",
    },
]


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "codex-serenity-collector/1.0"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode("utf-8"))


def dt_from_utc(ts: int | float | None) -> str:
    if not ts:
        return ""
    return datetime.fromtimestamp(float(ts), tz=timezone.utc).strftime("%Y-%m-%d")


def slugify(text: str, limit: int = 72) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return text[:limit].strip("-") or "post"


def post_url(permalink: str) -> str:
    if permalink.startswith("http"):
        return permalink
    return "https://www.reddit.com" + permalink


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    return value.strip()


def infer_symbols(row: dict) -> list[str]:
    text = f"{row.get('title','')} {row.get('selftext','')}"
    symbols = set(re.findall(r"\$([A-Z][A-Z0-9]{1,5})\b", text))
    upper_title = row.get("title", "").upper()
    exact_title_symbols = {
        "AXTI", "META", "T1", "FLY", "SNAP", "NBIS", "GRRR", "HIMS",
        "IBIT", "OSCR", "ETOR", "BULLZ", "BULLW", "RKLB", "ETH",
        "AVGO", "SMCI", "NVDA", "PDD", "FFIE", "AEMD", "UNH", "HOOD",
    }
    for sym in exact_title_symbols:
        if re.search(rf"\b{re.escape(sym)}\b", upper_title):
            symbols.add(sym)
    keyword_map = {
        "SWEETGREEN": "SG",
        "UPWORK": "UPWK",
        "OSCAR": "OSCR",
        "ETORO": "ETOR",
        "BITCOIN": "BTC",
        "GOOGLE": "GOOGL",
        "WEBULL": "BULL",
        "ROCKET LAB": "RKLB",
        "ROCKETLAB": "RKLB",
    }
    for keyword, sym in keyword_map.items():
        if keyword in upper_title:
            symbols.add(sym)
    return sorted(symbols)


def body_status(row: dict) -> str:
    text = clean_text(row.get("selftext"))
    removed = row.get("removed_by_category") or ""
    if text and text not in {"[removed]", "[deleted]"} and not text.startswith("[ Removed by Reddit"):
        return "body_saved"
    if removed:
        return f"removed:{removed}"
    if row.get("source", "").startswith("reddit_profile_link"):
        return "link_only_local_reddit_blocked"
    return "no_body"


def normalize(row: dict, source: str) -> dict:
    out = {
        "id": row.get("id") or "",
        "created_utc": int(float(row.get("created_utc") or row.get("created") or 0)),
        "date_utc": dt_from_utc(row.get("created_utc") or row.get("created")),
        "subreddit": row.get("subreddit") or "",
        "title": row.get("title") or "",
        "permalink": row.get("permalink") or "",
        "url": post_url(row.get("permalink") or ""),
        "selftext": clean_text(row.get("selftext")),
        "removed_by_category": row.get("removed_by_category") or "",
        "source": row.get("source") or source,
    }
    out["symbols"] = infer_symbols(out)
    out["body_status"] = body_status(out)
    out["word_count"] = len(out["selftext"].split())
    return out


def load_records() -> list[dict]:
    RAW.mkdir(parents=True, exist_ok=True)
    POSTS.mkdir(parents=True, exist_ok=True)
    payload = fetch_json(PULLPUSH_URL)
    (RAW / "pullpush_author_AleaBito.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    by_id: dict[str, dict] = {}
    for item in payload.get("data", []):
        rec = normalize(item, "pullpush")
        if rec["id"]:
            current = by_id.get(rec["id"])
            if current is None or rec["word_count"] > current["word_count"]:
                by_id[rec["id"]] = rec

    for item in MANUAL_RECENT:
        rec = normalize(item, item.get("source", "manual"))
        if rec["id"]:
            current = by_id.get(rec["id"])
            if current is None or rec["word_count"] >= current["word_count"]:
                by_id[rec["id"]] = rec

    records = sorted(by_id.values(), key=lambda r: (r["created_utc"], r["id"]), reverse=True)
    (RAW / "merged_submissions.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return records


def write_csv(records: list[dict]) -> None:
    cols = [
        "date_utc",
        "created_utc",
        "id",
        "subreddit",
        "symbols",
        "title",
        "body_status",
        "word_count",
        "removed_by_category",
        "source",
        "url",
    ]
    with (ROOT / "submissions_dedup.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        for row in records:
            out = {k: row.get(k, "") for k in cols}
            out["symbols"] = ",".join(row.get("symbols", []))
            writer.writerow(out)

    slim = [
        {k: (",".join(r[k]) if k == "symbols" else r.get(k, "")) for k in cols}
        for r in records
    ]
    (ROOT / "submissions_dedup.json").write_text(
        json.dumps(slim, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def write_posts(records: list[dict]) -> None:
    for row in records:
        date = row["date_utc"] or "unknown-date"
        filename = f"{date}_{row['subreddit']}_{row['id']}_{slugify(row['title'])}.md"
        path = POSTS / filename
        symbols = ", ".join(row["symbols"]) if row["symbols"] else "未识别"
        body = row["selftext"] or (
            "_正文未抓到：本机无登录访问 Reddit API 被 403/超时拦截；"
            "索引中保留公开可确认标题和原帖链接。_"
        )
        content = f"""# {row['title']}

- Date UTC: {row['date_utc'] or 'unknown'}
- Subreddit: r/{row['subreddit']}
- Symbols: {symbols}
- Reddit ID: {row['id']}
- Source: {row['source']}
- Body status: {row['body_status']}
- URL: {row['url']}

## Body

{body}
"""
        path.write_text(content, encoding="utf-8")


def write_timeline(records: list[dict]) -> None:
    lines = [
        "# AleaBito / Serenity Reddit Timeline",
        "",
        "说明：时间以 UTC 计；`body_status=body_saved` 表示本地保存了正文。",
        "",
        "| Date | Subreddit | Symbols | Status | Title |",
        "|---|---|---|---|---|",
    ]
    for row in records:
        symbols = ", ".join(row["symbols"]) if row["symbols"] else ""
        title = row["title"].replace("|", "\\|")
        lines.append(
            f"| {row['date_utc']} | r/{row['subreddit']} | {symbols} | "
            f"{row['body_status']} | [{title}]({row['url']}) |"
        )
    (ROOT / "timeline.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_by_ticker(records: list[dict]) -> None:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in records:
        keys = row["symbols"] or ["UNSORTED"]
        for key in keys:
            grouped[key].append(row)

    lines = [
        "# AleaBito / Serenity by Ticker",
        "",
        "同一篇文章可能归入多个 ticker。`UNSORTED` 是标题和正文里没有明确识别到股票代码的帖子。",
        "",
    ]
    for sym in sorted(grouped):
        lines.append(f"## {sym}")
        lines.append("")
        for row in grouped[sym]:
            title = row["title"]
            lines.append(f"- {row['date_utc']} - [{title}]({row['url']}) - {row['body_status']}")
        lines.append("")
    (ROOT / "by_ticker.md").write_text("\n".join(lines), encoding="utf-8")


def write_combined_body(records: list[dict]) -> None:
    lines = [
        "# AleaBito / Serenity Readable Reddit Body Collection",
        "",
        "只收录 `body_status=body_saved` 的帖子正文；已删除或本机未能抓取正文的帖子请看 `timeline.md` 和 `posts/` 里的占位说明。",
        "",
    ]
    saved = [r for r in records if r["body_status"] == "body_saved"]
    for idx, row in enumerate(saved, 1):
        symbols = ", ".join(row["symbols"]) if row["symbols"] else "未识别"
        lines.extend([
            f"## {idx}. {row['title']}",
            "",
            f"- Date UTC: {row['date_utc']}",
            f"- Subreddit: r/{row['subreddit']}",
            f"- Symbols: {symbols}",
            f"- URL: {row['url']}",
            "",
            row["selftext"],
            "",
            "---",
            "",
        ])
    (ROOT / "AleaBito_DD合集.md").write_text("\n".join(lines), encoding="utf-8")


def write_readme(records: list[dict]) -> None:
    body_saved = sum(1 for r in records if r["body_status"] == "body_saved")
    removed = sum(1 for r in records if r["body_status"].startswith("removed:"))
    link_only = sum(1 for r in records if "link_only" in r["body_status"])
    source_counts = defaultdict(int)
    for r in records:
        source_counts[r["source"]] += 1

    source_lines = "\n".join(f"- {k}: {v}" for k, v in sorted(source_counts.items()))
    readme = f"""# AleaBito / Serenity DD Collection

生成时间：{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}

本资料夹整理 Reddit 用户 `u/AleaBito`（Serenity / `@aleabitoreddit`）公开可检索的 submissions。核心来源是 PullPush Reddit 历史索引，外加 Reddit 个人页当前可见的新帖链接手工补齐。

## 统计

- 去重 submissions：{len(records)}
- 已保存正文：{body_saved}
- 已删除/被移除：{removed}
- 仅链接/本机未抓到正文：{link_only}

## 文件

- `submissions_dedup.csv`：去重总表，适合表格软件打开。
- `submissions_dedup.json`：去重总表 JSON 版。
- `timeline.md`：按时间倒序排列。
- `by_ticker.md`：按识别出的 ticker 分组。
- `AleaBito_DD合集.md`：已抓到正文的帖子全文合集。
- `posts/`：逐篇 markdown 文件，能抓到正文的已放入正文。
- `raw/pullpush_author_AleaBito.json`：PullPush 原始返回。
- `raw/merged_submissions.json`：合并后的完整 JSON，包含正文。
- `third_party_tracker_snapshot.md`：第三方 Serenity Tracker 资料摘录。

## 来源分布

{source_lines}

## 抓取限制

本机无登录请求 Reddit 官方 API 时多次出现 `403 Blocked`、连接重置或超时。因此：

- PullPush 里有正文的帖子，已完整保存。
- Reddit 个人页最新可见但 PullPush 未收录的帖子，已补入标题和链接；其中 AXTI、META、T1 Energy 三篇已根据 Reddit JSON 可读输出补入正文。
- GRRR 一帖仅能确认标题和原链接，页面显示已被版主删除。

## 参考入口

- Reddit profile: https://www.reddit.com/user/AleaBito/submitted/
- PullPush API: https://api.pullpush.io/reddit/search/submission/?author=AleaBito&size=100&sort=desc
- Serenity Tracker: https://semiconstocks.com/
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


def write_tracker_snapshot() -> None:
    # This is a compact local snapshot of the public third-party tracker page.
    text = """# Third-party Serenity Tracker Snapshot

Source: https://semiconstocks.com/

This third-party page describes itself as a retail-friendly tracker for Serenity / @aleabitoreddit. It is not affiliated with Serenity. Its data is paraphrased from public posts and third-party coverage, so treat it as an auxiliary index rather than primary source material.

Highlighted active/flagged names shown on the page as of its May 26, 2026 update include:

- AXTI - AXT Inc. - photonics - active/high conviction
- SIVE - Sivers Semiconductors - photonics - active/high conviction
- AAOI - Applied Optoelectronics - photonics - active/high conviction
- AEHR - Aehr Test Systems - photonics - active/watch
- MRVL - Marvell Technology - photonics - active/safe
- COHR - Coherent - photonics - active/safe
- LITE - Lumentum - photonics - active/safe
- TSEM - Tower Semiconductor - photonics - active/safe
- SOI - Soitec - photonics - active/safe
- NBIS - Nebius - neocloud - active/high conviction
- IREN - IREN Limited - neocloud - flipped
- LNG, CVX, NEXT, MP - macro/energy and supply-chain names
- ETH, COIN - crypto-related views
- XFAB, NVTS, WOLF, AIRO, OSS, EWY, RDDT - newer or adjacent names
- BOT, VCX - listed as risk/avoidance warnings

For anything actionable, verify against Serenity's own latest X/Reddit posts.
"""
    (ROOT / "third_party_tracker_snapshot.md").write_text(text, encoding="utf-8")


def main() -> None:
    records = load_records()
    write_csv(records)
    write_posts(records)
    write_timeline(records)
    write_by_ticker(records)
    write_combined_body(records)
    write_readme(records)
    write_tracker_snapshot()
    print(json.dumps({
        "records": len(records),
        "body_saved": sum(1 for r in records if r["body_status"] == "body_saved"),
        "root": str(ROOT),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

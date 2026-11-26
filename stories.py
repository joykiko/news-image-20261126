# Story data for the 26 November 2026 front page.
# Every story was reported on Thursday 26 November 2026 and cross-checked
# against at least two independent roundups of the day (AP and Reuters
# daily summaries, plus the Open Chronicle and Inshorts day briefs).
# Count: 1 hero + 6 scenes + 8 grid + 10 map pins + 12 briefs = 37 stories.

HERO = {
    "kicker": "THE DAY'S STORY - TRADE",
    "headline": "AMERICA RAISES A TARIFF WALL AGAINST 14 ECONOMIES",
    "deck": (
        "Washington moves to tax factory goods from China, the European Union, "
        "Taiwan and 11 more economies, blaming subsidised overproduction. "
        "Duties could reach 40 percent; India is offered 17 instead of 25 "
        "with a trade deal. Partners push back as a new front opens in "
        "the trade war."
    ),
    "chips": ["14 PARTNERS TARGETED", "UP TO 40% PROPOSED", "INDIA: 25% OR 17% WITH A DEAL"],
}

# Six drawn scenes: (kind, headline, one-line deck)
SCENES = [
    ("parade", "MACY'S 100TH PARADE STOPPED BY STORM",
     "The centenary parade moves to Saturday - a first."),
    ("port", "HOUTHIS STRIKE SAUDI OIL PORTS",
     "Jizan port hit; Ras Tanura refinery claimed struck."),
    ("kyiv", "BALLISTIC MISSILES RAIN ON KYIV",
     "Overnight strikes wound seven; grain ships hit."),
    ("candles", "HONG KONG MARKS A YEAR OF GRIEF",
     "Flowers for the 168 killed in the Wang Fuk Court fire."),
    ("virus", "CONGO EBOLA PASSES 12,000 CASES",
     "Second-largest ever; violence drives responders out."),
    ("chess", "GAME 3: GUKESH v SINDAROV",
     "Youngest title match ever resumes in Geneva, 1-1."),
]

# Numbered stories for the main grid (stories 8-15 on the page).
GRID = [
    ("UKRAINE HITS A RUSSIAN AIR BASE",
     "Kyiv says its strike damaged five planes, and that it also hit two oil refineries in Russia's Samara region."),
    ("KIM ORDERS NUCLEAR WEAPONS EVERYWHERE",
     "North Korea's leader calls wider tactical nuclear deployment an 'urgent task' and vows more nuclear material."),
    ("NINE KILLED IN GAZA STRIKES",
     "Israeli strikes kill nine overnight, among them Hamas's appointed deputy education minister, medics say."),
    ("EU LEADERS SPLIT OVER MONEY",
     "Brussels argues over its next budget and a 45 billion euro loan for Ukraine, with unity out of reach."),
    ("EXPLOSION AT BANGKOK OIL PLANT",
     "A large blast and fire at a major oil facility in the Thai capital injures at least nine people."),
    ("EGYPT DETAINS DRIVER AFTER TANKER FIRE",
     "A driver is held over the fuel-tanker crash near Cairo that killed 31 people and injured 21."),
    ("16 DEAD IN FLOODED JAVA GOLD MINE",
     "Rescuers search a flooded illegal mine in West Java; 16 miners are confirmed dead, 10 still missing."),
    ("SEOUL RAISES RATES ON AI CHIP BOOM",
     "The Bank of Korea lifts its rate to 3.25 percent and upgrades growth forecasts on semiconductor demand."),
]

# Map pins (stories 16-25): (lon, lat, short text)
PINS = [
    (56, 26, "IRAN: two ships strike mines in Hormuz"),
    (32, 49, "Nations urge Russia to halt alleged riot-agent use"),
    (33, 69, "Murmansk governor jailed in corruption probe"),
    (36, 34, "LEBANON: second airport as Hezbollah's sway wanes"),
    (32, 15, "SUDAN: families return to ruined Khartoum homes"),
    (38, 1, "KENYA: court voids US-backed Ebola quarantine centre"),
    (96, 17, "MYANMAR signals defiance of ICJ genocide ruling"),
    (90, 24, "BANGLADESH: garment workers protest over wages"),
    (-4, 40, "SPAIN: far right climbs on immigration fears"),
    (-2, 53, "BRITAIN trawls 100,000 ex-soldiers in recall"),
]

# One-line briefs, two columns of six.
BRIEFS = [
    "GOLD sinks to a 15-month low as PCE data fuels Fed hike bets",
    "MEMORY-CHIP shortage triples some RAM prices before Black Friday",
    "FCC clears SpaceX 'Starmind' constellation of orbital data centres",
    "MICROSOFT: Salt Typhoon and N. Korea hackers adopt AI tool ARTEX",
    "NEW YORK bans AI chatbots posing as human to children",
    "FIFA says a cyberattack took personal and business data",
    "DURAN DURAN guitarist Andy Taylor dies at 65",
    "US approves a $622m F-16 support package for Ukraine",
    "IOWA: the Army's lead-azide stockpile blast leaves air clean",
    "STEELERS cut Aaron Rodgers after TV clash with coach McCarthy",
    "INDIA marks 18 years since the 26/11 Mumbai attacks",
    "FEDEX MD-11 overruns Miami runway, closing most runways",
]

DATE_CHECK = (
    "DATE CHECK - Left out as not 26 November news: the Shenzhou-24 launch (25 Nov; only Pakistan's "
    "congratulations fell today), the judges' steer in the Netanyahu case (first reported 25 Nov), and the "
    "Kerch Bridge strike (part of a week-long campaign). The Wang Fuk Court fire burned on 26 Nov 2025 - "
    "today's story is its first anniversary. Every story above was reported on 26 Nov 2026."
)

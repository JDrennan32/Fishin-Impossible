import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Fishin' Impossible", layout="wide")

# Title
st.title("Fishin' Impossible")

# Fish categories including new Cheat Sheets tab
fish_names = ["Largemouth", "Smallmouth", "Bluegill", "Crappie", "Channel Catfish"]
tabs = st.tabs(fish_names + ["Cheat Sheets"])

# Cheat sheet content data structure
cheat_data = {
    "Largemouth": {
        "Pre-Spawn": {
            "temp_range": "45–58°F",
            "dates": "Late February – Early April",
            "weight_range": "3.5-5.0 lbs",
            "behavior": (
                "Pre-spawn largemouth are feeding aggressively as they prepare to spawn. "
                "They're moving from deeper wintering holes toward shallower spawning flats. During this phase, "
                "they stage near secondary points, channel swings, and rocky banks close to their future spawning areas. "
                "Water temps are still chilly, so they’re often sluggish in the morning but more active in the afternoon. "
                "Cold fronts can push them back deeper for a day or two. Because of the transition, this season offers one of "
                "the best chances to catch big females feeding up — especially in lakes and ponds."
            ),
            "table": [
                {"Bait": "Jerkbait", "Retrieval Style": "Twitch–pause", "Colors": "Ghost minnow, Natural shad", "Best Location": "Secondary points near spawning flats (Lake)"},
                {"Bait": "Flat-side crankbait", "Retrieval Style": "Steady medium retrieve", "Colors": "Red craw, Sexy shad", "Best Location": "Gravel banks near main lake points (Pond/Lake)"},
                {"Bait": "Lipless crankbait", "Retrieval Style": "Yo-yo retrieve", "Colors": "Chrome blue, Red craw", "Best Location": "Wind-blown flats and shallow ledges (Pond)"},
                {"Bait": "Jig", "Retrieval Style": "Slow drag or hop", "Colors": "Green pumpkin, Black & blue", "Best Location": "Rock transitions and brushy channels (Lake)"},
                {"Bait": "Finesse worm (shaky head)", "Retrieval Style": "Subtle bottom shake", "Colors": "Watermelon seed, Green pumpkin", "Best Location": "Slow eddies near shallow cover (River)"}
            ],
            "target_depth": "Lake/Pond: 4–10 ft, River: 3–6 ft"
        },
        "Spawn": {
            "temp_range": "58–72°F",
            "dates": "Late March – May",
            "weight_range": "3.0-4.5 lbs",
            "behavior": (
                "During the spawn, largemouth bass move into shallow, protected areas to build nests and lay eggs. "
                "They become territorial and aggressive, especially the males guarding the beds. "
                "Fish are usually found in 1–6 feet of water around flat coves, sandy or gravel banks, and near shallow cover like stumps or vegetation. "
                "Bites can be reactionary due to nest protection rather than feeding, so sight-fishing and slow presentations are effective."
            ),
            "table": [
                {"Bait": "Soft plastic lizard", "Retrieval Style": "Slow crawl over bed", "Colors": "White pearl, Green pumpkin", "Best Location": "Gravel flats and shallow coves (Lake)"},
                {"Bait": "Wacky rig stickbait", "Retrieval Style": "Subtle flutter and pause", "Colors": "Watermelon red, Green pumpkin", "Best Location": "Flat banks with isolated cover (Pond/Lake)"},
                {"Bait": "Tube bait", "Retrieval Style": "Short hops or deadstick", "Colors": "Smoke black flake, White", "Best Location": "Near stumps and spawning beds (Lake)"},
                {"Bait": "Texas-rigged craw", "Retrieval Style": "Lift and drop", "Colors": "Black/blue, Natural craw", "Best Location": "Vegetation edges and shallow logs (Pond)"},
                {"Bait": "Fluke", "Retrieval Style": "Twitch–pause over nests", "Colors": "White, Ayu", "Best Location": "Shallow pools near spawning pockets (River)"}
            ],
            "target_depth": "Lake/Pond: 1–6 ft, River: 2–5 ft"
        },
        "Post-Spawn": {
            "temp_range": "65–78°F",
            "dates": "Mid April – June",
            "weight_range": "2.0-3.5 lbs",
            "behavior": (
                "After the spawn, male bass remain on beds for a short period to protect fry, while females recover in nearby cover. "
                "Many bass suspend or move toward the first drop-offs and weed lines. This period is transitional — fish behavior can be inconsistent. "
                "Feeding activity generally increases as fish recover, and topwater lures start to become more effective in early mornings and evenings."
            ),
            "table": [
                {"Bait": "Topwater popper", "Retrieval Style": "Pop–pause near surface", "Colors": "Bone, Shad", "Best Location": "Shallow points near post-spawn beds (Lake)"},
                {"Bait": "Swimbait", "Retrieval Style": "Slow roll along weed lines", "Colors": "Bluegill, Natural shad", "Best Location": "Edge of flats near vegetation (Pond/Lake)"},
                {"Bait": "Spinnerbait", "Retrieval Style": "Medium retrieve through cover", "Colors": "White/chartreuse, Sexy shad", "Best Location": "Wind-blown banks and laydowns (Pond)"},
                {"Bait": "Ned rig", "Retrieval Style": "Hop or deadstick", "Colors": "Green pumpkin, Brown", "Best Location": "Transition areas near creek channels (Lake)"},
                {"Bait": "Buzzbait", "Retrieval Style": "Fast retrieve on top", "Colors": "Black, White", "Best Location": "Shady banks and low-light pockets (River)"}
            ],
            "target_depth": "Lake/Pond: 3–8 ft, River: 2–6 ft"    
        },
        "Summer": {
            "temp_range": "75–90°F",
            "dates": "June – August",
            "weight_range": "2.0-3.2 lbs",
            "behavior": (
                "During the summer, largemouth bass are less active during the heat of the day and feed more aggressively in low-light hours. "
                "In lakes and ponds, they tend to relate to deeper structure, vegetation edges, and shaded areas. "
                "In rivers, current breaks and eddies become prime ambush zones. "
                "Fishing early morning and late evening with moving baits or topwaters is productive, while slower presentations work in deeper, shaded midday spots."
            ),
            "table": [
                {"Bait": "Frog (hollow body)", "Retrieval Style": "Walk across pads or pause in holes", "Colors": "Black, Green pumpkin", "Best Location": "Lily pads and mats (Pond)"},
                {"Bait": "Texas-rigged worm", "Retrieval Style": "Drag and pause on bottom", "Colors": "Junebug, Redbug", "Best Location": "Brush piles and submerged timber (Lake)"},
                {"Bait": "Chatterbait", "Retrieval Style": "Slow roll near grass edges", "Colors": "White/chartreuse, Green pumpkin", "Best Location": "Grass transitions and open pockets (Lake)"},
                {"Bait": "Drop shot", "Retrieval Style": "Subtle twitch and hold in place", "Colors": "Morning dawn, Smoke", "Best Location": "Deep structure and creek channel drops (Lake)"},
                {"Bait": "Squarebill crankbait", "Retrieval Style": "Bounce off cover", "Colors": "Firetiger, Sexy shad", "Best Location": "Current seams and riprap (River)"}
            ],
            "target_depth": "Lake/Pond: 5–12 ft, River: 3–8 ft"
        },
        "Fall": {
            "temp_range": "65–55°F",
            "dates": "September – Mid-November",
            "weight_range": "2.8-4.0 lbs",
            "behavior": (
                "In the fall, largemouth bass feed heavily to prepare for the coming winter. They often chase baitfish that migrate toward creeks, flats, and shallow coves. "
                "Water temperatures are cooling, and bass become more active throughout the day, especially in shallower areas during overcast conditions. "
                "This is a great time to use moving baits that mimic shad or smaller fish. Windy banks and transition zones (where shallow flats meet deeper water) become key feeding locations."
            ),
            "table": [
                {"Bait": "Spinnerbait", "Retrieval Style": "Slow roll along grass edges", "Colors": "White/chartreuse, Gold shiner", "Best Location": "Creek mouths and flat points (Lake)"},
                {"Bait": "Crankbait (medium diving)", "Retrieval Style": "Steady retrieve with pauses", "Colors": "Shad, Firetiger", "Best Location": "Rock transitions and deep flats (Lake)"},
                {"Bait": "Chatterbait", "Retrieval Style": "Burn and kill retrieve", "Colors": "Black/blue, Green pumpkin", "Best Location": "Shallow weedlines and stump fields (Pond)"},
                {"Bait": "Topwater walking bait", "Retrieval Style": "Walk-the-dog action", "Colors": "Bone, Chrome", "Best Location": "Windy coves and open flats (Lake)"},
                {"Bait": "Jig", "Retrieval Style": "Hopped along bottom", "Colors": "PB&J, Black and red", "Best Location": "Eddy pockets and backwater seams (River)"}
            ],
            "target_depth": "Lake/Pond: 4–10 ft, River: 3–6 ft"
        },
        "Winter": {
            "temp_range": "45–55°F",
            "dates": "Mid-November – February",
            "weight_range": "2.0-3.0 lbs",
            "behavior": (
                "Largemouth bass become sluggish in the cold of winter and conserve energy by staying near deep cover. "
                "They often group up in deeper holes, channels, and ledges where water temperatures are more stable. "
                "Feeding windows are short and typically occur during the warmest part of the day. "
                "Finesse techniques and slow presentations are most effective, and bites can be subtle. "
                "In ponds, bass often suspend near the deepest structure available, while in rivers they hold tight to slow current areas."
            ),
            "table": [
                {"Bait": "Blade bait", "Retrieval Style": "Lift and fall vertically", "Colors": "Silver, Gold", "Best Location": "Deep creek channels and points (Lake)"},
                {"Bait": "Jigging spoon", "Retrieval Style": "Vertical jigging with small hops", "Colors": "Chrome, White", "Best Location": "Suspended over deep structure (Pond/Lake)"},
                {"Bait": "Finesse jig", "Retrieval Style": "Dragged slowly across bottom", "Colors": "Brown, Black & blue", "Best Location": "Rocky bottom and drop-offs (Lake)"},
                {"Bait": "Soft plastic worm (drop shot)", "Retrieval Style": "Minimal movement or deadstick", "Colors": "Green pumpkin, Morning dawn", "Best Location": "Deep water ledges and humps (Pond)"},
                {"Bait": "Hair jig", "Retrieval Style": "Slow swimming or hop", "Colors": "Black, Marabou", "Best Location": "Slow current bends and pools (River)"}
            ],
            "target_depth": "Lake/Pond: 8–20 ft, River: 5–12 ft"
        }
    },
    "Bluegill": {
        "Spring": {
            "temp_range": "55–68°F",
            "dates": "March – April",
            "weight_range": "0.6-1.0 lbs",
            "behavior": (
                "In spring, bluegill begin moving out of deep wintering holes and transition toward shallower areas as water temperatures rise. "
                "They feed actively in preparation for the spawn, targeting insects, small minnows, and worms. "
                "You’ll find them staging near brush piles, weed edges, and gradual slopes in ponds and coves. "
                "Sunny afternoons are particularly productive as water warms and fish move into feeding zones. "
                "They prefer slower water in rivers and often hold tight to cover."
            ),
            "table": [
                {"Bait": "Worm under bobber", "Retrieval Style": "Still or slow drift", "Colors": "Natural brown, Redworm", "Best Location": "Weed edges near coves (Pond)"},
                {"Bait": "Inline spinner", "Retrieval Style": "Slow roll", "Colors": "Gold, Chartreuse", "Best Location": "Brush pile drop-offs (Lake)"},
                {"Bait": "Tiny crankbait", "Retrieval Style": "Pause-pull near cover", "Colors": "Chrome/blue, Baby bass", "Best Location": "Grass lines and timber pockets (Lake)"},
                {"Bait": "Cricket on bobber", "Retrieval Style": "Light twitch", "Colors": "Natural", "Best Location": "Near shallow cover and laydowns (Pond)"},
                {"Bait": "Curl tail grub", "Retrieval Style": "Slow swim or fall", "Colors": "White, Chartreuse", "Best Location": "Slow pools and undercut banks (River)"}
            ],
            "target_depth": "Lake/Pond: 2–6 ft, River: 2–4 ft"
        },
        "Spawn": {
            "temp_range": "70–85°F",
            "dates": "May – July",
            "weight_range": "0.8-1.2 lbs",
            "behavior": (
                "During the spawn, bluegill move into shallow, sandy, or gravel-bottomed areas to build beds in colonies. "
                "They’re highly aggressive during this time, guarding nests from predators and striking at anything nearby. "
                "This makes them easier to catch, especially in clear water where beds are visible. "
                "The bite is most consistent in the morning and late afternoon, especially during stable weather patterns."
            ),
            "table": [
                {"Bait": "Cricket under bobber", "Retrieval Style": "Still or light twitch", "Colors": "Natural", "Best Location": "Spawning colonies near gravel banks (Pond)"},
                {"Bait": "Worm (half-nightcrawler)", "Retrieval Style": "Drop to bed and wait", "Colors": "Red, Natural brown", "Best Location": "Sandy flats near brush (Lake)"},
                {"Bait": "Tiny tube jig", "Retrieval Style": "Small hops or deadstick", "Colors": "Chartreuse, Pink", "Best Location": "Clear bed areas and docks (Lake)"},
                {"Bait": "Mini paddle tail", "Retrieval Style": "Slow swim above beds", "Colors": "Pearl, Silver flake", "Best Location": "Vegetation edges near spawning sites (Pond)"},
                {"Bait": "Inline spinner", "Retrieval Style": "Medium retrieve past beds", "Colors": "White, Gold", "Best Location": "Slow-moving sandy cuts and slack water (River)"}
            ],
            "target_depth": "Lake/Pond: 1–5 ft, River: 1–4 ft"
        },
        "Post-Spawn": {
            "temp_range": "80–85°F",
            "dates": "July – Early August",
            "weight_range": "0.5-0.8 lbs",
            "behavior": (
                "After spawning, bluegill gradually disperse from their beds and seek refuge in nearby cover. "
                "They often suspend around deeper weed edges, submerged timber, and shaded structures. "
                "Feeding resumes steadily as they recover, but bites may be more subtle in mid-day heat. "
                "Early morning and late evening offer the best bite windows. "
                "In rivers, they move toward deeper slackwater pools or current breaks with nearby structure."
            ),
            "table": [
                {"Bait": "Half nightcrawler", "Retrieval Style": "Slow drag with pauses", "Colors": "Natural brown, Red", "Best Location": "Weedline edges and brush piles (Lake)"},
                {"Bait": "Mini tube jig", "Retrieval Style": "Hop and settle", "Colors": "Chartreuse, Pink", "Best Location": "Shady undercut banks and deep timber (Pond)"},
                {"Bait": "Inline spinner", "Retrieval Style": "Steady slow retrieve", "Colors": "Gold, Orange", "Best Location": "Deeper flats near structure (Lake)"},
                {"Bait": "Cricket under slip bobber", "Retrieval Style": "Still or slight twitch", "Colors": "Natural", "Best Location": "Slackwater eddies with submerged logs (River)"},
                {"Bait": "Tiny swimbait", "Retrieval Style": "Medium retrieve through mid-depth", "Colors": "Silver flake, Pearl", "Best Location": "Shade lines and isolated cover (Pond)"}
            ],
            "target_depth": "Lake/Pond: 4–10 ft, River: 3–6 ft"
        },
        "Summer": {
            "temp_range": "85–90°F",
            "dates": "Mid August – Mid September",
            "weight_range": "0.6-0.9 lbs",
            "behavior": (
                "During the peak of summer, bluegill retreat to deeper, cooler waters during midday, becoming most active in the early morning and evening. "
                "They often school around submerged structure, dock pilings, and weed edges where oxygen levels are stable. "
                "Because of high temperatures and bright sun, they can be more sluggish and prefer slower presentations. "
                "Target shaded areas or deeper cover with subtle, natural baits to trigger bites. In rivers, focus on current breaks and deeper pools."
            ),
            "table": [
                {"Bait": "Worm on split shot rig", "Retrieval Style": "Slow drag near cover", "Colors": "Natural brown, Red", "Best Location": "Weedlines and drop-offs (Lake)"},
                {"Bait": "Inline spinner", "Retrieval Style": "Slow roll near shade", "Colors": "Gold, Orange", "Best Location": "Dock pilings and submerged timber (Pond)"},
                {"Bait": "Mini swimbait", "Retrieval Style": "Mid-depth swim retrieve", "Colors": "Silver flake, Pearl", "Best Location": "Shade lines and deeper cover (Lake)"},
                {"Bait": "Cricket under slip bobber", "Retrieval Style": "Still or twitch", "Colors": "Natural", "Best Location": "Slackwater pockets and brushy banks (River)"},
                {"Bait": "Hair jig", "Retrieval Style": "Lift-drop near bottom", "Colors": "Black, White", "Best Location": "Deep edges near structure (Pond)"}
            ],
            "target_depth": "Lake/Pond: 5–12 ft, River: 3–6 ft"
        },
        "Fall": {
            "temp_range": "60–70°F",
            "dates": "Late September – Early November",
            "weight_range": "0.7-1.0 lbs",
            "behavior": (
                "In the fall, bluegill become active again as water temperatures cool and oxygen levels stabilize. "
                "They feed heavily in preparation for winter, often forming loose schools around deeper vegetation, drop-offs, and structure. "
                "They roam more than in the summer and may suspend in mid-depth water chasing baitfish. "
                "Afternoon fishing is often best, especially on sunny days. In rivers, focus on deeper pools and current breaks with nearby cover."
            ),
            "table": [
                {"Bait": "Worm on jighead", "Retrieval Style": "Lift and settle", "Colors": "Red, Natural brown", "Best Location": "Weedline drop-offs and brush piles (Lake)"},
                {"Bait": "Inline spinner", "Retrieval Style": "Medium retrieve", "Colors": "Gold, Chartreuse", "Best Location": "Near submerged timber and docks (Pond)"},
                {"Bait": "Small crankbait", "Retrieval Style": "Steady retrieve with pauses", "Colors": "Shad, Firetiger", "Best Location": "Transition banks and ledges (Lake)"},
                {"Bait": "Tube jig", "Retrieval Style": "Hop near bottom", "Colors": "Pink, Smoke", "Best Location": "Slow current holes near cover (River)"},
                {"Bait": "Tiny swimbait", "Retrieval Style": "Slow roll at mid-depth", "Colors": "Silver flake, White", "Best Location": "Shade lines and brush piles (Pond)"}
            ],
            "target_depth": "Lake/Pond: 4–10 ft, River: 3–6 ft"
        },
        "Winter": {
            "temp_range": "45–50°F",
            "dates": "Mid November – February",
            "weight_range": "0.5-0.8 lbs",
            "behavior": (
                "In winter, bluegill slow down significantly and concentrate in deeper, more stable parts of the water. "
                "They often school tightly near the bottom or suspend over structure like brush piles, humps, or creek channels. "
                "Their feeding activity is limited to short windows, typically during the warmest part of the day. "
                "Presentations must be extremely subtle and slow, often vertical or deadsticked. In rivers, they hold tight in deeper eddies or slow pools."
            ),
            "table": [
                {"Bait": "Waxworm on ice jig", "Retrieval Style": "Deadstick or gentle jiggle", "Colors": "Glow, Pink", "Best Location": "Brush piles in deep coves (Lake)"},
                {"Bait": "Tiny tungsten jig", "Retrieval Style": "Lift-fall with pauses", "Colors": "Chartreuse, Red", "Best Location": "Deep submerged structure (Pond)"},
                {"Bait": "Micro plastic grub", "Retrieval Style": "Slow drag near bottom", "Colors": "White, Smoke", "Best Location": "Drop-offs near creek channels (Lake)"},
                {"Bait": "Hair jig", "Retrieval Style": "Subtle twitch and settle", "Colors": "Black, Olive", "Best Location": "Calm, deep bends and holes (River)"},
                {"Bait": "Half nightcrawler", "Retrieval Style": "Still under bobber or twitch", "Colors": "Natural brown", "Best Location": "Deep basin edges and humps (Pond)"}
            ],
            "target_depth": "Lake/Pond: 8–15 ft, River: 5–10 ft"
        }
    },
    "Crappie": {
        "Pre-Spawn": {
            "temp_range": "48–55°F",
            "dates": "Late February – Early March",
            "weight_range": "1.0–1.5 lbs",
            "behavior": (
                "Pre-spawn crappie stage just outside their eventual spawning areas, typically in slightly deeper water near brush piles, "
                "drop-offs, and creek channels. They begin feeding actively as water temperatures warm, preparing to move shallow. "
                "Fish tend to concentrate in schools and may suspend near vertical structure or hold tight to cover. "
                "Cold fronts can push them deeper temporarily, so timing and stable conditions are key. "
                "Late afternoons and sunny days often bring fish closer to shallow staging areas."
            ),
            "table": [
                {"Bait": "Marabou jig", "Retrieval Style": "Slow vertical jigging", "Colors": "Black/chartreuse, White", "Best Location": "Brush piles off spawning flats (Lake)"},
                {"Bait": "Small tube jig", "Retrieval Style": "Lift-fall with pause", "Colors": "Pink/white, Chartreuse", "Best Location": "Drop-offs near creek mouths (Pond)"},
                {"Bait": "Minnow under slip bobber", "Retrieval Style": "Still or slow drift", "Colors": "Live minnow", "Best Location": "Suspended near submerged timber (Lake)"},
                {"Bait": "Blade bait", "Retrieval Style": "Lift and fall near structure", "Colors": "Silver, Chrome", "Best Location": "Channel edges and ledges (River)"},
                {"Bait": "Crappie crankbait", "Retrieval Style": "Slow steady retrieve", "Colors": "Shad, Firetiger", "Best Location": "Staging points near spawning coves (Pond/Lake)"}
            ],
            "target_depth": "Lake/Pond: 6–12 ft, River: 4–8 ft"
        },
        "Spawn": {
            "temp_range": "56–68°F",
            "dates": "Mid March – Late April",
            "weight_range": "1.2–1.8 lbs",
            "behavior": (
                "During the spawn, crappie move into shallow protected areas to lay eggs, often in less than 5 feet of water. "
                "Males fan out nests and guard them, while females move in briefly to deposit eggs. "
                "Crappie become highly concentrated and aggressive in spawning coves, near submerged wood, and around shoreline vegetation. "
                "They are easier to target in clear water where beds are visible. Wind-protected pockets with warmer water tend to hold the most fish."
            ),
            "table": [
                {"Bait": "Tube jig", "Retrieval Style": "Pitch and pause", "Colors": "Chartreuse, White", "Best Location": "Shallow brush and stake beds (Lake)"},
                {"Bait": "Minnow under float", "Retrieval Style": "Set and twitch", "Colors": "Live minnow", "Best Location": "Grassy banks and timber edges (Pond)"},
                {"Bait": "Hair jig", "Retrieval Style": "Slow swim or hop", "Colors": "Black, Pink", "Best Location": "Shallow spawning pockets (Lake)"},
                {"Bait": "Beetle spin", "Retrieval Style": "Steady retrieve", "Colors": "White/chartreuse, Yellow", "Best Location": "Flat gravel points and creek arms (Pond/Lake)"},
                {"Bait": "Tiny swimbait", "Retrieval Style": "Glide over beds", "Colors": "Silver flake, Pearl", "Best Location": "Sandy bottoms near cover (River)"}
            ],
            "target_depth": "Lake/Pond: 2–5 ft, River: 2–6 ft"
        },
        "Post-Spawn": {
            "temp_range": "69–75°F",
            "dates": "Late April – May",
            "weight_range": "1.0–1.6 lbs",
            "behavior": (
                "After the spawn, crappie begin to disperse from shallow nesting areas and move toward slightly deeper cover. "
                "Males may linger briefly to guard fry, but most fish return to submerged brush, timber, or weed edges. "
                "Feeding behavior can be inconsistent as fish recover from spawning, but action improves with warming temperatures. "
                "Look for crappie to suspend off structure or stack up along channel breaks and deeper transitions. "
                "Late evenings and early mornings often produce the best bite windows."
            ),
            "table": [
                {"Bait": "Small swimbait", "Retrieval Style": "Slow roll near cover", "Colors": "Silver flake, Shad", "Best Location": "Submerged brush piles near spawning flats (Lake)"},
                {"Bait": "Minnow under slip bobber", "Retrieval Style": "Still or twitch", "Colors": "Live minnow", "Best Location": "Weed edges near deeper drop-offs (Pond)"},
                {"Bait": "Hair jig", "Retrieval Style": "Lift-fall in open pockets", "Colors": "Black, Chartreuse", "Best Location": "Ledges and timber lines (Lake)"},
                {"Bait": "Blade bait", "Retrieval Style": "Hop along bottom", "Colors": "Gold, Chrome", "Best Location": "Mid-depth channel edges (River)"},
                {"Bait": "Tube jig", "Retrieval Style": "Bounce off structure", "Colors": "Pink/white, Green pumpkin", "Best Location": "Deeper coves with isolated cover (Pond/Lake)"}
            ],
            "target_depth": "Lake/Pond: 6–14 ft, River: 4–10 ft"
        },
        "Early Summer": {
            "temp_range": "76–81°F",
            "dates": "June – Early July",
            "weight_range": "1.1–1.7 lbs",
            "behavior": (
                "As summer begins, crappie move away from spawning areas and settle into deeper, cooler zones with nearby structure. "
                "They often suspend over submerged brush, ledges, and drop-offs, particularly where there's shade or temperature stability. "
                "Crappie feed early and late in the day, becoming more sluggish under direct sun. "
                "Targeting them vertically or with slow presentations around structure is key during this season. "
                "In rivers, they shift toward deeper eddies and slow-moving current edges."
            ),
            "table": [
                {"Bait": "Hair jig", "Retrieval Style": "Vertical twitch and drop", "Colors": "Black/chartreuse, Pink", "Best Location": "Submerged timber in coves (Lake)"},
                {"Bait": "Minnow under slip bobber", "Retrieval Style": "Hover over brush", "Colors": "Live minnow", "Best Location": "Shaded cover near drop-offs (Pond)"},
                {"Bait": "Tube jig", "Retrieval Style": "Lift-fall along ledges", "Colors": "Chartreuse, White", "Best Location": "Channel swings and brush piles (Lake)"},
                {"Bait": "Blade bait", "Retrieval Style": "Jigged through current breaks", "Colors": "Silver, Gold", "Best Location": "Deep pools and rock ledges (River)"},
                {"Bait": "Small crankbait", "Retrieval Style": "Slow crank at mid-depth", "Colors": "Shad, Pearl", "Best Location": "Deeper flats with scattered cover (Pond/Lake)"}
            ],
            "target_depth": "Lake/Pond: 8–15 ft, River: 6–10 ft"
        },
        "Late Summer": {
            "temp_range": "76–85°F",
            "dates": "Mid July – August",
            "weight_range": "1.0–1.6 lbs",
            "behavior": (
                "In late summer, crappie often hold deeper during the heat of the day, especially around structure like submerged timber, bridge pilings, and drop-offs. "
                "They can be more scattered and less aggressive, so vertical presentations and precision targeting become important. "
                "Look for early morning and late evening windows when crappie suspend higher in the water column to feed. "
                "In rivers, they concentrate in deeper eddies and slower-moving channels with available cover."
            ),
            "table": [
                {"Bait": "Tube jig", "Retrieval Style": "Slow lift-fall", "Colors": "Chartreuse, White", "Best Location": "Timber lines near deeper flats (Lake)"},
                {"Bait": "Minnow under slip bobber", "Retrieval Style": "Still or drift", "Colors": "Live minnow", "Best Location": "Shade near structure (Pond)"},
                {"Bait": "Hair jig", "Retrieval Style": "Subtle twitch", "Colors": "Black, Pink", "Best Location": "Brush piles and ledges (Lake)"},
                {"Bait": "Blade bait", "Retrieval Style": "Vertical jigging", "Colors": "Gold, Silver", "Best Location": "River channels and drop-offs (River)"},
                {"Bait": "Small crankbait", "Retrieval Style": "Mid-depth steady retrieve", "Colors": "Firetiger, Shad", "Best Location": "Deep weed edges and coves (Pond/Lake)"}
            ],
            "target_depth": "Lake/Pond: 10–18 ft, River: 6–12 ft"
        },
        "Fall": {
            "temp_range": "60–70°F",
            "dates": "September – Early November",
            "weight_range": "1.2–1.7 lbs",
            "behavior": (
                "In fall, crappie feed heavily in preparation for winter, often chasing schools of baitfish into shallower water. "
                "They become more active throughout the day, especially during stable weather and wind-blown banks. "
                "Fish can be found transitioning between shallow flats and nearby deep cover like brush piles, docks, and ledges. "
                "Expect crappie to suspend more frequently and follow bait movement, particularly in lakes and ponds. "
                "In rivers, focus on deeper bends and eddies with access to nearby feeding zones."
            ),
            "table": [
                {"Bait": "Crappie jig", "Retrieval Style": "Cast and pendulum swing", "Colors": "Chartreuse, White", "Best Location": "Brush piles near flats (Lake)"},
                {"Bait": "Minnow under bobber", "Retrieval Style": "Slow drift with twitch", "Colors": "Live minnow", "Best Location": "Windy banks near structure (Pond)"},
                {"Bait": "Small crankbait", "Retrieval Style": "Mid-speed retrieve with pauses", "Colors": "Shad, Firetiger", "Best Location": "Transition zones and docks (Lake)"},
                {"Bait": "Tube jig", "Retrieval Style": "Hop across bottom", "Colors": "Pink, Smoke", "Best Location": "Deeper flats and bends (River)"},
                {"Bait": "Hair jig", "Retrieval Style": "Lift-fall near suspended schools", "Colors": "Black, Yellow", "Best Location": "Drop-offs near feeding grounds (Pond/Lake)"}
            ],
            "target_depth": "Lake/Pond: 6–12 ft, River: 5–10 ft"
        },
        "Winter": {
            "temp_range": "38–55°F",
            "dates": "November – February",
            "weight_range": "1.0–1.4 lbs",
            "behavior": (
                "In winter, crappie concentrate in the deepest parts of lakes, ponds, and rivers where water temperatures are most stable. "
                "They often form tight schools and suspend just above the bottom or around vertical cover like timber or bridge pilings. "
                "Feeding activity slows, with short bite windows usually occurring during the warmest part of the day. "
                "Precise vertical presentations and subtle movement are critical. In rivers, target deep eddies, pools, and the slow side of current seams."
            ),
            "table": [
                {"Bait": "Hair jig", "Retrieval Style": "Slow vertical twitch", "Colors": "Black, Purple", "Best Location": "Deep timber and ledges (Lake)"},
                {"Bait": "Minnow on ice jig", "Retrieval Style": "Deadstick or slight lift", "Colors": "Live minnow", "Best Location": "Near bottom over brush piles (Pond)"},
                {"Bait": "Tungsten jig with plastic", "Retrieval Style": "Lift-drop with long pauses", "Colors": "Chartreuse, White", "Best Location": "Deep basin structure (Lake)"},
                {"Bait": "Blade bait", "Retrieval Style": "Short hops on bottom", "Colors": "Silver, Chrome", "Best Location": "Slow current holes and ledges (River)"},
                {"Bait": "Micro tube jig", "Retrieval Style": "Hover or pendulum swing", "Colors": "Pink, Glow", "Best Location": "Staging areas near channels (Pond/Lake)"}
            ],
            "target_depth": "Lake/Pond: 12–25 ft, River: 8–15 ft"
        }
    }
}

# Corrected Dropdown options for Seasons
season_options_dict = {
    "Largemouth": ["Select...", "Pre-Spawn", "Spawn", "Post-Spawn", "Summer", "Fall", "Winter"],
    "Smallmouth": ["Select...", "Early Spring", "Spawn", "Late Summer", "Fall"],
    "Bluegill": ["Select...", "Spring", "Spawn", "Post-Spawn", "Summer", "Fall", "Winter"],
    "Crappie": ["Select...", "Pre-Spawn", "Spawn", "Post-Spawn", "Early Summer", "Late Summer", "Fall", "Winter"],
    "Channel Catfish": ["Select...", "Spring", "Summer", "Fall", "Winter"]
}

# Water temperature options based on fish and season
water_temp_options_dict = {
    "Largemouth": {
        "Pre-Spawn": ["Cold (45-55F)", "Mild (55-58F)"],
        "Spawn": ["Mild (58-65F)", "Warm (65-72F)"],
        "Post-Spawn": ["Mild (65-70F)", "Warm (70-78F)"],
        "Summer": ["Warm (75-85F)", "Hot (85-90F+)"],
        "Fall": ["Warm (75-65F)", "Cool (65-55F)"],
        "Winter": ["Cold (45-55F)"]
    },
    "Smallmouth": {
        "Early Spring": ["Cold (40-50F)"],
        "Spawn": ["Mild (55-60F)", "Warm (60-68F)"],
        "Late Summer": ["Warm (70-75F)"],
        "Fall": ["Cool (55-65F)"]
    },
    "Bluegill": {
        "Spring": ["Cold (55-60F)", "Mild (60-68F)"],
        "Spawn": ["Mild (70-75F), Warm (75-85F)"],
        "Post-Spawn": ["Warm (80-85F)", "Hot (85-90F)"],
        "Summer": ["Warm (80-85F)", "Hot (85-90F)"],
        "Fall": ["Cool (70-75F)", "Cold (60-70F)"],
        "Winter": ["Cold (38-50F)"]
    },
    "Crappie": {
        "Pre-Spawn": ["Cold (48-51F)", "Mild (52-55F)"],
        "Spawn": ["Mild (56-65F)", "Warm (66-68F)"],
        "Post-Spawn": ["Warm (69-72F)", "Hot (73-75F)"],
        "Early Summer": ["Hot (76-78F)", "Very Hot (79-81F)"],
        "Late Summer": ["Hot (76-85F)", "Warm (66-75F)"],
        "Fall": ["Mild (66-70F)", "Cool (60-65F)"],
        "Winter": ["Cold (50-55F)", "Very Cold (38-49F)"]
    },
    "Channel Catfish": {
        "Spring": ["Moderate (60-70F)"],
        "Summer": ["Warm (75-85F)"],
        "Fall": ["Cool (65-75F)"],
        "Winter": ["Cold (40-50F)"]
    }
}

water_clarity_options = ["Select...", "Clear", "Stained", "Murky"]
weather_options = ["Select...", "Sunny", "Cloudy", "Windy", "Rainy", "After Rain"]
time_of_day_options = ["Select...", "Morning", "Afternoon", "Evening"]
waterbody_type_options = ["Select...", "Lake", "Pond", "River"]

# Load data for Largemouth, Bluegill, and Crappie
@st.cache_data
def load_largemouth_data():
    df = pd.read_csv("Data/Largemouth_AllSeasons.csv", encoding="cp1252")
    df.columns = df.columns.str.strip()
    df = df.apply(lambda col: col.str.replace("\u00a0", " ", regex=False).str.strip() if col.dtypes == "object" else col)
    return df

@st.cache_data
def load_bluegill_data():
    df = pd.read_csv("Data/Bluegill_AllSeasons.csv", encoding="cp1252")
    df.columns = df.columns.str.strip()
    df = df.apply(lambda col: col.str.replace("\u00a0", " ", regex=False).str.strip() if col.dtypes == "object" else col)
    return df

@st.cache_data
def load_crappie_data():
    df = pd.read_csv("Data/Crappie_AllSeasons.csv", encoding="cp1252")
    df.columns = df.columns.str.strip()
    df = df.apply(lambda col: col.str.replace("\u00a0", " ", regex=False).str.strip() if col.dtypes == "object" else col)
    return df

largemouth_data = load_largemouth_data()
bluegill_data = load_bluegill_data()
crappie_data = load_crappie_data()

def condition_selectors(fish, season_options_custom):
    season_key = f"{fish}_season_v2"
    temp_key = f"{fish}_temp_v2"

    season = st.selectbox("Season", season_options_custom, key=season_key)

    if season != "Select...":
        temp_options = water_temp_options_dict.get(fish, {}).get(season, ["No temp data available."])
        water_temp = st.selectbox("Water Temperature", temp_options, key=temp_key)
    else:
        st.markdown("\n_* Select a season to view temperature options\n")
        return

    clarity = st.selectbox("Water Clarity", water_clarity_options, key=f"{fish}_clarity_v2")
    weather = st.selectbox("Weather", weather_options, key=f"{fish}_weather_v2")
    time = st.selectbox("Time of Day", time_of_day_options, key=f"{fish}_time_v2")
    waterbody = st.selectbox("Waterbody Type", waterbody_type_options, key=f"{fish}_waterbody_v2")

    if st.button(f"Show {fish} Recommendations"):
        data = None
        if fish == "Largemouth":
            data = largemouth_data
        elif fish == "Bluegill":
            data = bluegill_data
        elif fish == "Crappie":
            data = crappie_data

        if data is not None:
            filtered = data[
                (data["Season"].str.strip().str.lower() == season.strip().lower()) &
                (data["Water Temp"].str.strip().str.lower() == water_temp.strip().lower()) &
                (data["Water Clarity"].str.strip().str.lower() == clarity.strip().lower()) &
                (data["Weather"].str.strip().str.lower() == weather.strip().lower()) &
                (data["Time of Day"].str.strip().str.lower() == time.strip().lower()) &
                (data["Waterbody Type"].str.strip().str.lower() == waterbody.strip().lower())
            ]

            if not filtered.empty:
                for _, row in filtered.iterrows():
                    st.subheader("🎣 Recommended Setup")
                    st.markdown(f"**Best Baits:** {row['Best Baits (Retrieve Styles)']}")
                    st.markdown(f"**Colors:** {row['Recommended Bait Colors']}")
                    st.markdown(f"**Where to Fish:** {row['Where to Fish']}")
                    st.markdown(f"**Target Depth:** {row['Target Depth']}")
            else:
                st.warning("No exact match found. Try adjusting one of the conditions.")
        else:
            st.info("Recommendations not yet available for this fish and season.")

# Add main tabs for each fish and the new Cheat Sheets tab
for tab, fish in zip(tabs[:-1], fish_names):
    with tab:
        st.header(f"Select Conditions for {fish}")
        condition_selectors(fish, season_options_dict[fish])

# Add Cheat Sheets Tab Logic
with tabs[-1]:
    st.header("Cheat Sheet Lookup")
    selected_fish = st.selectbox("Select Fish", ["Select..."] + fish_names, key="cheat_fish")
    if selected_fish != "Select...":
        selected_season = st.selectbox("Select Season", season_options_dict[selected_fish], key="cheat_season")
        if selected_season != "Select...":
            info = cheat_data.get(selected_fish, {}).get(selected_season)
            if info:
                st.markdown(f"**Water Temperature Range:** {info['temp_range']}")
                st.markdown(f"**Dates:** {info['dates']}")
                st.markdown(f"**Behavior:** {info['behavior']}")
                st.markdown("**Recommended Tactics:**")
                st.table(pd.DataFrame(info["table"]))
                st.markdown(f"**Target Depth:** {info['target_depth']}")
            else:
                st.info("Cheat sheet not available yet for this selection.")


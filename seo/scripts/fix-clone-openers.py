#!/usr/bin/env python3
"""
Fix clone:first5_words_x3 and x4 groups by varying openers.
For each x4 group: change 2 rows; for each x3 group: change 1 row.
Target: 220-250 chars, 2 sentences, TGG in S2.
"""
import csv, sys

BASE_URL = "https://www.thegoodguys.com.au/"

# 28 full rewrites keyed by URL slug
REWRITES = {
    # x4: "Start your day smoothly with" — change rows 3 & 4
    "smeg/small-kitchen-appliances/toasters-and-kettles/2-slice-toasters":
        "Get crisp golden toast with Smeg 2-Slice Toasters from The Good Guys, offering precise browning control, wide slots and consistent toasting. "
        "Add retro style, multiple browning settings and easy cleaning to your kitchen benchtop.",

    "delonghi/small-kitchen-appliances/toasters-and-kettles/toaster-and-kettle-packs":
        "Match your morning routine with DeLonghi toaster and kettle packs from The Good Guys, combining consistent toasting, rapid boiling and coordinated style. "
        "Save time with matched sets offering adjustable browning and 2200W kettles.",

    # x4: "Power through study, work, and" — change rows 3 & 4
    "acer/computers-tablets-and-gaming":
        "Choose Acer computers and tablets for study, work and play, delivering fast processors, vivid displays and ample storage for home and campus. "
        "Discover laptops and gaming monitors at The Good Guys that balance performance and portability.",

    "msi/computers-tablets-and-gaming/desktop-and-laptop/latest-pcs":
        "Run demanding apps and games with MSI laptops and desktop PCs from The Good Guys, combining fast processors, generous storage and sharp displays. "
        "Stay productive on the go with slim designs, long battery life and graphics performance.",

    # x4: "Protect your clothing with Solt" — change rows 3 & 4
    "solt/laundry/washing-machines/front-load-washing-machines":
        "Care for garments with Solt front load washing machines from The Good Guys, offering efficient cycles, gentle drum care, and water-saving performance. "
        "Save time with smart wash programs and capacities suited to everyday household laundry.",

    "solt/laundry/washing-machines/small-washing-machines":
        "Handle laundry gently with Solt small washing machines delivering compact sizing, gentle drum care and efficient spin speeds. "
        "Explore space-saving front and top load options at The Good Guys for quick cycles and tailored capacities.",

    # x4: "Protect your kitchen air with" — change rows 3 & 4
    "miele/cooking-and-dishwashers/rangehoods/canopy-rangehoods":
        "Extract steam and odours with Miele canopy rangehoods delivering powerful extraction, quiet operation and precise airflow control. "
        "Discover wall-mounted and island designs at The Good Guys to manage steam, smoke and cooking odours.",

    "unilux/cooking-and-dishwashers":
        "Refresh your kitchen air with Unilux cooking and dishwasher filters that help capture grease and odours for a fresher space. "
        "Find active carbon and rangehood filters at The Good Guys to support efficient ventilation and air quality.",

    # x4: "Stay in control of every" — change rows 3 & 4
    "artusi/cooking-and-dishwashers/cooktops":
        "Master heat for every meal with ARTUSI cooktops from The Good Guys, offering precise gas heat, flexible burner layouts, and sleek black glass finishes. "
        "Save time with responsive controls and sizes to suit compact benches or wide cooking spaces.",

    "samsung/cooking-and-dishwashers/cooktops":
        "Cook efficiently at every level with Samsung cooktops from The Good Guys, offering fast induction heating, accurate temperature settings, and easy-clean glass surfaces. "
        "Save time with smart zone layouts and flexible sizes to match.",

    # x4: "Clear the air in your" — change rows 3 & 4
    "miele/cooking-and-dishwashers/rangehoods/undermount-rangehoods":
        "Tuck extraction neatly in your kitchen with Miele undermount rangehoods from The Good Guys, designed for discreet installation, powerful extraction and quieter operation. "
        "Reduce smoke, steam and odours with efficient 70cm and 90cm options.",

    "solt/cooking-and-dishwashers/rangehoods/fixed-rangehoods":
        "Draw out smoke from your kitchen with Solt fixed rangehoods from The Good Guys, offering dependable extraction and simple controls. "
        "Reduce odours and steam with compact 60cm or wider 90cm models that integrate neatly into modern cooking spaces.",

    # x4: "Level up your play with" — change rows 3 & 4
    "nintendo/gaming/gaming-hardware":
        "Play your way with Nintendo gaming consoles and hardware delivering vivid graphics, portable versatility, and family-friendly fun. "
        "Discover Nintendo Switch systems and accessories at The Good Guys for flexible handheld and TV play.",

    "origin/gaming":
        "Expand your gaming library with Origin Gaming accessories from The Good Guys, delivering smooth access to EA titles and flexible digital passes. "
        "Save time with instant ESD codes, tiered price options and secure online delivery tailored.",

    # x3: "Save time with Fisher &" — change row 3
    "fisher-and-paykel/cooking-and-dishwashers/microwaves/built-in-microwaves":
        "Cook efficiently with Fisher & Paykel built-in microwaves offering combination cooking, compact designs and integrated styling. "
        "Discover precision heating, steam options and multiple capacities at The Good Guys for efficient meals.",

    # x3: "Stay comfortable in a fresher" — change row 3
    "bosch/cooking-and-dishwashers/rangehoods":
        "Breathe easier in a cleaner kitchen with Bosch rangehoods offering strong extraction, quieter operation, and efficient lighting. "
        "Explore canopy, slideout, undermount and downdraft options at The Good Guys to match your cooktop size.",

    # x3: "Stay comfortable in the kitchen" — change row 3
    "laura-ashley/small-kitchen-appliances/toasters-and-kettles":
        "Add a touch of pattern with Laura Ashley toasters and kettles offering fast boiling, multiple browning settings, and generous capacity. "
        "Discover patterned 2 and 4 slice toasters and 1.7L electric kettles at The Good Guys.",

    # x3: "Stay connected on the go" — change row 3
    "sonos/audio/portable-audio/portable-bluetooth-speakers":
        "Enjoy rich sound anywhere with Sonos Portable Bluetooth Speakers from The Good Guys, offering powerful sound, Wi-Fi and Bluetooth streaming, and long-lasting battery life. "
        "Choose compact, durable designs ideal for indoor and outdoor listening.",

    # x3: "Upgrade meal prep with Franke" — change row 3
    "franke/cooking-and-dishwashers/sinks-and-taps":
        "Elevate your kitchen with Franke sinks and taps from The Good Guys, combining durable stainless steel, generous bowl capacity and precise mixer control. "
        "Streamline washing, rinsing and draining with smart layouts and pull-out tap options.",

    # x3: "Save time with Russell Hobbs" — change row 3
    "russell-hobbs/small-kitchen-appliances/mixers-and-food-processors":
        "Speed through prep with Russell Hobbs mixers and food processors featuring sharp blades, variable speeds and simple controls for everyday use. "
        "Discover compact blenders and choppers at The Good Guys for fast smoothies and kitchen tasks.",

    # x3: "Upgrade movie nights with Hisense" — change row 3
    "hisense/televisions/all-tvs/tvs-75-inch-to-84-inch":
        "Fill the room with Hisense 75 Inch to 84 Inch TVs from The Good Guys, delivering cinematic 4K Ultra HD detail, Mini LED and QLED panels, plus smart streaming. "
        "Stay immersed with large-screen clarity, smooth motion and efficient energy ratings.",

    # x3: "Protect your tech on the" — change row 3
    "generation-earth/computers-tablets-and-gaming/software-and-accessories":
        "Carry your laptop safely with Generation Earth computer software and accessories that combine device safety, recycled materials and smart organisation. "
        "Discover eco-conscious laptop sleeves and briefcases at The Good Guys.",

    # x3: "Protect your cleaning performance with" — change row 3
    "bosch/vacuums-and-cleaners/vacuum-and-cleaning-accessories":
        "Maintain peak vacuum performance with Bosch vacuum and cleaning accessories from The Good Guys, designed for strong suction and efficient dust capture. "
        "Save time with durable dust bags and rapid battery chargers that help keep equipment running.",

    # x3: "Upgrade your kitchen with Oliveri" — change row 3
    "oliveri/cooking-and-dishwashers/sinks-and-taps/double-bowl-kitchen-sinks":
        "Maximise kitchen space with Oliveri Double Bowl Sinks from The Good Guys, offering generous capacity, durable finishes and undermount or inset installation. "
        "Streamline food prep with two-bowl layouts and flexible basin configurations.",

    # x3: "Protect your phone with ZAGG" — change row 3
    "zagg/phones-and-wearables":
        "Guard every screen with ZAGG cases and screen protectors delivering impact resistance, scratch defence, and camera-friendly clarity. "
        "Explore options at The Good Guys for iPhone and Samsung devices with MagSafe-ready designs.",

    # x3: "Stay immersed in your music" — change row 3
    "panasonic/audio/headphones":
        "Tune out the world with Panasonic headphones that offer clear audio, wireless freedom, and smart noise cancelling. "
        "Explore in-ear and over-ear Panasonic options at The Good Guys for comfortable listening on commutes, workouts, and daily use.",

    # x3: "Protect your phone with Panzer" — change row 3
    "panzer-glass/phones-and-wearables/phone-accessories":
        "Guard your device with Panzer Glass mobile accessories from The Good Guys, combining tough screen protection and lens covers with slim cases. "
        "Reduce scratches, cracks and glare while keeping touch response and camera clarity.",

    # x3: "Stay immersed in vivid detail" — change row 3
    "tcl/televisions/all-tvs/tvs-45-inch-to-54-inch":
        "Watch every scene clearly with TCL 45\u201354 inch TVs from The Good Guys, offering sharp 4K Ultra HD resolution and smart Google TV. "
        "Upgrade movie nights with QLED and Mini LED options for bright images, smooth motion and vivid colour.",
}


def validate():
    errors = []
    for slug, copy in REWRITES.items():
        n = len(copy)
        if n < 220 or n > 250:
            errors.append((n, slug))
    return errors


def fix_csv(input_path, output_path):
    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    fixed = 0
    for row in rows:
        slug = row['url'].replace(BASE_URL, '').rstrip('/')
        if slug in REWRITES:
            new_copy = REWRITES[slug]
            row['copy'] = new_copy
            row['chars'] = str(len(new_copy))
            if 'Flag' in row:
                row['Flag'] = 'fixed:2026-03-19'
            fixed += 1

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return fixed


print("Validating 28 clone opener rewrites (target 220-250 chars)...")
errors = validate()

if errors:
    print(f"\n{len(errors)} CHAR RANGE ERRORS:")
    for n, slug in sorted(errors):
        direction = "SHORT" if n < 220 else "LONG"
        copy = REWRITES[slug]
        print(f"  {direction} ({n}): {slug}")
        print(f"    {copy[:90]}...")
    sys.exit(1)

print(f"All {len(REWRITES)} rewrites OK. Applying to CSVs...")

merged_path = "/home/user/Claude/seo/outputs/plp-all-batches-2026-03-19.csv"
candidates_path = "/home/user/Claude/seo/outputs/plp-fix-candidates-2026-03-19.csv"

n1 = fix_csv(merged_path, merged_path)
n2 = fix_csv(candidates_path, candidates_path)

print(f"Fixed {n1} rows in all-batches CSV")
print(f"Fixed {n2} rows in fix-candidates CSV")
print("Done.")

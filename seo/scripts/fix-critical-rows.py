#!/usr/bin/env python3
"""
Fix the 47 critical-flag rows in both PLP CSVs.
Flags addressed: clone:first5_words_x5+, missing:TGG, opener:ban, brand_ban, structure:single_sentence
Target: 220-250 chars, 2 sentences, TGG in S2, named tech in S1.
"""
import csv, sys

BASE_URL = "https://www.thegoodguys.com.au/"

# New copy keyed by URL slug. All must be 220-250 chars.
REWRITES = {
    "hisense/fridges-and-freezers/refrigerators":
        "Hisense refrigerators use multi-airflow cooling and MyZone temperature drawers across French door, top mount and bar fridge formats up to 620L capacity. "
        "Shop Hisense at The Good Guys for water dispensers, LED interiors and slim French door designs.",

    "samsung/fridges-and-freezers/refrigerators":
        "Samsung refrigerators apply Twin Cooling Plus dual evaporators and SpaceMax insulation across French door, bottom mount and top mount formats. "
        "Choose Samsung at The Good Guys for Family Hub touchscreens, All-Around Cooling and water dispensers.",

    "fisher-and-paykel/fridges-and-freezers/refrigerators":
        "Fisher & Paykel refrigerators use ActiveSmart Foodcare to adapt airflow and temperature to usage patterns across French door, bottom mount and quad door formats. "
        "Find F&P at The Good Guys from 390L to 690L with SpacePlus ice-on-door options.",

    "lg/fridges-and-freezers":
        "LG fridges and freezers use Linear Compressor technology and InstaView Door-in-Door panels across French door, side-by-side, bottom mount and top mount formats. "
        "Find LG at The Good Guys with HygieneFRESH+ filtration and ThinQ smart monitoring.",

    "hisense/fridges-and-freezers/freezers":
        "Hisense freezers deliver multi-airflow temperature control and fast-freeze functions in chest and upright formats across 100L to 400L capacity. "
        "Shop Hisense freezers at The Good Guys for frost-free energy-efficient models with adjustable baskets.",

    "chiq/fridges-and-freezers/refrigerators":
        "CHiQ refrigerators use frost-free multi-airflow cooling and adjustable glass shelving across French door, bottom mount, top mount and bar formats to 520L. "
        "Find the CHiQ fridge range at The Good Guys in stainless steel and white finishes.",

    "haier/fridges-and-freezers/refrigerators/bottom-mount-fridges":
        "Haier bottom mount fridges use Total No Frost and MultiAirFlow circulation across 350L to 490L capacities with bottom-drawer freezer compartments. "
        "Shop the Haier bottom mount range at The Good Guys in single and twin drawer configurations.",

    "fisher-and-paykel/fridges-and-freezers":
        "Fisher & Paykel fridges and freezers apply ActiveSmart Foodcare intelligence across French door, bottom mount, top mount and column formats. "
        "Shop the F&P range at The Good Guys for freestanding, integrated and ice dispenser models.",

    "lg/fridges-and-freezers/refrigerators/french-door-fridges":
        "LG French door fridges combine InstaView knock-twice panels and Door-in-Door storage with Linear Compressor technology across 600L to 710L formats. "
        "Choose LG at The Good Guys for French door models with ThinQ app control and HygieneFRESH+ filtration.",

    "westinghouse/fridges-and-freezers/refrigerators/french-door-fridges":
        "Westinghouse French door fridges use FreshSeal humidity-controlled crispers and wide dual-door access across 490L to 630L with bottom-mount freezer drawers. "
        "Discover Westinghouse at The Good Guys in ice dispenser and quad-door configurations.",

    "hisense/fridges-and-freezers/refrigerators/french-door-fridges":
        "Hisense French door fridges pair MyZone adjustable temperature drawers with multi-airflow cooling across 570L to 640L wide-format layouts. "
        "Shop Hisense at The Good Guys for French door models with water dispensers and glass crisper drawers.",

    "lg/fridges-and-freezers/refrigerators/side-by-side-fridges":
        "LG Side by Side Fridges use Door-in-Door access and Linear Compressor technology across 600L plus formats with full-height fridge and freezer columns. "
        "Choose LG at The Good Guys for Side by Side models with InstaView panels and ThinQ connectivity.",

    "lg/fridges-and-freezers/refrigerators":
        "LG refrigerators use Linear Compressor and Multi Air Flow cooling across top mount, bottom mount, French door and side-by-side formats. "
        "Find LG refrigerators at The Good Guys from 300L to 700L with InstaView and HygieneFRESH+ options.",

    "hisense/fridges-and-freezers/refrigerators/bottom-mount-fridges":
        "Hisense bottom mount fridges deliver multi-airflow cooling and LED-lit interiors across 280L to 490L capacities with reversible doors. "
        "Shop Hisense at The Good Guys for bottom mount models with glass shelves and convertible temperature zones.",

    "westinghouse/fridges-and-freezers":
        "Westinghouse fridges and freezers use FreshSeal humidity-controlled crispers across French door, bottom mount, top mount and chest freezer formats. "
        "Explore Westinghouse at The Good Guys for energy-rated frost-free models with ice dispensers.",

    "hisense/fridges-and-freezers":
        "Hisense fridges and freezers span French door, bottom mount, top mount and chest formats with multi-airflow cooling and MyZone temperature drawers. "
        "Explore Hisense at The Good Guys for water dispensers, glass crispers and slim French door designs.",

    "haier/fridges-and-freezers":
        "Haier fridges and freezers use Total No Frost and MultiAirFlow cooling across French door, bottom mount, top mount and chest freezer formats. "
        "Find Haier models at The Good Guys from 140L bar fridges to 500L French door units with ZoneFlex drawers.",

    "breville/small-kitchen-appliances/coffee-machines-and-beverages":
        "Breville coffee machines use ThermoJet and ThermoCoil heating systems across Barista Express, Oracle Touch and Bambino Plus formats. "
        "Discover Breville coffee machines at The Good Guys from entry-level pump models to dual-boiler automatics.",

    "bosch/cooking-and-dishwashers/cooktops/induction-cooktops":
        "Bosch induction cooktops use FlexInduction zones and PerfectFry temperature sensor technology across 60cm and 90cm ceramic glass surfaces. "
        "Find Bosch induction cooktops at The Good Guys in 4, 5 and 6-zone formats with PowerBoost and ChildLock.",

    "eufy/smart-home/home-security/baby-monitors":
        "eufy baby monitors use 2K resolution and AI-powered cry detection with colour night vision and two-way audio across SpaceView and Babycare series models. "
        "Find eufy baby monitors at The Good Guys with Wi-Fi, pan-and-tilt cameras and real-time alerts.",

    "rinnai/heating-and-cooling/air-conditioners/portable-air-conditioners":
        "Rinnai portable air conditioners deliver single-hose and dual-hose spot cooling across 2.0kW to 4.6kW capacities with programmable timers. "
        "Find Rinnai portable air conditioner models at The Good Guys in compact and high-capacity configurations.",

    "nespresso/small-kitchen-appliances/coffee-machines-and-beverages/capsule-coffee-machines":
        "Nespresso capsule coffee machines use 19-bar extraction and Centrifusion technology in Vertuo models to brew Espresso, Gran Lungo, Mug and Carafe sizes. "
        "Find Nespresso at The Good Guys for Original and Vertuo machines including the Lattissima.",

    "tcl/fridges-and-freezers":
        "TCL fridges span French door, bottom mount and top mount formats with frost-free multi-airflow cooling and LED interiors across 100L to 550L. "
        "Discover the TCL fridge range at The Good Guys from compact bar models to 550L French door configurations.",

    "bosch/fridges-and-freezers":
        "Bosch fridges and freezers use VitaFresh technology and FreshSense sensors to maintain optimal humidity and temperature across multiple formats. "
        "Shop Bosch at The Good Guys for models with NoFrost, SuperCooling and inverter compressors.",

    "bissell/vacuums-and-cleaners/vacuum-and-cleaning-accessories":
        "BISSELL vacuum accessories include CrossWave formula solutions, Deep Clean Pro detergents and replacement brush rolls for BISSELL vacuums and cleaners. "
        "Find BISSELL accessories at The Good Guys for brushes, filters, tanks and cleaning formulas.",

    "eufy/smart-home/home-security":
        "eufy home security cameras use 2K to 4K resolution with AI human detection, colour night vision and local storage across indoor, outdoor and doorbell formats. "
        "Find eufy security cameras and smart locks at The Good Guys for wire-free and PoE setups.",

    "samsung/televisions/all-tvs/tvs-85-inch-and-above":
        "Samsung 85 Inch and Above TVs use Neo QLED Quantum Matrix technology and Neural Quantum Processor 4K with Vision AI upscaling across 85, 90 and 98-inch screens. "
        "Find Samsung large-format TVs at The Good Guys in Neo QLED, OLED and Crystal UHD series.",

    "breville/heating-and-cooling":
        "Breville heating and cooling products span air purifiers with HEPA filtration, dehumidifiers with Laundry Mode and humidifiers with auto humidity sensing. "
        "Find Breville air treatment at The Good Guys for purifiers, humidifiers and dehumidifiers.",

    "westinghouse/heating-and-cooling/air-conditioners/split-system-air-conditioners":
        "Westinghouse split system air conditioners use inverter compressor technology for reverse-cycle heating and cooling across 2.5kW to 9.0kW formats. "
        "Find Westinghouse at The Good Guys for models with Wi-Fi control and auto-restart functions.",

    "tcl/fridges-and-freezers/refrigerators":
        "TCL refrigerators deliver frost-free multi-airflow cooling across 300L to 550L with adjustable glass shelving, LED interiors and reversible doors. "
        "Choose TCL at The Good Guys for top mount, bottom mount and French door models with water dispensers.",

    "solt/fridges-and-freezers/refrigerators/top-mount-fridges":
        "Solt top mount fridges deliver frost-free performance and adjustable glass shelving across 280L to 450L capacities for everyday household cooling. "
        "Choose Solt at The Good Guys for top mount models with LED interiors and reversible doors.",

    "sony/televisions/all-tvs/tvs-85-inch-and-above":
        "Sony 85 Inch and Above TVs pair the Cognitive Processor XR with XR Triluminos Pro colour across Mini LED, OLED and 4K HDR screens from 85 to 98 inches. "
        "Find Sony BRAVIA 7, 8 and 9 series TVs at The Good Guys with Acoustic Multi-Audio and Google TV.",

    "microsoft/computers-tablets-and-gaming/desktop-and-laptop/microsoft-surface":
        "Microsoft Surface laptops use Snapdragon X Elite and Intel Core Ultra processors with Copilot+ AI features and PixelSense touchscreens in convertible formats. "
        "Find Microsoft Surface at The Good Guys for Surface Pro, Surface Laptop and Surface Go.",

    "belkin/phones-and-wearables/phone-accessories":
        "Belkin phone accessories combine GaN fast-charge adapters, BoostCharge Pro magnetic wireless pads and Kevlar-reinforced cables across MagSafe and USB-C formats. "
        "Shop Belkin at The Good Guys for chargers, cables, mounts and screen protectors.",

    "mophie/phones-and-wearables/phone-accessories/phone-chargers-and-accessories":
        "Mophie phone chargers use GaN technology for compact fast charging alongside Powerstation wireless power banks, braided USB-C cables and MagSafe wireless pads. "
        "Find Mophie at The Good Guys for wall, car and multi-port chargers and power banks.",

    "kindle/computers-tablets-and-gaming":
        "Kindle e-readers combine E Ink Paperwhite displays with adjustable warm light and weeks-long battery life across the Kindle, Paperwhite and Scribe lines. "
        "Shop the Kindle range at The Good Guys for waterproof Paperwhite and Scribe eReaders.",

    "sunbeam/heating-and-cooling":
        "Sunbeam heating and cooling products span electric blankets with nine heat settings, heated throws with auto-shutoff and ceramic tower heaters with PTC elements. "
        "Find Sunbeam at The Good Guys for bedroom, living room and personal comfort models.",

    "cygnett/phones-and-wearables/phone-accessories":
        "Cygnett phone accessories use GaN technology in compact fast-charge adapters alongside ArmourShield screen protectors, MagSafe wireless chargers and car mounts. "
        "Shop Cygnett at The Good Guys for cables, chargers, cases and mounts.",

    "milo/phones-and-wearables":
        "Milo Phones & Wearables cover the Milo Action Communicator, action clips, helmet mounts and carry accessories for group communication outdoors. "
        "Find the Milo range at The Good Guys for communicators and accessories for cyclists, skiers and hikers.",

    "sandisk/computers-tablets-and-gaming":
        "SanDisk storage products span USB flash drives, UHS-I and UHS-II microSD and SD cards and portable SSD drives in capacities from 32GB to 4TB. "
        "Find SanDisk at The Good Guys for camera SD cards, dashcam storage and high-speed portable SSDs.",

    "oliveri/cooking-and-dishwashers/sinks-and-taps/pullout-pulldown-taps":
        "Oliveri pullout and pulldown taps use precision ceramic cartridge valves and flexible braided hose with spray and stream modes in chrome and matte black finishes. "
        "Find Oliveri taps at The Good Guys to pair with Santorini and Regatta sink bowls.",

    "incase/computers-tablets-and-gaming":
        "Incase MacBook cases use CL90052-compliant hardshell construction and Woolenex fabric for drop protection across 13-inch to 16-inch MacBook Air and Pro models. "
        "Find Incase at The Good Guys for laptop sleeves, hardshell cases and carry accessories.",

    "norton/computers-tablets-and-gaming":
        "Norton security software uses real-time threat protection, a secure VPN and Dark Web monitoring across PC, Mac, iOS and Android on single and family plans. "
        "Find Norton at The Good Guys for AntiVirus Plus, 360 Standard and 360 Deluxe plans.",

    "tcl/fridges-and-freezers/refrigerators/bottom-mount-fridges":
        "TCL bottom mount fridges use frost-free multi-airflow cooling and LED-lit interiors with bottom-drawer freezer compartments across 300L to 490L capacities. "
        "Shop the TCL bottom mount range at The Good Guys for adjustable shelving and reversible doors.",

    "mophie/phones-and-wearables":
        "Mophie phones and wearables span Juice Pack battery cases, Powerstation wireless power banks and MagSafe charging pads that keep devices charged all day. "
        "Find the full Mophie range at The Good Guys from GaN fast-charge adapters to car chargers.",

    "baileys/small-kitchen-appliances":
        "Baileys small kitchen appliances pair capsule coffee systems with kettles and toasters using signature Irish Cream flavour profiles for home entertaining. "
        "Shop the Baileys range at The Good Guys for capsule machines, kettles and toasters.",

    "mophie/phones-and-wearables/phone-accessories":
        "Mophie phone accessories combine Juice Pack battery cases with Powerstation wireless power banks and MagSafe charging pads for all-day device charge. "
        "Shop Mophie at The Good Guys for fast-charge cables, car chargers and charging stations.",
}


def validate():
    errors = []
    for slug, copy in REWRITES.items():
        n = len(copy)
        if n < 220 or n > 250:
            errors.append((n, slug, copy))
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


print("Validating rewrites (target 220-250 chars)...")
errors = validate()

if errors:
    print(f"\n{len(errors)} CHAR RANGE ERRORS:")
    for n, slug, copy in sorted(errors):
        direction = "SHORT" if n < 220 else "LONG"
        print(f"  {direction} ({n}): {slug}")
        print(f"    {copy[:80]}...")
    sys.exit(1)

print(f"All {len(REWRITES)} rewrites OK. Applying to CSVs...")

candidates_path = "/home/user/Claude/seo/outputs/plp-fix-candidates-2026-03-19.csv"
merged_path = "/home/user/Claude/seo/outputs/plp-all-batches-2026-03-19.csv"

n1 = fix_csv(candidates_path, candidates_path)
n2 = fix_csv(merged_path, merged_path)

print(f"Fixed {n1} rows in fix-candidates CSV")
print(f"Fixed {n2} rows in all-batches CSV")
print("Done.")

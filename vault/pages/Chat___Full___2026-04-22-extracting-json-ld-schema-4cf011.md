---
title: Extracting JSON-LD schema (full)
parent: Chat/Light/2026-04-22-extracting-json-ld-schema-4cf011
uuid: 4cf0112c-85fd-4d9a-bae2-a46705dc47b5
---

#chat/full #project/main #status/completed

# Extracting JSON-LD schema — Full Transcript

→ Light view: [[Chat/Light/2026-04-22-extracting-json-ld-schema-4cf011]]
→ Medium view: [[Chat/Medium/2026-04-22-extracting-json-ld-schema-4cf011]]

**Messages:** 4 | **Date:** 2026-04-22

---

### 1. **Human** — 2026-04-22T03:45

get me only the schema (json LD) bits from here
get me only the schema (json LD) bits from here

---

### 2. **Claude** — 2026-04-22T03:46

Let me read the file first.
```
This block is not supported on your current device yet.
```

Let me try a different approach.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Got 3 blocks. Let me present them cleanly.3 blocks found.

**Block 1 — CollectionPage**
```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "url": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums",
  "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#collectionpage",
  "name": "Stick Vacuums",
  "description": "Keep floors in top shape with lightweight stick vacuums offering strong suction, flexible handling & cordless convenience for everyday cleaning. Explore high-quality designs from Dyson, Samsung, LG & Hoover to find a premium fit for your home at The Good Guys.",
  "isPartOf": {
    "@type": "WebSite",
    "@id": "https://www.thegoodguys.com.au/#WebSite",
    "url": "https://www.thegoodguys.com.au",
    "name": "The Good Guys",
    "alternateName": "The Good Guys Discount Warehouses"
  },
  "publisher": {
    "@type": "Organization",
    "name": "The Good Guys",
    "url": "https://www.thegoodguys.com.au/",
    "@id": "https://www.thegoodguys.com.au/#organization"
  },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#BreadcrumbList"
  },
  "relatedLink": [
    "https://www.thegoodguys.com.au/vacuums-and-cleaners",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/handheld-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/wet-and-dry-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/upright-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/bagless-vacuum-cleaners",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/barrel-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/car-cleaning-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/robot-mops",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/pet-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/robot-vacuums"
  ],
  "inLanguage": "en-AU",
  "hasPart": {
    "@type": "FAQPage",
    "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#faqs"
  }
}
```

**Block 2 — FAQPage**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#faqs",
  "isPartOf": {
    "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#collectionpage"
  },
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How Do You Maintain and Care for a Cordless Vacuum?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Regular maintenance keeps your cordless vacuum performing at peak power:Empty dust container after every few uses—smaller capacity means more frequent emptyingClean washable filters monthly under cold water, dry completely for 24 hoursCheck brush roller weekly for tangled hair, use scissors to remove obstructionsInspect tubes and connections if suction drops—blockages restrict airflowStore on charging dock away from direct heat to protect batteryFind replacement vacuum cleaner bags and filters when parts wear out. Bring your vacuum in store if you need troubleshooting help."
      }
    },
    {
      "@type": "Question",
      "name": "How Powerful Are Stick Vacuums? Performance on Different Surfaces",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stick vacuum power is measured in Air Watts (AW) or kilopascals (kPa) rather than standard wattage. Higher AW or kPa numbers mean stronger suction—premium models reach 200+ AW compared to 100-150 AW in budget options. Standard wattage measures electricity consumption, not cleaning performance. Cordless vacuums excel on hard floors and low-pile carpets but may struggle with thick, plush carpeting compared to upright vacuums. Rotating brushes enhance carpet cleaning but should be switched off on hardwood to avoid scratches. Newer lithium-ion batteries maintain consistent power throughout the charge cycle. Our team can demonstrate performance differences in store."
      }
    },
    {
      "@type": "Question",
      "name": "What Features to Look for in a Stick Vacuum?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Choosing the right cordless vacuum depends on your cleaning priorities:Weight under 2.5kg reduces arm fatigue for overhead cleaningSwivel steering improves manoeuvrability around furnitureMultiple power modes balance suction strength with battery lifeDigital displays show run time and maintenance alertsExtension wands andattachments expand cleaning reachEdge-cleaning brushes sweep debris from skirting boardsVisit us in store to compare models and find what works within your budget."
      }
    }
  ]
}
```

**Block 3 — BreadcrumbList**
```json
{
  "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#BreadcrumbList",
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@id": "/",
        "@type": "WebPage",
        "name": "Home"
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@id": "/vacuums-and-cleaners",
        "@type": "WebPage",
        "name": "Vacuums & Cleaners"
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@id": "/vacuums-and-cleaners/vacuum-cleaners",
        "@type": "WebPage",
        "name": "Vacuum Cleaners"
      }
    },
    {
      "@type": "ListItem",
      "position": 4,
      "item": {
        "@id": "/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums",
        "@type": "WebPage",
        "name": "Stick Vacuums"
      }
    }
  ]
}
```

One flag worth noting: the FAQ `text` values have no line breaks between list items (e.g. "...frequent emptyingClean washable..."). The HTML likely used `<ul>`/`<li>` tags that didn't get serialised as newlines in the schema output. Worth fixing in the source if this schema is being submitted for rich result eligibility.
 
3 blocks found.

**Block 1 — CollectionPage**
```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "url": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums",
  "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#collectionpage",
  "name": "Stick Vacuums",
  "description": "Keep floors in top shape with lightweight stick vacuums offering strong suction, flexible handling & cordless convenience for everyday cleaning. Explore high-quality designs from Dyson, Samsung, LG & Hoover to find a premium fit for your home at The Good Guys.",
  "isPartOf": {
    "@type": "WebSite",
    "@id": "https://www.thegoodguys.com.au/#WebSite",
    "url": "https://www.thegoodguys.com.au",
    "name": "The Good Guys",
    "alternateName": "The Good Guys Discount Warehouses"
  },
  "publisher": {
    "@type": "Organization",
    "name": "The Good Guys",
    "url": "https://www.thegoodguys.com.au/",
    "@id": "https://www.thegoodguys.com.au/#organization"
  },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#BreadcrumbList"
  },
  "relatedLink": [
    "https://www.thegoodguys.com.au/vacuums-and-cleaners",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/handheld-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/wet-and-dry-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/upright-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/bagless-vacuum-cleaners",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/barrel-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/car-cleaning-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/robot-mops",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/pet-vacuums",
    "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/robot-vacuums"
  ],
  "inLanguage": "en-AU",
  "hasPart": {
    "@type": "FAQPage",
    "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#faqs"
  }
}
```

**Block 2 — FAQPage**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#faqs",
  "isPartOf": {
    "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#collectionpage"
  },
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How Do You Maintain and Care for a Cordless Vacuum?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Regular maintenance keeps your cordless vacuum performing at peak power:Empty dust container after every few uses—smaller capacity means more frequent emptyingClean washable filters monthly under cold water, dry completely for 24 hoursCheck brush roller weekly for tangled hair, use scissors to remove obstructionsInspect tubes and connections if suction drops—blockages restrict airflowStore on charging dock away from direct heat to protect batteryFind replacement vacuum cleaner bags and filters when parts wear out. Bring your vacuum in store if you need troubleshooting help."
      }
    },
    {
      "@type": "Question",
      "name": "How Powerful Are Stick Vacuums? Performance on Different Surfaces",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stick vacuum power is measured in Air Watts (AW) or kilopascals (kPa) rather than standard wattage. Higher AW or kPa numbers mean stronger suction—premium models reach 200+ AW compared to 100-150 AW in budget options. Standard wattage measures electricity consumption, not cleaning performance. Cordless vacuums excel on hard floors and low-pile carpets but may struggle with thick, plush carpeting compared to upright vacuums. Rotating brushes enhance carpet cleaning but should be switched off on hardwood to avoid scratches. Newer lithium-ion batteries maintain consistent power throughout the charge cycle. Our team can demonstrate performance differences in store."
      }
    },
    {
      "@type": "Question",
      "name": "What Features to Look for in a Stick Vacuum?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Choosing the right cordless vacuum depends on your cleaning priorities:Weight under 2.5kg reduces arm fatigue for overhead cleaningSwivel steering improves manoeuvrability around furnitureMultiple power modes balance suction strength with battery lifeDigital displays show run time and maintenance alertsExtension wands andattachments expand cleaning reachEdge-cleaning brushes sweep debris from skirting boardsVisit us in store to compare models and find what works within your budget."
      }
    }
  ]
}
```

**Block 3 — BreadcrumbList**
```json
{
  "@id": "https://www.thegoodguys.com.au/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums#BreadcrumbList",
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@id": "/",
        "@type": "WebPage",
        "name": "Home"
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@id": "/vacuums-and-cleaners",
        "@type": "WebPage",
        "name": "Vacuums & Cleaners"
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@id": "/vacuums-and-cleaners/vacuum-cleaners",
        "@type": "WebPage",
        "name": "Vacuum Cleaners"
      }
    },
    {
      "@type": "ListItem",
      "position": 4,
      "item": {
        "@id": "/vacuums-and-cleaners/vacuum-cleaners/stick-vacuums",
        "@type": "WebPage",
        "name": "Stick Vacuums"
      }
    }
  ]
}
```

One flag worth noting: the FAQ `text` values have no line breaks between list items (e.g. "...frequent emptyingClean washable..."). The HTML likely used `<ul>`/`<li>` tags that didn't get serialised as newlines in the schema output. Worth fixing in the source if this schema is being submitted for rich result eligibility.

---

### 3. **Human** — 2026-04-22T03:49

sorry, wrong file version, here - i only want prooduct
sorry, wrong file version, here - i only want prooduct

---

### 4. **Claude** — 2026-04-22T03:50

Let me read the file and extract JSON-LD blocks, filtering for product schema only.
```
This block is not supported on your current device yet.
```

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Dyson V8 Cyclone Cordless Vacuum",
  "description": "150 Air Watts of fade-free suction(3)15 cyclones increase airflow and capture fine dust consistently. Working with the updated digital motor for 30% more fade-free suction(1). Up to 60 minutes run time(2) Advanced seven-cell, lithium-ion battery delivers fade-free suction. Delivering 50% more dust removal on a single charge(4). Power modes for every clean, Triggerless power with 3 adjustable modes tro choose from: Eco, Medium, MAX. Root Cyclone(TM)) separation system. Dyson's patented 15 cyclones capture and separate dust and debris, so there's no loss of suction. Captures 99.99% microscopic particles. Fully sealed , whole-machine filtration captures dust, particles and allergens to 0.3microns(5). Deep clean your whole home. Lightweight design transforms into a handheld to tackle debris, including pet hair. Disclaimers:(1)30% more suction compared to the existing V8 cordless vacuum cleaner (SV25). Suction tested to IEC 62885-4:2023 Sec. 5.11 and 5.12, in Boost mode at the inlet in SGS Laboratory USA in 2025 (2)Applies in Eco mode in handheld configuration. Actual run time will vary based on power mode, floor type and/or attachments used. (3) Suction tested to IEC 62885-4:2023, Sec. 5.11 and 5.12, in Boost mode at the inlet in SGS Laboratory USA in 2025 (4)50% more runtime in Eco mode compared to the original V8 (SV25) allows 50% more dirt collected. Actual performance may vary based on debris and usage.(5)Tested to ASTM1977-04 Boost mode in SGS Laboratory USA in 2025. Filtration efficiency is calculated by comparing the number of standard dust particles absorbed by the vacuum cleaner to the number of standard dust particles discharged. Capture rate may vary depending on actual usage environment and cleaning mode",
  "url": "https://www.thegoodguys.com.au/dyson-v8-cyclone-cordless-vacuum-226890-01",
  "@id": "https://www.thegoodguys.com.au/dyson-v8-cyclone-cordless-vacuum-226890-01#productpage",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.thegoodguys.com.au/dyson-v8-cyclone-cordless-vacuum-226890-01#WebPage"
  },
  "brand": {
    "@type": "Brand",
    "name": "Dyson"
  },
  "sku": "50096116",
  "image": [
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011432.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011427.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011426.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011364.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011367.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011358.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011359.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011354.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011356.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011412.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011413.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011415.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011414.png?v=1776231994"
  ],
  "gtin": "5025155122631",
  "category": "Vacuums & Cleaners/Vacuum Cleaners/Stick Vacuums",
  "height": { "@type": "QuantitativeValue", "value": 1160, "unitCode": "MMT" },
  "width": { "@type": "QuantitativeValue", "value": 240, "unitCode": "MMT" },
  "depth": { "@type": "QuantitativeValue", "value": 210, "unitCode": "MMT" },
  "weight": { "@type": "QuantitativeValue", "value": 2.7, "unitCode": "KGM" },
  "offers": {
    "@type": "Offer",
    "url": "https://www.thegoodguys.com.au/dyson-v8-cyclone-cordless-vacuum-226890-01",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "price": "495.00",
    "validFrom": "2026-03-30T00:01:00.000+11:00",
    "validThrough": "2026-04-22T23:59:59.000+10:00",
    "priceValidUntil": "2026-04-22",
    "priceCurrency": "AUD",
    "acceptedPaymentMethod": ["Cash", "Credit Card", "Debit Card", "Apple Pay", "PayPal", "Afterpay", "Latitude", "ZIP PAY"],
    "seller": {
      "@type": "Organization",
      "@id": "https://www.thegoodguys.com.au/#organization",
      "name": "The Good Guys"
    },
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "applicableCountry": "AU",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 30,
      "returnMethod": "https://schema.org/ReturnInStore",
      "returnFees": "https://schema.org/FreeReturn"
    },
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingDestination": {
        "@type": "DefinedRegion",
        "addressCountry": "AU"
      },
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "handlingTime": { "@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY" },
        "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 7, "unitCode": "DAY" }
      }
    },
    "additionalProperty": {
      "@type": "PropertyValue",
      "name": "Delivery Options",
      "value": "Standard, Express and Scheduled delivery available. For large appliances, customers can choose their delivery date during checkout."
    }
  },
  "model": "226890-01",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": 4.8,
    "bestRating": 5,
    "worstRating": 1,
    "reviewCount": 37
  },
  "review": [
    {
      "@type": "Review",
      "name": "Dyson V8 Cyclone ",
      "reviewBody": "I'm really happy with my new V8 stick vacuum—it's a big step up from my old V6. The new on/off button is much more convenient than holding down a trigger, and the updated lever system makes emptying it quick and easy. It's also slightly longer, the battery lasts noticeably longer, and overall it feels more user-friendly. Another bonus is that it's lighter than the V12 and newer models, which makes it even easier to handle.",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-04-21",
      "author": { "@type": "Person", "name": "Jody" }
    },
    {
      "@type": "Review",
      "name": "Replaced old V7 - with newer V8 Cyclone - Brilliant!",
      "reviewBody": "Had to replace the old V7 as Battery was not as long lasting (Understandable) after many years of use .. this new V8 Cyclone is Brilliant.\r\nAlso like that it has on/off button instead of trigger.. Great suction and weight/balance for everyday use.   Also lasts much longer . \r\nAlso better design to empty unlike the older V7 ..\r\nGive it a 5 out of 5 ",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-04-19",
      "author": { "@type": "Person", "name": "Vik Prasad" }
    },
    {
      "@type": "Review",
      "name": "Suction power is good",
      "reviewBody": "It comes with other two sets of head which is good to be used while cleaning the car",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-31",
      "author": { "@type": "Person", "name": "Rose" }
    },
    {
      "@type": "Review",
      "name": "Great lightweight vacuum",
      "reviewBody": "This Vacuum is very powerful and lightweight.  Great for my arthritic hands",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-31",
      "author": { "@type": "Person", "name": "John" }
    },
    {
      "@type": "Review",
      "name": "Cyclone  Dyson",
      "reviewBody": "Love it !!!",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-25",
      "author": { "@type": "Person", "name": "Barbara" }
    },
    {
      "@type": "Review",
      "name": "Dyson v8 cordless vacuum ",
      "reviewBody": "Very light to use and vacuums well",
      "reviewRating": { "@type": "Rating", "ratingValue": 4, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-24",
      "author": { "@type": "Person", "name": "NP" }
    },
    {
      "@type": "Review",
      "name": "Powerful ",
      "reviewBody": "The best thing about this product is I don't have to keep holding down a trigger for it to go. That was the problem with my other one. I just click a button and off it goes. It is one of the best cordless vacuums I've ever owned.",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-24",
      "author": { "@type": "Person", "name": "Kerrianne" }
    },
    {
      "@type": "Review",
      "name": "Can't go wrong with this one. ",
      "reviewBody": "Brought this to replace an older V8. Has better suction, longer battery life. And best upgrade is the hands free power button.  Good for a medium sized house. ",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-23",
      "author": { "@type": "Person", "name": "Brian" }
    },
    {
      "@type": "Review",
      "name": "Good and easy. ",
      "reviewBody": "When held an angle, the battery keeps pressing against the wrist. ",
      "reviewRating": { "@type": "Rating", "ratingValue": 4, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-17",
      "author": { "@type": "Person", "name": "N Raj" }
    },
    {
      "@type": "Review",
      "name": "Love the extra tools",
      "reviewBody": "Great suction power",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-17",
      "author": { "@type": "Person", "name": "Rose" }
    }
  ]
}
```

One thing worth noting: `priceValidUntil` is today (2026-04-22), so this offer expires tonight. If you're using this as a template, that field will need updating.
 
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Dyson V8 Cyclone Cordless Vacuum",
  "description": "150 Air Watts of fade-free suction(3)15 cyclones increase airflow and capture fine dust consistently. Working with the updated digital motor for 30% more fade-free suction(1). Up to 60 minutes run time(2) Advanced seven-cell, lithium-ion battery delivers fade-free suction. Delivering 50% more dust removal on a single charge(4). Power modes for every clean, Triggerless power with 3 adjustable modes tro choose from: Eco, Medium, MAX. Root Cyclone(TM)) separation system. Dyson's patented 15 cyclones capture and separate dust and debris, so there's no loss of suction. Captures 99.99% microscopic particles. Fully sealed , whole-machine filtration captures dust, particles and allergens to 0.3microns(5). Deep clean your whole home. Lightweight design transforms into a handheld to tackle debris, including pet hair. Disclaimers:(1)30% more suction compared to the existing V8 cordless vacuum cleaner (SV25). Suction tested to IEC 62885-4:2023 Sec. 5.11 and 5.12, in Boost mode at the inlet in SGS Laboratory USA in 2025 (2)Applies in Eco mode in handheld configuration. Actual run time will vary based on power mode, floor type and/or attachments used. (3) Suction tested to IEC 62885-4:2023, Sec. 5.11 and 5.12, in Boost mode at the inlet in SGS Laboratory USA in 2025 (4)50% more runtime in Eco mode compared to the original V8 (SV25) allows 50% more dirt collected. Actual performance may vary based on debris and usage.(5)Tested to ASTM1977-04 Boost mode in SGS Laboratory USA in 2025. Filtration efficiency is calculated by comparing the number of standard dust particles absorbed by the vacuum cleaner to the number of standard dust particles discharged. Capture rate may vary depending on actual usage environment and cleaning mode",
  "url": "https://www.thegoodguys.com.au/dyson-v8-cyclone-cordless-vacuum-226890-01",
  "@id": "https://www.thegoodguys.com.au/dyson-v8-cyclone-cordless-vacuum-226890-01#productpage",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.thegoodguys.com.au/dyson-v8-cyclone-cordless-vacuum-226890-01#WebPage"
  },
  "brand": {
    "@type": "Brand",
    "name": "Dyson"
  },
  "sku": "50096116",
  "image": [
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011432.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011427.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011426.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011364.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011367.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011358.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011359.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011354.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011356.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011412.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011413.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011415.png?v=1776231994",
    "https://cdn.shopify.com/s/files/1/0641/9388/8321/files/50096116_1011414.png?v=1776231994"
  ],
  "gtin": "5025155122631",
  "category": "Vacuums & Cleaners/Vacuum Cleaners/Stick Vacuums",
  "height": { "@type": "QuantitativeValue", "value": 1160, "unitCode": "MMT" },
  "width": { "@type": "QuantitativeValue", "value": 240, "unitCode": "MMT" },
  "depth": { "@type": "QuantitativeValue", "value": 210, "unitCode": "MMT" },
  "weight": { "@type": "QuantitativeValue", "value": 2.7, "unitCode": "KGM" },
  "offers": {
    "@type": "Offer",
    "url": "https://www.thegoodguys.com.au/dyson-v8-cyclone-cordless-vacuum-226890-01",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "price": "495.00",
    "validFrom": "2026-03-30T00:01:00.000+11:00",
    "validThrough": "2026-04-22T23:59:59.000+10:00",
    "priceValidUntil": "2026-04-22",
    "priceCurrency": "AUD",
    "acceptedPaymentMethod": ["Cash", "Credit Card", "Debit Card", "Apple Pay", "PayPal", "Afterpay", "Latitude", "ZIP PAY"],
    "seller": {
      "@type": "Organization",
      "@id": "https://www.thegoodguys.com.au/#organization",
      "name": "The Good Guys"
    },
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "applicableCountry": "AU",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 30,
      "returnMethod": "https://schema.org/ReturnInStore",
      "returnFees": "https://schema.org/FreeReturn"
    },
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingDestination": {
        "@type": "DefinedRegion",
        "addressCountry": "AU"
      },
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "handlingTime": { "@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY" },
        "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 7, "unitCode": "DAY" }
      }
    },
    "additionalProperty": {
      "@type": "PropertyValue",
      "name": "Delivery Options",
      "value": "Standard, Express and Scheduled delivery available. For large appliances, customers can choose their delivery date during checkout."
    }
  },
  "model": "226890-01",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": 4.8,
    "bestRating": 5,
    "worstRating": 1,
    "reviewCount": 37
  },
  "review": [
    {
      "@type": "Review",
      "name": "Dyson V8 Cyclone ",
      "reviewBody": "I'm really happy with my new V8 stick vacuum—it's a big step up from my old V6. The new on/off button is much more convenient than holding down a trigger, and the updated lever system makes emptying it quick and easy. It's also slightly longer, the battery lasts noticeably longer, and overall it feels more user-friendly. Another bonus is that it's lighter than the V12 and newer models, which makes it even easier to handle.",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-04-21",
      "author": { "@type": "Person", "name": "Jody" }
    },
    {
      "@type": "Review",
      "name": "Replaced old V7 - with newer V8 Cyclone - Brilliant!",
      "reviewBody": "Had to replace the old V7 as Battery was not as long lasting (Understandable) after many years of use .. this new V8 Cyclone is Brilliant.\r\nAlso like that it has on/off button instead of trigger.. Great suction and weight/balance for everyday use.   Also lasts much longer . \r\nAlso better design to empty unlike the older V7 ..\r\nGive it a 5 out of 5 ",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-04-19",
      "author": { "@type": "Person", "name": "Vik Prasad" }
    },
    {
      "@type": "Review",
      "name": "Suction power is good",
      "reviewBody": "It comes with other two sets of head which is good to be used while cleaning the car",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-31",
      "author": { "@type": "Person", "name": "Rose" }
    },
    {
      "@type": "Review",
      "name": "Great lightweight vacuum",
      "reviewBody": "This Vacuum is very powerful and lightweight.  Great for my arthritic hands",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-31",
      "author": { "@type": "Person", "name": "John" }
    },
    {
      "@type": "Review",
      "name": "Cyclone  Dyson",
      "reviewBody": "Love it !!!",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-25",
      "author": { "@type": "Person", "name": "Barbara" }
    },
    {
      "@type": "Review",
      "name": "Dyson v8 cordless vacuum ",
      "reviewBody": "Very light to use and vacuums well",
      "reviewRating": { "@type": "Rating", "ratingValue": 4, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-24",
      "author": { "@type": "Person", "name": "NP" }
    },
    {
      "@type": "Review",
      "name": "Powerful ",
      "reviewBody": "The best thing about this product is I don't have to keep holding down a trigger for it to go. That was the problem with my other one. I just click a button and off it goes. It is one of the best cordless vacuums I've ever owned.",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-24",
      "author": { "@type": "Person", "name": "Kerrianne" }
    },
    {
      "@type": "Review",
      "name": "Can't go wrong with this one. ",
      "reviewBody": "Brought this to replace an older V8. Has better suction, longer battery life. And best upgrade is the hands free power button.  Good for a medium sized house. ",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-23",
      "author": { "@type": "Person", "name": "Brian" }
    },
    {
      "@type": "Review",
      "name": "Good and easy. ",
      "reviewBody": "When held an angle, the battery keeps pressing against the wrist. ",
      "reviewRating": { "@type": "Rating", "ratingValue": 4, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-17",
      "author": { "@type": "Person", "name": "N Raj" }
    },
    {
      "@type": "Review",
      "name": "Love the extra tools",
      "reviewBody": "Great suction power",
      "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": "5", "worstRating": "1" },
      "datePublished": "2026-03-17",
      "author": { "@type": "Person", "name": "Rose" }
    }
  ]
}
```

One thing worth noting: `priceValidUntil` is today (2026-04-22), so this offer expires tonight. If you're using this as a template, that field will need updating.

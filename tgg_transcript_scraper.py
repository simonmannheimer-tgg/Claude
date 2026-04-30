#!/usr/bin/env python3
"""
TGG YouTube Transcript Scraper
Uses yt-dlp to extract transcripts. Video list is hardcoded from prior channel scrape.

Requirements:
    pip install yt-dlp

Usage:
    python tgg_transcript_scraper.py
"""

import json
import sys
import re
import time
import tempfile
import os
import subprocess
from pathlib import Path
from datetime import date

VIDEOS = [
  {
    "id": "BvojUieuckc",
    "title": "Welcome to Alice Zaslavsky's happy place | The Good Guys",
    "url": "https://www.youtube.com/watch?v=BvojUieuckc"
  },
  {
    "id": "Bb_TfpszDPA",
    "title": "Ready to Cook? | The Good Guys",
    "url": "https://www.youtube.com/watch?v=Bb_TfpszDPA"
  },
  {
    "id": "LgCOi2FsTE0",
    "title": "Essential Cooking Tips and Expert Advice from Alice Zaslavsky: Your Kitchen Q&A Guide",
    "url": "https://www.youtube.com/watch?v=LgCOi2FsTE0"
  },
  {
    "id": "WAnAmXdAmLg",
    "title": "Cooking Q&A with Alice | The Good Guys",
    "url": "https://www.youtube.com/watch?v=WAnAmXdAmLg"
  },
  {
    "id": "JJMDV2dwuV8",
    "title": "Thinking about induction? | The Good Guys",
    "url": "https://www.youtube.com/watch?v=JJMDV2dwuV8"
  },
  {
    "id": "h12d63fJW3g",
    "title": "Meet the iRobot Roomba\u00ae 105 Combo Robot with AutoEmpty\u2122 | The Good Guys",
    "url": "https://www.youtube.com/watch?v=h12d63fJW3g"
  },
  {
    "id": "a8h3xYsHKHc",
    "title": "Meet the Dyson V16 Piston Animal Submarine\u2122 Wet & Dry Cordless Vacuum | The Good Guys",
    "url": "https://www.youtube.com/watch?v=a8h3xYsHKHc"
  },
  {
    "id": "9atTEBfpY4I",
    "title": "Meet the Hoover ONEPWR CleanSlate Pet Cordless Spot Cleaner | The Good Guys",
    "url": "https://www.youtube.com/watch?v=9atTEBfpY4I"
  },
  {
    "id": "LJCxzgYxWZ8",
    "title": "Meet Samsung's 2025 TV Range",
    "url": "https://www.youtube.com/watch?v=LJCxzgYxWZ8"
  },
  {
    "id": "_aSVT-d9qdo",
    "title": "Meet The Breville Oracle\u00ae Dual Boiler | The Good Guys",
    "url": "https://www.youtube.com/watch?v=_aSVT-d9qdo"
  },
  {
    "id": "k082NJjJWlI",
    "title": "Meet The Dyson V16 Piston Animal Cordless Vacuum",
    "url": "https://www.youtube.com/watch?v=k082NJjJWlI"
  },
  {
    "id": "HA_zohASg2Q",
    "title": "Step into the future with LG entertainment | The Good Guys",
    "url": "https://www.youtube.com/watch?v=HA_zohASg2Q"
  },
  {
    "id": "dbeX5H5cNu8",
    "title": "Meet LG's 2025 TV Range | The Good Guys",
    "url": "https://www.youtube.com/watch?v=dbeX5H5cNu8"
  },
  {
    "id": "7s0tC3P4x8M",
    "title": "Features of LG's 2025 TV Range | The Good Guys",
    "url": "https://www.youtube.com/watch?v=7s0tC3P4x8M"
  },
  {
    "id": "nG6Gs0sZfMY",
    "title": "Get ready for Black Friday at The Good Guys!",
    "url": "https://www.youtube.com/watch?v=nG6Gs0sZfMY"
  },
  {
    "id": "yrBe8S_kJfw",
    "title": "Poh's Here To Introduce LG Cooking | The Good Guys",
    "url": "https://www.youtube.com/watch?v=yrBe8S_kJfw"
  },
  {
    "id": "CKPahpACpnY",
    "title": "The Clever LG Cooking Range | The Good Guys",
    "url": "https://www.youtube.com/watch?v=CKPahpACpnY"
  },
  {
    "id": "njZJAEfUJWE",
    "title": "Listen Up Bakers! | The Good Guys",
    "url": "https://www.youtube.com/watch?v=njZJAEfUJWE"
  },
  {
    "id": "Y_sLi5Z6zlA",
    "title": "Get Inspired With The LG Cooking Range | The Good Guys",
    "url": "https://www.youtube.com/watch?v=Y_sLi5Z6zlA"
  },
  {
    "id": "_ZIWuFJCxas",
    "title": "Create Your Dream Kitchen | The Good Guys",
    "url": "https://www.youtube.com/watch?v=_ZIWuFJCxas"
  },
  {
    "id": "m_2eRVz8nbM",
    "title": "Kitchen Secrets With Poh | The Good Guys",
    "url": "https://www.youtube.com/watch?v=m_2eRVz8nbM"
  },
  {
    "id": "1qydw0VWkwM",
    "title": "Poh\u2019s Cantonese Style Whole Steamed Fish | The Good Guys",
    "url": "https://www.youtube.com/watch?v=1qydw0VWkwM"
  },
  {
    "id": "wsM5wnY3Jy0",
    "title": "Poh\u2019s Parmesan And Herb Panko Parma With Slaw | The Good Guys",
    "url": "https://www.youtube.com/watch?v=wsM5wnY3Jy0"
  },
  {
    "id": "5YRxg95Q0oE",
    "title": "Yeow Family Fried Rice | The Good Guys",
    "url": "https://www.youtube.com/watch?v=5YRxg95Q0oE"
  },
  {
    "id": "Z9sSYh0SqQk",
    "title": "Find Your Perfect Coffee Machine | The Good Guys",
    "url": "https://www.youtube.com/watch?v=Z9sSYh0SqQk"
  },
  {
    "id": "HzTCLgvnHvg",
    "title": "Father's Day Gift Ideas | The Good Guys",
    "url": "https://www.youtube.com/watch?v=HzTCLgvnHvg"
  },
  {
    "id": "hfzveNOSQCE",
    "title": "Explore LG's 2024 TV Range | The Good Guys",
    "url": "https://www.youtube.com/watch?v=hfzveNOSQCE"
  },
  {
    "id": "JAR7gI3-0ak",
    "title": "Explore LG's 2024 TV Range | The Good Guys",
    "url": "https://www.youtube.com/watch?v=JAR7gI3-0ak"
  },
  {
    "id": "6gunHeDuAlg",
    "title": "Choosing A TV Stand Or Wall Mount | The Good Guys",
    "url": "https://www.youtube.com/watch?v=6gunHeDuAlg"
  },
  {
    "id": "wUvk3xSwZlw",
    "title": "Choosing The Best Media Player | The Good Guys",
    "url": "https://www.youtube.com/watch?v=wUvk3xSwZlw"
  },
  {
    "id": "QfHWK9vY02I",
    "title": "How To Choose The Right Sink & Tap | The Good Guys",
    "url": "https://www.youtube.com/watch?v=QfHWK9vY02I"
  },
  {
    "id": "suuqu03TGfs",
    "title": "How To Choose The Best Projector | The Good Guys",
    "url": "https://www.youtube.com/watch?v=suuqu03TGfs"
  },
  {
    "id": "21oi8kg-H0M",
    "title": "How to Choose the Right Portable Cooler | The Good Guys",
    "url": "https://www.youtube.com/watch?v=21oi8kg-H0M"
  },
  {
    "id": "G9y-PCPp7h4",
    "title": "How To Choose The Right Mobile Phone Accessories | The Good Guys",
    "url": "https://www.youtube.com/watch?v=G9y-PCPp7h4"
  },
  {
    "id": "jKvNn5igjwM",
    "title": "How to Choose the Right Carpet or Steam Cleaner",
    "url": "https://www.youtube.com/watch?v=jKvNn5igjwM"
  },
  {
    "id": "ZYShAKKZ_yY",
    "title": "How to Measure For A TV | The Good Guys",
    "url": "https://www.youtube.com/watch?v=ZYShAKKZ_yY"
  },
  {
    "id": "vxvKprNW-P4",
    "title": "How to Choose the Best Printer | The Good Guys",
    "url": "https://www.youtube.com/watch?v=vxvKprNW-P4"
  },
  {
    "id": "qC7lzsxbUTo",
    "title": "How to Choose the Best Home Gym Equipment | The Good Guys",
    "url": "https://www.youtube.com/watch?v=qC7lzsxbUTo"
  },
  {
    "id": "5TaS54CWM8c",
    "title": "How to Choose the Best Massager | The Good Guys",
    "url": "https://www.youtube.com/watch?v=5TaS54CWM8c"
  },
  {
    "id": "gTTeLGprDU8",
    "title": "How to Create The Best Gaming Setup | The Good Guys",
    "url": "https://www.youtube.com/watch?v=gTTeLGprDU8"
  },
  {
    "id": "nT0JnepOnoo",
    "title": "How to Choose the Best TV | The Good Guys",
    "url": "https://www.youtube.com/watch?v=nT0JnepOnoo"
  },
  {
    "id": "ynlLJ1lLW0E",
    "title": "How to Choose The Best Monitor | The Good Guys",
    "url": "https://www.youtube.com/watch?v=ynlLJ1lLW0E"
  },
  {
    "id": "9NDwDQ5HyJw",
    "title": "Top Tips For a Reliable Home Network | The Good Guys",
    "url": "https://www.youtube.com/watch?v=9NDwDQ5HyJw"
  },
  {
    "id": "tSCh9nXiu_E",
    "title": "How to Select The Best Computer Accessories | The Good Guys",
    "url": "https://www.youtube.com/watch?v=tSCh9nXiu_E"
  },
  {
    "id": "dYvLf1EE-IE",
    "title": "How to Choose the Best Camera | The Good Guys",
    "url": "https://www.youtube.com/watch?v=dYvLf1EE-IE"
  },
  {
    "id": "jfhDqjmG6zs",
    "title": "How to Choose the Right Blender | The Good Guys",
    "url": "https://www.youtube.com/watch?v=jfhDqjmG6zs"
  },
  {
    "id": "AT1SkoB1DXM",
    "title": "How to Choose the Right Rangehood | The Good Guys",
    "url": "https://www.youtube.com/watch?v=AT1SkoB1DXM"
  },
  {
    "id": "Lc04mTC5NNM",
    "title": "How to Choose the Right Freezer | The Good Guys",
    "url": "https://www.youtube.com/watch?v=Lc04mTC5NNM"
  },
  {
    "id": "UgwxZk-s7R0",
    "title": "How to Choose the Best Kitchen Mixer | The Good Guys",
    "url": "https://www.youtube.com/watch?v=UgwxZk-s7R0"
  },
  {
    "id": "uMsgVDZTZuE",
    "title": "How to Measure For a Dishwasher | The Good Guys",
    "url": "https://www.youtube.com/watch?v=uMsgVDZTZuE"
  },
  {
    "id": "cd2SrM8KI08",
    "title": "How to Measure For an Oven | The Good Guys",
    "url": "https://www.youtube.com/watch?v=cd2SrM8KI08"
  },
  {
    "id": "va3xOt9ZD-w",
    "title": "How to Choose the Right Vacuum | The Good Guys",
    "url": "https://www.youtube.com/watch?v=va3xOt9ZD-w"
  },
  {
    "id": "d3DaZZP07ko",
    "title": "How to Choose the Right Microwave | The Good Guys",
    "url": "https://www.youtube.com/watch?v=d3DaZZP07ko"
  },
  {
    "id": "J4DNUsGcqMI",
    "title": "How To Choose The Right Air Treatment | The Good Guys",
    "url": "https://www.youtube.com/watch?v=J4DNUsGcqMI"
  },
  {
    "id": "50qZCrM4ysw",
    "title": "How To Choose The Right Home Security | The Good Guys",
    "url": "https://www.youtube.com/watch?v=50qZCrM4ysw"
  },
  {
    "id": "BKI9Qu-fCMg",
    "title": "Why You Need Smart Home Security | The Good Guys",
    "url": "https://www.youtube.com/watch?v=BKI9Qu-fCMg"
  },
  {
    "id": "dgMD4SRg1Fw",
    "title": "How To Measure for a Fridge | The Good Guys",
    "url": "https://www.youtube.com/watch?v=dgMD4SRg1Fw"
  },
  {
    "id": "fzXi4WbKlGw",
    "title": "How to Choose the Right Fryer | The Good Guys",
    "url": "https://www.youtube.com/watch?v=fzXi4WbKlGw"
  },
  {
    "id": "5Fe4L7ucCd0",
    "title": "Pay Less Every day on Home Appliances | The Good Guys",
    "url": "https://www.youtube.com/watch?v=5Fe4L7ucCd0"
  },
  {
    "id": "2rvgcWI6pBE",
    "title": "How to Choose the Right Home Sound Solution | The Good Guys",
    "url": "https://www.youtube.com/watch?v=2rvgcWI6pBE"
  },
  {
    "id": "mbpGT2Xx1sY",
    "title": "How to Choose the Right Portable Heater | The Good Guys",
    "url": "https://www.youtube.com/watch?v=mbpGT2Xx1sY"
  },
  {
    "id": "gFd0Mi_FQ0o",
    "title": "The Hottest Gifts to Wow Your Loved Ones This Christmas | The Good Guys",
    "url": "https://www.youtube.com/watch?v=gFd0Mi_FQ0o"
  },
  {
    "id": "hoN1fEBHAcY",
    "title": "The Best Kitchen Appliances to Gift This Christmas | The Good Guys",
    "url": "https://www.youtube.com/watch?v=hoN1fEBHAcY"
  },
  {
    "id": "qSzVcYR9OCE",
    "title": "Wow with These Trending Gifts for 2022 | The Good Guys",
    "url": "https://www.youtube.com/watch?v=qSzVcYR9OCE"
  },
  {
    "id": "lwlfbUJI4fE",
    "title": "Give the Gift of Tech with These Wow Gifts | The Good Guys",
    "url": "https://www.youtube.com/watch?v=lwlfbUJI4fE"
  },
  {
    "id": "DB3q4CG9OfU",
    "title": "Update Your Tech This Black Friday | The Good Guys",
    "url": "https://www.youtube.com/watch?v=DB3q4CG9OfU"
  },
  {
    "id": "FMFyH0rUu_k",
    "title": "Update With Big Brands This Black Friday | The Good Guys",
    "url": "https://www.youtube.com/watch?v=FMFyH0rUu_k"
  },
  {
    "id": "KcMZX-s3EDg",
    "title": "Treat Yourself This Black Friday! | The Good Guys",
    "url": "https://www.youtube.com/watch?v=KcMZX-s3EDg"
  },
  {
    "id": "ONfc-u7s5dE",
    "title": "Get Ready For Christmas With Black Friday | The Good Guys",
    "url": "https://www.youtube.com/watch?v=ONfc-u7s5dE"
  },
  {
    "id": "YXeaGjupVLs",
    "title": "Get Ready for Black Friday | The Good Guys",
    "url": "https://www.youtube.com/watch?v=YXeaGjupVLs"
  },
  {
    "id": "H1oRRmY430g",
    "title": "What Are OLED TVs? A Comprehensive Guide to Features and Benefits",
    "url": "https://www.youtube.com/watch?v=H1oRRmY430g"
  },
  {
    "id": "y2SFK4wJgZw",
    "title": "Tips To Optimise Your Kitchen Layout | The Good Guys",
    "url": "https://www.youtube.com/watch?v=y2SFK4wJgZw"
  },
  {
    "id": "FSp7klpxdCk",
    "title": "Tips For Creating The Ultimate Outdoor Space | The Good Guys",
    "url": "https://www.youtube.com/watch?v=FSp7klpxdCk"
  },
  {
    "id": "BNQj7WiK7n8",
    "title": "Get Ready For Back To Uni | The Good Guys",
    "url": "https://www.youtube.com/watch?v=BNQj7WiK7n8"
  },
  {
    "id": "h32dcKGJHfU",
    "title": "Kid Friendly Laptops For Back To School | The Good Guys",
    "url": "https://www.youtube.com/watch?v=h32dcKGJHfU"
  },
  {
    "id": "6Zo_xxd-t3s",
    "title": "Choosing The Right Iron | The Good Guys",
    "url": "https://www.youtube.com/watch?v=6Zo_xxd-t3s"
  },
  {
    "id": "u4LIvs4UMLc",
    "title": "Tips For Creating A European Laundry | The Good Guys",
    "url": "https://www.youtube.com/watch?v=u4LIvs4UMLc"
  },
  {
    "id": "jMHDZOwYTLs",
    "title": "The Top 4 Small Kitchen Appliances You Need | The Good Guys",
    "url": "https://www.youtube.com/watch?v=jMHDZOwYTLs"
  },
  {
    "id": "W0Mh-rIC1OM",
    "title": "Choosing The Right Shaver For You | The Good Guys",
    "url": "https://www.youtube.com/watch?v=W0Mh-rIC1OM"
  },
  {
    "id": "Vd2hMRGsGe8",
    "title": "How To Choose The Right Split System | The Good Guys",
    "url": "https://www.youtube.com/watch?v=Vd2hMRGsGe8"
  },
  {
    "id": "vo8fR01ZmHo",
    "title": "Auto Dosing Washing Machines Explained | The Good Guys",
    "url": "https://www.youtube.com/watch?v=vo8fR01ZmHo"
  },
  {
    "id": "MR8udHyQGW0",
    "title": "Choosing a Wall or Freestanding Oven | The Good Guys",
    "url": "https://www.youtube.com/watch?v=MR8udHyQGW0"
  },
  {
    "id": "rSlP1Vd_FhU",
    "title": "Choosing The Right Hair Styler | The Good Guys",
    "url": "https://www.youtube.com/watch?v=rSlP1Vd_FhU"
  },
  {
    "id": "1WDDnr1x-EI",
    "title": "How To Select The Right Fridge For You | The Good Guys",
    "url": "https://www.youtube.com/watch?v=1WDDnr1x-EI"
  },
  {
    "id": "WBJuv7A2UiM",
    "title": "How To Select The Best Phone For Your Teen | The Good Guys",
    "url": "https://www.youtube.com/watch?v=WBJuv7A2UiM"
  },
  {
    "id": "HztLmDfrZ0Y",
    "title": "Noise Cancelling Headphones Explained | The Good Guys",
    "url": "https://www.youtube.com/watch?v=HztLmDfrZ0Y"
  },
  {
    "id": "zAwmn8NP_F0",
    "title": "How To Select The Right Wearable For You | The Good Guys",
    "url": "https://www.youtube.com/watch?v=zAwmn8NP_F0"
  },
  {
    "id": "6XR-W1SGWfY",
    "title": "Mother's Day Gift Guide | The Good Guys",
    "url": "https://www.youtube.com/watch?v=6XR-W1SGWfY"
  },
  {
    "id": "7KK4wsH0WfU",
    "title": "Our Fave Mother's Day Gift Ideas | The Good Guys",
    "url": "https://www.youtube.com/watch?v=7KK4wsH0WfU"
  },
  {
    "id": "ZoDtlb2LYdw",
    "title": "Mother's Day Gift Inspo | The Good Guys",
    "url": "https://www.youtube.com/watch?v=ZoDtlb2LYdw"
  },
  {
    "id": "5tB8itSh5ec",
    "title": "Mother's Day Gift Ideas! | The Good Guys",
    "url": "https://www.youtube.com/watch?v=5tB8itSh5ec"
  },
  {
    "id": "-5KkDd1SAjQ",
    "title": "Heat Pump Dryers Explained | The Good Guys",
    "url": "https://www.youtube.com/watch?v=-5KkDd1SAjQ"
  },
  {
    "id": "Vi2skDg3aFI",
    "title": "How To Select The Best Computer | The Good Guys",
    "url": "https://www.youtube.com/watch?v=Vi2skDg3aFI"
  },
  {
    "id": "4xNmCydjQrw",
    "title": "How To Select The Best Dishwasher For Your Kitchen | The Good Guys",
    "url": "https://www.youtube.com/watch?v=4xNmCydjQrw"
  },
  {
    "id": "GNv91jaZL_U",
    "title": "How To Select The Right Coffee Machine  | The Good Guys",
    "url": "https://www.youtube.com/watch?v=GNv91jaZL_U"
  },
  {
    "id": "mBjBQBL9ik8",
    "title": "Tips For A Small Laundry | The Good Guys",
    "url": "https://www.youtube.com/watch?v=mBjBQBL9ik8"
  },
  {
    "id": "wrwUqi1jyAg",
    "title": "Induction Cooktops Explained | The Good Guys",
    "url": "https://www.youtube.com/watch?v=wrwUqi1jyAg"
  },
  {
    "id": "iY22eBwj9PU",
    "title": "How To Select The Best Washing Machine For Your Laundry | The Good Guys",
    "url": "https://www.youtube.com/watch?v=iY22eBwj9PU"
  },
  {
    "id": "FtjwpAYmkSU",
    "title": "How To Select The Best Oven For Your Kitchen | The Good Guys",
    "url": "https://www.youtube.com/watch?v=FtjwpAYmkSU"
  },
  {
    "id": "52DMTYuPo5c",
    "title": "How to choose the right Dryer for your laundry | The Good Guys",
    "url": "https://www.youtube.com/watch?v=52DMTYuPo5c"
  },
  {
    "id": "iJeViVW1FSQ",
    "title": "How To Buy The Best Cooktop For Your Kitchen | The Good Guys",
    "url": "https://www.youtube.com/watch?v=iJeViVW1FSQ"
  },
  {
    "id": "4QnqOgDCzLo",
    "title": "How To Choose Safe Family-Friendly Kitchen Appliances | The Good Guys",
    "url": "https://www.youtube.com/watch?v=4QnqOgDCzLo"
  },
  {
    "id": "DuUpBi7PHbc",
    "title": "Why We Love Air Purifiers | The Good Guys",
    "url": "https://www.youtube.com/watch?v=DuUpBi7PHbc"
  },
  {
    "id": "gt0mNUXoTF0",
    "title": "What is Mini LED Technology? A Comprehensive Guide to Advanced Backlighting for TVs",
    "url": "https://www.youtube.com/watch?v=gt0mNUXoTF0"
  },
  {
    "id": "IRNWBsTdoqY",
    "title": "Getting Your New TV Home Safely | The Good Guys",
    "url": "https://www.youtube.com/watch?v=IRNWBsTdoqY"
  },
  {
    "id": "L3fHS94r-CY",
    "title": "Oven Installation is Made Easy with The Good Guys Home Services",
    "url": "https://www.youtube.com/watch?v=L3fHS94r-CY"
  },
  {
    "id": "H-KP4NFFALY",
    "title": "Wall Mount TV Installation is Made Easy with The Good Guys Home Services",
    "url": "https://www.youtube.com/watch?v=H-KP4NFFALY"
  },
  {
    "id": "GtYcT7At3rw",
    "title": "Upright Stove Installation is Made Easy with The Good Guys Home Services",
    "url": "https://www.youtube.com/watch?v=GtYcT7At3rw"
  },
  {
    "id": "0ise9WYSDGU",
    "title": "Air Conditioner Installation is Made Easy with The Good Guys Home Services",
    "url": "https://www.youtube.com/watch?v=0ise9WYSDGU"
  },
  {
    "id": "RDFXKqY_n8M",
    "title": "Rangehood Installation is Made Easy with The Good Guys Home Services",
    "url": "https://www.youtube.com/watch?v=RDFXKqY_n8M"
  },
  {
    "id": "wxNCqlTidP0",
    "title": "Dryer Installation is Made Easy with The Good Guys Home Services",
    "url": "https://www.youtube.com/watch?v=wxNCqlTidP0"
  },
  {
    "id": "pHqsk9TbqzY",
    "title": "Dishwasher Installation is Made Easy with The Good Guys Home Services",
    "url": "https://www.youtube.com/watch?v=pHqsk9TbqzY"
  },
  {
    "id": "THQRS8SI8Mc",
    "title": "Cooktop Installation is Made Easy with The Good Guys Home Services",
    "url": "https://www.youtube.com/watch?v=THQRS8SI8Mc"
  },
  {
    "id": "NZciQqP7M3U",
    "title": "Episode 5: Neale Whitaker goes into detail about Kinsman as a company, what they offer and more.",
    "url": "https://www.youtube.com/watch?v=NZciQqP7M3U"
  },
  {
    "id": "FUGDBeXOFOM",
    "title": "Episode 4: Neale Whitaker takes you through the Kinsman kitchen process step by step.",
    "url": "https://www.youtube.com/watch?v=FUGDBeXOFOM"
  },
  {
    "id": "-An0ZRSWyeE",
    "title": "Episode 3: Neale Whitaker explains the importance of visiting a Kinsman Showroom before renovating.",
    "url": "https://www.youtube.com/watch?v=-An0ZRSWyeE"
  },
  {
    "id": "HcXnxD3Lg34",
    "title": "Episode 2: Neale Whitaker shares tips on the ideal kitchen design for Kinsman Kitchens.",
    "url": "https://www.youtube.com/watch?v=HcXnxD3Lg34"
  },
  {
    "id": "pPtKHKjyKRg",
    "title": "Create a Deliciously Simple Chicken Stir Fry with Adam Liaw  | The Good Guys",
    "url": "https://www.youtube.com/watch?v=pPtKHKjyKRg"
  }
]


def run(cmd, timeout=120):
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return result.stdout, result.stderr, result.returncode


def get_transcript(video_id, video_url, tmpdir):
    out_template = os.path.join(tmpdir, video_id)

    for sub_flag in ["--write-auto-sub", "--write-sub"]:
        try:
            run([
                sys.executable, "-m", "yt_dlp",
                sub_flag,
                "--skip-download",
                "--sub-lang", "en",
                "--sub-format", "json3",
                "--no-warnings",
                "-o", out_template,
                video_url
            ])
        except subprocess.TimeoutExpired:
            continue

        sub_files = list(Path(tmpdir).glob(f"{video_id}*.json3"))
        if not sub_files:
            continue

        sub_file = sub_files[0]
        try:
            with open(sub_file, encoding="utf-8") as f:
                data = json.load(f)
            os.remove(sub_file)

            transcript = []
            for e in data.get("events", []):
                if not e.get("segs"):
                    continue
                start_s = e.get("tStartMs", 0) / 1000
                duration_s = e.get("dDurationMs", 0) / 1000
                text = "".join(s.get("utf8", "") for s in e["segs"]).replace("\n", " ").strip()
                if not text:
                    continue
                m, s = divmod(int(start_s), 60)
                transcript.append({
                    "start": round(start_s, 2),
                    "startFormatted": f"{m}:{s:02d}",
                    "duration": round(duration_s, 2),
                    "text": text
                })

            if transcript:
                return transcript
        except Exception:
            if sub_file.exists():
                os.remove(sub_file)

    return None


def main():
    print(f"📋 Processing {len(VIDEOS)} videos...\n")
    results = []
    success_count = 0

    with tempfile.TemporaryDirectory() as tmpdir:
        for i, video in enumerate(VIDEOS, 1):
            label = f"[{i}/{len(VIDEOS)}]"
            vid_id = video["id"]
            title = video["title"]
            url = video["url"]

            transcript = get_transcript(vid_id, url, tmpdir)

            if transcript:
                print(f"   {label} ✅ {len(transcript)} segments — {title}")
                success_count += 1
                results.append({
                    "url": url, "videoId": vid_id, "title": title,
                    "hasTranscript": True, "transcriptLength": len(transcript),
                    "transcript": transcript
                })
            else:
                print(f"   {label} ⚠️  No transcript — {title}")
                results.append({
                    "url": url, "videoId": vid_id, "title": title,
                    "hasTranscript": False, "transcriptLength": 0, "transcript": []
                })

            time.sleep(0.5)

    print(f"\n📊 {success_count}/{len(VIDEOS)} transcripts extracted")

    output_file = f"tgg_youtube_transcripts_{date.today()}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved to {output_file}")


if __name__ == "__main__":
    main()

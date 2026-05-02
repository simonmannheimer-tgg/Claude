"""
GTIN validation utilities for AEO schema checks.

Supports GTIN-8, GTIN-12 (UPC-A), GTIN-13 (EAN-13), and GTIN-14.
Also validates GS1 Digital Link URLs (used in Product.sameAs for AI product matching).
"""

import re


def validate_gtin(gtin: str) -> bool:
    """
    Luhn-style check digit validation for GTIN-8/12/13/14.

    Returns True if the check digit is valid, False otherwise.
    Non-numeric characters are stripped before validation (handles hyphens, spaces).
    """
    digits = re.sub(r"\D", "", str(gtin))
    if len(digits) not in (8, 12, 13, 14):
        return False
    total = 0
    for i, d in enumerate(reversed(digits[:-1])):
        n = int(d)
        total += n * 3 if i % 2 == 0 else n
    expected_check = (10 - total % 10) % 10
    return expected_check == int(digits[-1])


def validate_gs1_digital_link(url: str) -> bool:
    """
    Checks if a URL matches the GS1 Digital Link structure.

    Valid examples:
        https://id.gs1.org/01/09506000134352
        https://www.thegoodguys.com.au/01/09506000134352/10/ABC123

    The /01/<gtin14> segment is the minimum required for a Digital Link.
    Returns True if the GTIN-14 in the URL also passes check digit validation.
    """
    match = re.search(r"/01/(\d{14})", url)
    if not match:
        return False
    return validate_gtin(match.group(1))


def normalise_gtin(gtin: str) -> str | None:
    """
    Normalises a GTIN string to its canonical form (no separators, zero-padded to 14 digits).
    Returns None if the raw value is not a valid GTIN.
    """
    digits = re.sub(r"\D", "", str(gtin))
    if len(digits) not in (8, 12, 13, 14):
        return None
    if not validate_gtin(digits):
        return None
    return digits.zfill(14)

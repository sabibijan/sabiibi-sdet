PACKAGES = [
    {"key": "archetypeEdit", "name": "The Archetype Edit", "price_usd": 150, "price_text": "$150",
     "checkout_url": "https://hello.dubsado.com/public/form/view/6ab92920a2c03493f789dbe5", "call_minutes": None},
    {"key": "signatureStyling", "name": "The Signature Styling", "price_usd": 500, "price_text": "$500",
     "checkout_url": "https://hello.dubsado.com/public/form/view/6ab92e28a2c03493f789e4a8", "call_minutes": 30},
    {"key": "fullTransformation", "name": "The Full Transformation", "price_usd": 1000, "price_text": "$1,000",
     "checkout_url": "https://hello.dubsado.com/public/form/view/6ab92f2ca2c03493f789e765", "call_minutes": 60},
]
BY_KEY = {p["key"]: p for p in PACKAGES}          # a dict comprehension: look up by key
CONTACT_EMAIL = "contact@sabiibi.com"
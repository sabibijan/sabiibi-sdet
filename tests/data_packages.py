PACKAGES = [
    {"key": "archetypeEdit", "name": "The Archetype Edit", "price_usd": 300, "price_text": "$300",
     "checkout_url": "https://hello.dubsado.com/public/form/view/6ab92920a2c03493f789dbe5", "call_minutes": None},
    {"key": "signatureStyling", "name": "The Signature Styling", "price_usd": 900, "price_text": "$900",
     "checkout_url": "https://hello.dubsado.com/public/form/view/6ab92e28a2c03493f789e4a8", "call_minutes": 30},
    {"key": "fullTransformation", "name": "The Full Transformation", "price_usd": 2000, "price_text": "$2,000",
     "checkout_url": "https://hello.dubsado.com/public/form/view/6ab92f2ca2c03493f789e765", "call_minutes": 60},
]
BY_KEY = {p["key"]: p for p in PACKAGES}          # a dict comprehension: look up by key
CONTACT_EMAIL = "contact@sabiibi.com"
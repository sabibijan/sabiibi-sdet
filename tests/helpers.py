def format_price(amount: int) -> str:
    """1000 -> '$1000' (how the website writes prices)."""
    return f"${amount:,}"
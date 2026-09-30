from data_packages import PACKAGES, BY_KEY
from helpers import format_price


def test_there_are_three_packages():
    assert len(PACKAGES) == 3


def test_format_price_adds_dollar_and_comma():
    assert format_price(1000) == "$1,000"
    assert format_price(150) == "$150"


def test_price_text_matches_price_number():
    for p in PACKAGES:
        assert p["price_text"] == format_price(p["price_usd"]), p["key"]


def test_checkout_links_are_unique():
    urls = [p["checkout_url"] for p in PACKAGES]
    assert len(set(urls)) == len(urls)


def test_only_higher_packages_include_a_call():
    assert BY_KEY["archetypeEdit"]["call_minutes"] is None
    assert BY_KEY["fullTransformation"]["call_minutes"] == 60
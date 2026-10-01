import pytest
from data_packages import PACKAGES, BY_KEY
from helpers import format_price

pytestmark = pytest.mark.unit


def test_there_are_three_packages():
    assert len(PACKAGES) == 3


@pytest.mark.parametrize("amount, expected", [(150, "$150"), (500, "$500"), (1000, "$1,000"), (0, "$0")])
def test_format_price(amount, expected):
    assert format_price(amount) == expected


@pytest.mark.parametrize("pkg", PACKAGES, ids=lambda p: p["key"])
def test_price_text_matches_price_number(pkg):
    assert pkg["price_text"] == format_price(pkg["price_usd"])


def test_checkout_links_are_unique():
    urls = [p["checkout_url"] for p in PACKAGES]
    assert len(set(urls)) == len(urls)


def test_only_higher_packages_include_a_call():
    assert BY_KEY["archetypeEdit"]["call_minutes"] is None
    assert BY_KEY["fullTransformation"]["call_minutes"] == 60
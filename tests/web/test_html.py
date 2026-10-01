"""Fast checks on the raw HTML, no browser needed."""
import pytest
from data_packages import PACKAGES, CONTACT_EMAIL

pytestmark = pytest.mark.web          # every test in this file gets the 'web' marker


def test_title(homepage_html):
    assert "Sabiibi Transforms" in homepage_html


@pytest.mark.parametrize("pkg", PACKAGES, ids=lambda p: p["key"])
def test_price_is_in_the_page(homepage_html, pkg):
    assert pkg["price_text"] in homepage_html


@pytest.mark.parametrize("pkg", PACKAGES, ids=lambda p: p["key"])
def test_checkout_link_is_in_the_page(homepage_html, pkg):
    assert pkg["checkout_url"] in homepage_html


def test_contact_email(homepage_html):
    assert f"mailto:{CONTACT_EMAIL}" in homepage_html
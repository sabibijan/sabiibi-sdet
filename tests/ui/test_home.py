import re

import pytest
from playwright.sync_api import Page, expect
from data_packages import PACKAGES

pytestmark = pytest.mark.ui


def test_page_loads_with_title(page: Page):
    response = page.goto("/")
    assert response.status == 200
    expect(page).to_have_title(re.compile("Sabiibi Transforms"))


def test_no_javascript_errors(page: Page):
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto("/")
    page.wait_for_load_state("load")
    assert errors == []


@pytest.mark.parametrize("name, target", [
    ("Packages", "#packages"), ("Process", "#process"), ("About", "#about"), ("Book", "#contact")])
def test_nav_links(page: Page, name, target):
    page.goto("/")
    link = page.locator("nav").get_by_role("link", name=name, include_hidden=True)
    expect(link).to_have_attribute("href", target)


def test_three_package_cards(page: Page):
    page.goto("/")
    expect(page.locator("#packages .pkg")).to_have_count(3)



@pytest.mark.parametrize("pkg", PACKAGES, ids=lambda p: p["key"])
def test_package_price(page: Page, pkg):
    page.goto("/")
    card = page.locator("#packages .pkg").filter(
        has=page.locator(".pkg-name").get_by_text(pkg["name"], exact=True))    
    expect(card.locator(".price")).to_have_text(pkg["price_text"])
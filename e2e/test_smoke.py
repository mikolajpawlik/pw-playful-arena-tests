from playwright.sync_api import Page, expect


class TestSmoke:
    def test_app_loads_successfully(self, page: Page):
        page.goto("/")
        expect(page).not_to_have_title("")
        expect(page.locator("body")).to_be_visible()

    def test_pwa_manifest_is_present(self, page: Page):
        page.goto("/")
        expect(page.locator('link[rel="manifest"]')).to_have_count(1)

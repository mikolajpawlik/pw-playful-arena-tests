from playwright.sync_api import Page, expect


class TestAsync:
    def test_fetch_success_shows_result(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-fetch-ok").click()
        expect(page.get_by_test_id("fetch-result")).to_be_visible(timeout=5000)

    def test_fetch_error_shows_error(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-fetch-fail").click()
        expect(page.get_by_test_id("fetch-error")).to_be_visible(timeout=5000)

    def test_success_result_does_not_show_error(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-fetch-ok").click()
        expect(page.get_by_test_id("fetch-result")).to_be_visible(timeout=10000)
        expect(page.get_by_test_id("fetch-error")).not_to_be_visible()

    def test_fetch_fail_then_ok_shows_result(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-fetch-fail").click()
        expect(page.get_by_test_id("fetch-error")).to_be_visible(timeout=5000)
        page.get_by_test_id("btn-fetch-ok").click()
        expect(page.get_by_test_id("fetch-result")).to_be_visible(timeout=5000)

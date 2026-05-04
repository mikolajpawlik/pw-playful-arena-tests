from playwright.sync_api import Page, expect


class TestOverlays:
    def test_modal_opens_and_closes(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-open-modal").click()
        expect(page.get_by_test_id("modal-dialog")).to_be_visible()
        page.get_by_test_id("modal-cancel").click()
        expect(page.get_by_test_id("modal-dialog")).not_to_be_visible()

    def test_modal_confirm_button(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-open-modal").click()
        expect(page.get_by_test_id("modal-dialog")).to_be_visible()
        page.get_by_test_id("modal-confirm").click()
        expect(page.get_by_test_id("modal-dialog")).not_to_be_visible()

    def test_toast_appears_and_disappears(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-show-alert").click()
        expect(page.get_by_test_id("toast")).to_be_visible()
        expect(page.get_by_test_id("toast")).not_to_be_visible(timeout=6000)

    def test_native_confirm_accept(self, page: Page):
        page.goto("/")
        page.on("dialog", lambda d: d.accept())
        page.get_by_test_id("btn-native-confirm").click()
        expect(page.get_by_test_id("confirm-result")).to_contain_text("tak")

    def test_native_confirm_dismiss(self, page: Page):
        page.goto("/")
        page.on("dialog", lambda d: d.dismiss())
        page.get_by_test_id("btn-native-confirm").click()
        expect(page.get_by_test_id("confirm-result")).to_contain_text("nie")

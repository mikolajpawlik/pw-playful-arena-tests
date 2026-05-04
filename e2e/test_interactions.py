from playwright.sync_api import Page, expect


class TestButtons:
    def test_click_counter_increments(self, page: Page):
        page.goto("/")
        button = page.get_by_test_id("btn-counter")
        expect(button).to_contain_text("0")
        button.click()
        expect(button).to_contain_text("1")
        button.click()
        button.click()
        expect(button).to_contain_text("3")

    def test_double_click(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-double").dblclick()
        expect(page.get_by_test_id("msg-double")).to_be_visible()

    def test_right_click(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-right").click(button="right")
        expect(page.get_by_test_id("msg-right")).to_be_visible()

    def test_disabled_button_cannot_be_clicked(self, page: Page):
        page.goto("/")
        expect(page.get_by_test_id("btn-disabled")).to_be_disabled()

    def test_delayed_element_appears_after_click(self, page: Page):
        page.goto("/")
        expect(page.get_by_test_id("delayed-element")).not_to_be_visible()
        page.get_by_test_id("btn-delayed-toggle").click()
        page.get_by_test_id("delayed-element").wait_for(state="visible", timeout=3000)

    def test_long_press(self, page: Page):
        page.goto("/")
        button = page.get_by_test_id("btn-longpress")
        button.scroll_into_view_if_needed()
        page.wait_for_timeout(200)
        button.click(delay=900)
        expect(page.get_by_test_id("msg-longpress")).to_be_visible()


class TestDynamicState:
    def test_tabs_switch_panels(self, page: Page):
        page.goto("/")
        page.get_by_test_id("tab-a").click()
        expect(page.get_by_test_id("tab-panel-a")).to_be_visible()
        page.get_by_test_id("tab-b").click()
        expect(page.get_by_test_id("tab-panel-b")).to_be_visible(timeout=8000)
        expect(page.get_by_test_id("tab-panel-a")).not_to_be_visible()
        page.get_by_test_id("tab-c").click()
        expect(page.get_by_test_id("tab-panel-c")).to_be_visible(timeout=8000)
        expect(page.get_by_test_id("tab-panel-b")).not_to_be_visible()

    def test_add_and_remove_list_item(self, page: Page):
        page.goto("/")
        page.get_by_test_id("input-new-item").fill("nowe zadanie")
        page.get_by_test_id("btn-add-item").click()
        new_item = page.get_by_test_id("dynamic-list").get_by_text("nowe zadanie")
        expect(new_item).to_be_visible()
        page.get_by_test_id("dynamic-list").locator("[data-testid$='-remove']").last.click()
        expect(new_item).not_to_be_visible()

    def test_toggle_visibility(self, page: Page):
        page.goto("/")
        target = page.get_by_test_id("visible-target")
        page.get_by_test_id("btn-toggle-visibility").click()
        expect(target).not_to_be_visible()
        page.get_by_test_id("btn-toggle-visibility").click()
        expect(target).to_be_visible()

    def test_progress_bar_reaches_100(self, page: Page):
        page.goto("/")
        page.get_by_test_id("btn-start-progress").click()
        expect(page.get_by_test_id("progress-value")).to_contain_text("100", timeout=10000)

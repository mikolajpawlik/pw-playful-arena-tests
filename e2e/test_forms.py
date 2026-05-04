from playwright.sync_api import Page, expect


class TestForms:
    def test_valid_submission(self, page: Page):
        page.goto("/")

        page.get_by_test_id("input-name").fill("Jan Kowalski")
        page.get_by_test_id("input-email").fill("jan@example.com")
        page.get_by_test_id("select-role").select_option(label="QA Engineer")
        page.get_by_test_id("checkbox-newsletter").check()
        page.get_by_test_id("button-submit").click()
        result = page.get_by_test_id("form-result")
        expect(result).to_be_visible()
        expect(result).to_contain_text("Jan Kowalski")
        expect(result).to_contain_text("jan@example.com")

    def test_submit_without_name_shows_no_result(self, page: Page):
        page.goto("/")

        page.get_by_test_id("input-email").fill("jan@example.com")
        page.get_by_test_id("button-submit").click()
        expect(page.get_by_test_id("form-result")).not_to_be_visible()

    def test_submit_with_invalid_email_shows_no_result(self, page: Page):
        page.goto("/")

        page.get_by_test_id("input-name").fill("Jan Kowalski")
        page.get_by_test_id("input-email").fill("to-nie-jest-email")
        page.get_by_test_id("button-submit").click()
        expect(page.get_by_test_id("form-result")).not_to_be_visible()

    def test_reset_clears_all_fields(self, page: Page):
        page.goto("/")

        page.get_by_test_id("input-name").fill("Jan Kowalski")
        page.get_by_test_id("input-email").fill("jan@example.com")
        page.get_by_test_id("checkbox-newsletter").check()
        page.get_by_test_id("button-reset").click()
        expect(page.get_by_test_id("input-name")).to_have_value("")
        expect(page.get_by_test_id("input-email")).to_have_value("")
        expect(page.get_by_test_id("checkbox-newsletter")).not_to_be_checked()

    def test_all_role_options_selectable(self, page: Page):
        page.goto("/")

        select = page.get_by_test_id("select-role")
        for role in ["QA Engineer", "Developer", "Product Manager"]:
            select.select_option(label=role)

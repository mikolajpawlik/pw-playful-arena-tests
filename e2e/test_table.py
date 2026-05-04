from playwright.sync_api import Page, expect


class TestDataTable:
    def test_table_renders_rows(self, page: Page):
        page.goto("/")
        table = page.get_by_test_id("users-table")
        expect(table).to_be_visible()
        assert table.get_by_role("row").count() > 1

    def test_select_row_updates_count(self, page: Page):
        page.goto("/")
        page.get_by_test_id("row-1-select").check()
        expect(page.get_by_test_id("table-selected-count")).to_contain_text("1")

    def test_select_multiple_rows(self, page: Page):
        page.goto("/")
        page.get_by_test_id("row-1-select").check()
        page.get_by_test_id("row-2-select").check()
        page.get_by_test_id("row-3-select").check()
        expect(page.get_by_test_id("table-selected-count")).to_contain_text("3")

    def test_sort_by_score_column(self, page: Page):
        page.goto("/")
        page.get_by_test_id("th-score").click()
        score_cells = page.locator("[data-testid^='row-'][data-testid$='-score']").all()
        scores = [int(cell.inner_text()) for cell in score_cells]
        assert scores == sorted(scores) or scores == sorted(scores, reverse=True)


class TestDragAndDrop:
    def test_drag_card_from_todo_to_done(self, page: Page):
        page.goto("/")
        todo_list = page.get_by_test_id("column-todo-list")
        done_list = page.get_by_test_id("column-done-list")
        todo_count_before = todo_list.get_by_role("listitem").count()
        done_count_before = done_list.get_by_role("listitem").count()
        page.get_by_test_id("card-test-login").drag_to(done_list)
        expect(todo_list.get_by_role("listitem")).to_have_count(todo_count_before - 1)
        expect(done_list.get_by_role("listitem")).to_have_count(done_count_before + 1)

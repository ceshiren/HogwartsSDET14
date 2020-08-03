import pytest
import yaml

from xueqiu_app.page.app import App


class TestXueqiu:
    def setup(self):
        self.app = App()

    def load_data(self):
        with open("./data.yaml", encoding="utf-8") as f:
            result = yaml.safe_load(f)
        return result

    @pytest.mark.parametrize("stock_name", load_data(0))
    def test_search(self, stock_name):
        search = self.app.start().goto_main().goto_market().goto_search()
        search.search(stock_name)
        assert search.is_choose(stock_name)
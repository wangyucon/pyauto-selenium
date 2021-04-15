"""
测试用例
"""
import pytest

@pytest.mark.usefixtures('browser','browser_close')
class TestSearch:
    def test_one(self,browser,base_url):
        browser.get(base_url)
        browser.find_element_by_id('kw').send_keys('自动化测试')
        browser.find_element_by_id('ss').click()

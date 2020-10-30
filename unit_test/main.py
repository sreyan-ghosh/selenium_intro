import unittest
from selenium import webdriver
import page

# it is important to know that in case of multiple test cases, the way unittest works is it first runs the first test it
# encounters on the way down and then checks whether it passed, tears down the test and and then sets it up again.
# If we had test1 and test2 then unittest to setUp, check test1, tearDown, setUp, check test2 and tearDown.
class PythonOrgClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/mnt/d/web_dev/chromedriver.exe')
        self.driver.get("http://www.python.org")
    
    # any test in this class must start with the word "test" and then it can be followed by anything
    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
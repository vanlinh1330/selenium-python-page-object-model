import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Firefox()
        self.driver.get("https://www.lazada.vn/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=1).run(suite)

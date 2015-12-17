import selenium, unittest, time
from selenium import webdriver


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://master-cmm.integration.covermymeds.com/user/login"
        self.driver.implicitly_wait(15)

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("deanmax")
        driver.find_element_by_name("plaintext_password").clear()
        driver.find_element_by_name("plaintext_password").send_keys("wangwang")
        driver.find_element_by_css_selector("a.button2").click()
        # time.sleep(5)
        element = driver.find_element_by_css_selector("div.ud_title")
        # print element.text
        self.assertEqual(element.text, "How to Start A PA Request")

    def tearDown(self):
        self.driver.quit()
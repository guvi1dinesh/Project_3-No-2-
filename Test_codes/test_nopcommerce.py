from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_data import data2
import pytest
from webdriver_manager.firefox import GeckoDriverManager
import time


class TestNopCommerce:
    url = 'https://demo.nopcommerce.com/login'

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    # # Testcase ID:- TC_Login_01
    def test_login_01(self, booting_function):
        self.driver.get(self.url)

        # Click registration button on left side of the webpage.

        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.register_xpath))
        )
        register_button.click()

        #  Fill your personal details:

        # Firstname:
        first_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.first_name_input))
        )
        first_name.send_keys(data2.TestData.firstname)

        # Lastname:
        last_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.last_name_input))
        )
        last_name.send_keys(data2.TestData.lastname)

        # Email:
        Email = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input))
        )
        Email.send_keys(data2.TestData.email)

        # Password:
        Password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input))
        )
        Password.send_keys(data2.TestData.password)

        # Confirm Password:
        ConfirmPassword = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_2))
        )
        ConfirmPassword.send_keys(data2.TestData.password_2)

        # Click register button(to save customer details):
        register_button_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.register_xpath_2))
        )
        register_button_2.click()

        # Expected result:
        print('Registration of customer account successfully.')

    #
    # # Testcase ID:- TC_Login_02
    def test_login_02(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Tester@yahoo.com).

        Email1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_2))
        )
        Email1.send_keys(data2.TestData.email2)

        # Enter the (password: admin123).

        password3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_3))
        )
        password3.send_keys(data2.TestData.password_3)

        # Click the “Login” button.

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath))
        )
        login_button.click()

        # Validation:
        # 1) Computers
        computers = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.computers_xpath))
        )
        text1 = computers.text
        print(text1)
        computers.click()

        # 2) Electronics
        electronics = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.electronics_xpath))
        )
        text1 = electronics.text
        print(text1)
        electronics.click()

        # 3) Apparel
        apparel = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.apparel_xpath))
        )
        text1 = apparel.text
        print(text1)
        apparel.click()

        # 4) Digital downloads
        digital_downloads = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.digital_xpath))
        )
        text1 = digital_downloads.text
        print(text1)
        digital_downloads.click()

        # 5) Books
        books = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.books_xpath))
        )
        text1 = books.text
        print(text1)
        books.click()

        # 6) Jewelery
        jewelry = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.jewelry_xpath))
        )
        text1 = jewelry.text
        print(text1)
        jewelry.click()

        # 7) Gift cards
        gift_cards = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.gift_card_xpath))
        )
        text1 = gift_cards.text
        print(text1)
        gift_cards.click()

        # Expected result:
        print('Test_Login_02 executed Successfully')

    def test_login_03(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Tester@yahoo.com).

        Email1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_2))
        )
        Email1.send_keys(data2.TestData.email2)

        # Enter the (password: admin123).

        password3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_3))
        )
        password3.send_keys(data2.TestData.password_3)

        # Click the “Login” button.

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath))
        )
        login_button.click()
        time.sleep(5)
        self.driver.execute_script('window.scrollBy(0, 1900)')

        # Validating -> Community poll
        # 1) Excellent
        excellent = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, data2.TestSelectors.excellent_xpath))
        )
        excellent.click()

        # 2) Good
        good = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.good_xpath))
        )
        good.click()

        # 3) Poor
        poor = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.poor_xpath))
        )
        poor.click()

        # 4) Very bad
        Very_bad = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.very_bad_xpath))
        )
        Very_bad.click()

        # 5) Vote
        Vote = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.vote_xpath))
        )
        Vote.click()
        time.sleep(3)

        # Expected result:
        print('Test_Login_03 executed Successfully')

    def test_login_04(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Tester@yahoo.com).

        Email1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_2))
        )
        Email1.send_keys(data2.TestData.email2)

        # Enter the (password: admin123).

        password3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_3))
        )
        password3.send_keys(data2.TestData.password_3)

        # Click the “Login” button.

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath))
        )
        login_button.click()
        time.sleep(3)
        self.driver.execute_script('window.scrollBy(0, 900)')

        # Validation (Information):
        # 1) Site map:
        Site_map = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.site_map_xpath))
        )
        text1 = Site_map.text
        print(text1)
        Site_map.click()

        # 2) Shipping & returns:
        Shipping_returns = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.ship_returns_xpath))
        )
        text1 = Shipping_returns.text
        print(text1)
        Shipping_returns.click()

        # 3) Privacy notice:
        Privacy_notice = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.privacy_notice_xpath))
        )
        text1 = Privacy_notice.text
        print(text1)
        Privacy_notice.click()

        # 4) Conditions of Use:
        Conditions_of_use = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.conditions_of_use_xpath))
        )
        text1 = Conditions_of_use.text
        print(text1)
        Conditions_of_use.click()

        # 5) About us:
        About_us = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.about_us_xpath))
        )
        text1 = About_us.text
        print(text1)
        About_us.click()

        # 6) Contact us:
        Contact_us = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.contact_us_xpath))
        )
        text1 = Contact_us.text
        print(text1)
        Contact_us.click()

        # Expected result:
        print('Test_Login_04 executed Successfully')

    def test_login_05(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Tester@yahoo.com).

        Email1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_2))
        )
        Email1.send_keys(data2.TestData.email2)

        # Enter the (password: admin123).

        password3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_3))
        )
        password3.send_keys(data2.TestData.password_3)

        # Click the “Login” button.

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath))
        )
        login_button.click()
        time.sleep(3)
        self.driver.execute_script('window.scrollBy(0, 900)')

        # Validation (Customer service):
        # 1) Search:
        Search = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.search_xpath))
        )
        text1 = Search.text
        print(text1)
        Search.click()

        # 2) News:
        news = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.news_xpath))
        )
        text1 = news.text
        print(text1)
        news.click()

        # 3) Blog:
        blog = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.blog_xpath))
        )
        text1 = blog.text
        print(text1)
        blog.click()

        # 4) Recently viewed products:
        rec_view_products = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.rec_view_products_xpath))
        )
        text1 = rec_view_products.text
        print(text1)
        rec_view_products.click()

        # 5) Compare products list:
        Compare_prod_list = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.compare_prod_list_xpath))
        )
        text1 = Compare_prod_list.text
        print(text1)
        Compare_prod_list.click()

        # 6) New products:
        New_products = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.new_products_xpath))
        )
        text1 = New_products.text
        print(text1)
        New_products.click()

        # Expected result:
        print('Test_Login_05 executed Successfully')

    def test_login_06(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Tester@yahoo.com).

        Email1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_2))
        )
        Email1.send_keys(data2.TestData.email2)

        # Enter the (password: admin123).

        password3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_3))
        )
        password3.send_keys(data2.TestData.password_3)

        # Click the “Login” button.

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath))
        )
        login_button.click()
        time.sleep(3)
        self.driver.execute_script('window.scrollBy(0, 900)')

        # Validation (My Account):
        # 1) My Account:
        my_account = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.my_account_xpath))
        )
        text1 = my_account.text
        print(text1)
        my_account.click()

        # 2) Orders:
        orders = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.orders_xpath))
        )
        text1 = orders.text
        print(text1)
        orders.click()

        # 3) Addresses:
        addresses = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.addresses_xpath))
        )
        text1 = addresses.text
        print(text1)
        addresses.click()

        # 4) Shopping cart:
        shopping_cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.shopping_cart_xpath))
        )
        text1 = shopping_cart.text
        print(text1)
        shopping_cart.click()

        # 5) Wishlist:
        wishlist = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.wishlist_xpath))
        )
        text1 = wishlist.text
        print(text1)
        wishlist.click()

        # 6) Apply for vendor account:
        apply_vendor_account = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.apply_vendor_account_xpath))
        )
        text1 = apply_vendor_account.text
        print(text1)
        apply_vendor_account.click()

        # Expected result:
        print('Test_Login_06 executed Successfully')

    def test_login_07(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Tester@yahoo.com).

        Email1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_2))
        )
        Email1.send_keys(data2.TestData.email2)

        # Enter the (password: admin123).

        password3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_3))
        )
        password3.send_keys(data2.TestData.password_3)

        # Click the “Login” button.

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath))
        )
        login_button.click()
        time.sleep(3)
        self.driver.execute_script('window.scrollBy(0, 900)')

        # Validation (Follow us):
        # 1) Facebook:
        facebook = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.facebook_xpath))
        )
        text1 = facebook.text
        print(text1)
        facebook.click()

        # 2) Twitter:
        twitter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.twitter_xpath))
        )
        text1 = twitter.text
        print(text1)
        twitter.click()

        # 3) RSS:
        rss = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.rss_xpath))
        )
        text1 = rss.text
        print(text1)
        rss.click()

        # 4) Youtube:
        youtube = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.youtube_xpath))
        )
        text1 = youtube.text
        print(text1)
        youtube.click()

        # Expected result:
        print('Test_Login_07 executed Successfully')

    def test_login_08(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Tester@yahoo.com).

        Email1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_2))
        )
        Email1.send_keys(data2.TestData.email2)

        # Enter the (password: admin123).

        password3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_3))
        )
        password3.send_keys(data2.TestData.password_3)

        # Click the “Login” button.

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath))
        )
        login_button.click()
        time.sleep(3)

        # Validation :
        # 1) Register:
        register = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.reg_xpath))
        )
        text1 = register.text
        print(text1)
        register.click()

        # 2) wishlist:
        wishlist = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.wish_list_xpath))
        )
        text1 = wishlist.text
        print(text1)
        wishlist.click()

        # 4) Logout:
        register = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.logout_xpath))
        )
        text1 = register.text
        print(text1)
        register.click()

        # Expected result:
        print('Test_Login_08 executed Successfully')
        
        









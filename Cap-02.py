"""
TestcaseID:TC_PIM_01

Test objective:
  Forgot password link validation on login page
URL= https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Precondition:
1.Launch URL
2.OrangeHRM 3.0 site launched on a compatible browser
3.Click on “Forgot password” link
Steps
1.Username textbox is visible
2.Provide username
3.Click on Reset Password

Expected Result:
The user should be able to see the username box and get a successful message saying “Reset password link sent successfully”.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


# Login Page POM
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")
        self.forgot_password_link_locator = (By.XPATH, "//a[text()='Forgot your password?']")
        self.reset_username_locator = (By.NAME, "username")
        self.reset_button_locator = (By.XPATH, "//button[text()='Reset Password']")
        self.success_message_locator = (By.XPATH, "//p[text()='Reset password link sent successfully.']")

    def login(self, username, password):
        """Perform login action."""
        try:
            self.wait.until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
            self.wait.until(EC.presence_of_element_located(self.password_locator)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.login_button_locator)).click()
            print("[INFO] Login successful.")
        except TimeoutException:
            raise Exception("[ERROR] Login elements not found or not clickable within the timeout period.")

    def click_forgot_password(self):
        """Click the 'Forgot password' link."""
        try:
            self.wait.until(EC.element_to_be_clickable(self.forgot_password_link_locator)).click()
            print("[INFO] 'Forgot password' link clicked.")
        except TimeoutException:
            raise Exception("[ERROR] 'Forgot password' link not clickable within the timeout period.")

    def reset_password(self, username):
        """Enter username and click Reset Password."""
        try:
            self.wait.until(EC.presence_of_element_located(self.reset_username_locator)).send_keys(username)
            self.wait.until(EC.element_to_be_clickable(self.reset_button_locator)).click()
            print("[INFO] Password reset requested.")
        except TimeoutException:
            raise Exception("[ERROR] Reset password elements not found or not clickable within the timeout period.")

    def verify_success_message(self):
        """Verify the success message for password reset."""
        try:
            self.wait.until(EC.presence_of_element_located(self.success_message_locator))
            print("[INFO] Reset password link sent successfully.")
            return True
        except TimeoutException:
            print("[ERROR] Success message not displayed.")
            return False


# Test Case: Forgot Password Link Validation
def test_forgot_password():
    """Test case for validating the Forgot password functionality on the login page."""
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"

    # Browser options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

    try:
        # Launch the application
        driver.get(base_url)
        print("[INFO] Application launched.")

        # Initialize POM classes
        login_page = LoginPage(driver)

        # Click on Forgot password link
        login_page.click_forgot_password()

        # Reset password
        login_page.reset_password(username)

        # Verify success message
        if login_page.verify_success_message():
            print("[INFO] Test case passed: Reset password link sent successfully.")
        else:
            print("[ERROR] Test case failed: Success message not displayed.")

    except Exception as e:
        print(f"[ERROR] Test case execution failed: {str(e)}")

    finally:
        # Close browser
        driver.quit()
        print("[INFO] Browser closed.")


# Run the test
test_forgot_password()


"""
TestcaseID:TC_PIM_02
Test objective:
  Header validation on Admin page 
Precondition:
1.Launch URL and login as “Admin”
2.OrangeHRM 3.0 site launched on a compatible browser
Steps:
1.Go to Admin page and validate “Title of the page as OrangeHRM”
2.Validate below options are displaying on admin page
                 1.User management
                 2.Job
                3.Organizations
               4.Qualifications
               5.Nationalities
              6.Corporate banking
              7.Configuration

Expected Result:
The user should be able to see above mentioned Admin page headers on Admin page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


# Login Page POM
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        """Perform login action."""
        try:
            self.wait.until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
            self.wait.until(EC.presence_of_element_located(self.password_locator)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.login_button_locator)).click()
            print("[INFO] Login successful.")
        except TimeoutException:
            raise Exception("[ERROR] Login elements not found or not clickable within the timeout period.")


# Admin Page POM
class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.admin_tab_locator = (By.XPATH, "//span[text()='Admin']")
        self.page_title = "OrangeHRM"
        self.headers = {
            "User Management": (By.XPATH, "//span[text()='User Management']"),
            "Job": (By.XPATH, "//span[text()='Job']"),
            "Organizations": (By.XPATH, "//span[text()='Organization']"),
            "Qualifications": (By.XPATH, "//span[text()='Qualifications']"),
            "Nationalities": (By.XPATH, "//span[text()='Nationalities']"),
            "Corporate Banking": (By.XPATH, "//span[text()='Corporate Banking']"),
            "Configuration": (By.XPATH, "//span[text()='Configuration']"),
        }

    def navigate_to_admin_page(self):
        """Navigate to the Admin page."""
        try:
            self.wait.until(EC.element_to_be_clickable(self.admin_tab_locator)).click()
            print("[INFO] Navigated to the Admin page.")
        except TimeoutException:
            raise Exception("[ERROR] Admin tab not clickable within the timeout period.")

    def validate_page_title(self):
        """Validate the page title."""
        try:
            current_title = self.driver.title
            if current_title == self.page_title:
                print("[INFO] Page title validated successfully.")
                return True
            else:
                print(f"[ERROR] Page title mismatch. Expected: '{self.page_title}', Found: '{current_title}'")
                return False
        except Exception as e:
            raise Exception(f"[ERROR] Unexpected error while validating page title: {str(e)}")

    def validate_admin_headers(self):
        """Validate the headers on the Admin page."""
        missing_headers = []
        for header_name, header_locator in self.headers.items():
            try:
                self.wait.until(EC.presence_of_element_located(header_locator))
                print(f"[INFO] Header '{header_name}' is present.")
            except TimeoutException:
                print(f"[ERROR] Header '{header_name}' is missing.")
                missing_headers.append(header_name)
        return missing_headers


# Test Case: Validate Admin Page Headers
def test_admin_page_headers():
    """Test case for validating headers on the Admin page."""
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    # Browser options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

    try:
        # Launch the application
        driver.get(base_url)
        print("[INFO] Application launched.")

        # Initialize POM classes
        login_page = LoginPage(driver)
        admin_page = AdminPage(driver)

        # Perform login
        login_page.login(username, password)

        # Navigate to Admin page
        admin_page.navigate_to_admin_page()

        # Validate page title
        if not admin_page.validate_page_title():
            print("[ERROR] Test case failed: Page title mismatch.")
            return

        # Validate headers
        missing_headers = admin_page.validate_admin_headers()
        if not missing_headers:
            print("[INFO] Test case passed: All headers are present.")
        else:
            print(f"[ERROR] Test case failed: Missing headers - {', '.join(missing_headers)}")

    except Exception as e:
        print(f"[ERROR] Test case execution failed: {str(e)}")

    finally:
        # Close browser
        driver.quit()
        print("[INFO] Browser closed.")


# Run the test
test_admin_page_headers()

"""
TestcaseID:TC_PIM_03
Test objective:
  Main menu validation on Admin page 
Precondition:
1.Launch URL and login as “Admin”
2.OrangeHRM 3.0 site launched on a compatible browser
Steps:
             1.Go to admin Page
             2.Validate below “Menu options”(on side pane)displaying on Admin page

                 a.Admin
                 b.PIM
                 C.Time
                 d.Leave
                 e.Recruitment
                 f.My Info
                 g.Performance
                 h.Dashboard
                 i.Directory
                k.Maintainance
                l.Buzz

Ecpected Result: The user should able to see above mentioned Admin Page Menu items on Admin page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


# Login Page POM
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        """Perform login action."""
        try:
            self.wait.until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
            self.wait.until(EC.presence_of_element_located(self.password_locator)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.login_button_locator)).click()
            print("[INFO] Login successful.")
        except TimeoutException:
            raise Exception("[ERROR] Login elements not found or not clickable within the timeout period.")


# Admin Page POM
class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.admin_tab_locator = (By.XPATH, "//span[text()='Admin']")
        self.page_title = "OrangeHRM"
        self.menu_options = {
            "Admin": (By.XPATH, "//span[text()='Admin']"),
            "PIM": (By.XPATH, "//span[text()='PIM']"),
            "Time": (By.XPATH, "//span[text()='Time']"),
            "Leave": (By.XPATH, "//span[text()='Leave']"),
            "Recruitment": (By.XPATH, "//span[text()='Recruitment']"),
            "My Info": (By.XPATH, "//span[text()='My Info']"),
            "Performance": (By.XPATH, "//span[text()='Performance']"),
            "Dashboard": (By.XPATH, "//span[text()='Dashboard']"),
            "Directory": (By.XPATH, "//span[text()='Directory']"),
            "Maintenance": (By.XPATH, "//span[text()='Maintenance']"),
            "Buzz": (By.XPATH, "//span[text()='Buzz']")
        }

    def navigate_to_admin_page(self):
        """Navigate to the Admin page."""
        try:
            self.wait.until(EC.element_to_be_clickable(self.admin_tab_locator)).click()
            print("[INFO] Navigated to the Admin page.")
        except TimeoutException:
            raise Exception("[ERROR] Admin tab not clickable within the timeout period.")

    def validate_page_title(self):
        """Validate the page title."""
        try:
            current_title = self.driver.title
            if current_title == self.page_title:
                print("[INFO] Page title validated successfully.")
                return True
            else:
                print(f"[ERROR] Page title mismatch. Expected: '{self.page_title}', Found: '{current_title}'")
                return False
        except Exception as e:
            raise Exception(f"[ERROR] Unexpected error while validating page title: {str(e)}")

    def validate_menu_options(self):
        """Validate the menu options on the Admin page."""
        missing_menu_items = []
        for menu_name, menu_locator in self.menu_options.items():
            try:
                self.wait.until(EC.presence_of_element_located(menu_locator))
                print(f"[INFO] Menu item '{menu_name}' is present.")
            except TimeoutException:
                print(f"[ERROR] Menu item '{menu_name}' is missing.")
                missing_menu_items.append(menu_name)
        return missing_menu_items


# Test Case: Validate Main Menu on Admin Page
def test_admin_page_menu():
    """Test case for validating main menu options on Admin page."""
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    # Browser options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

    try:
        # Launch the application
        driver.get(base_url)
        print("[INFO] Application launched.")

        # Initialize POM classes
        login_page = LoginPage(driver)
        admin_page = AdminPage(driver)

        # Perform login
        login_page.login(username, password)

        # Navigate to Admin page
        admin_page.navigate_to_admin_page()

        # Validate page title
        if not admin_page.validate_page_title():
            print("[ERROR] Test case failed: Page title mismatch.")
            return

        # Validate menu options
        missing_menu_items = admin_page.validate_menu_options()
        if not missing_menu_items:
            print("[INFO] Test case passed: All menu items are present.")
        else:
            print(f"[ERROR] Test case failed: Missing menu items - {', '.join(missing_menu_items)}")

    except Exception as e:
        print(f"[ERROR] Test case execution failed: {str(e)}")

    finally:
        # Close browser
        driver.quit()
        print("[INFO] Browser closed.")


# Run the test
test_admin_page_menu()

import os
import time
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    # Setup
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()  # Maximize the browser window
    #driver.implicitly_wait(10)  # Set implicit wait of 10 seconds


    print("URL of the login page")
    login_url = "https://ablehrms.purestudy.com/"  # Replace with the actual URL of your login page

    # Open the login page
    driver.get(login_url)

    # Print the title of the page
    print("Page title is:", driver.title)

    # Optionally, you can assert the title if needed
    assert driver.title == "ECMS"

    print("Launch URL Successfully !!!")

    # Find and fill in the username field

    username_field = driver.find_element(By.ID, 'user_name')  # Adjust locator strategy as needed
    username_field.send_keys('1320')

    # Find and fill in the password field
    password_field = driver.find_element(By.ID, 'user_password')  # Adjust locator strategy as needed
    password_field.send_keys('Welcome@123')

    # Find and click the login button
    login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')  # Adjust locator strategy as needed
    login_button.click()

    # # Use explicit wait to assertion
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.NAME, "password"))
    # ).send_keys("your_password")
    time.sleep(4)
    # Optional: Check for successful login
    # For example, check if redirected to a dashboard or a specific page
    assert driver.current_url == 'https://ablehrms.purestudy.com/courses_dashboard'  # Adjust expected URL as needed

    # Or check for the presence of a specific element after login
    welcome_message = driver.find_element(By.XPATH, '//h3[normalize-space()="Courses Dashboard"]')  # Adjust locator strategy as needed
    assert welcome_message.is_displayed()

    print("User Login Successfully !!!")

    #-----------------------------------------------------------------------------------------

    #Return the WebDriver instance
    yield driver

    # Teardown
    driver.close()

    print("Test Cases --> Launch site - Login - Click to add course")
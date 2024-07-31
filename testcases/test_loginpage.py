# import time
# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
# @pytest.mark.order(2)
# def test_loginpage(driver):
#     # Find and fill in the username field
#
#     username_field = driver.find_element(By.ID, 'user_name')  # Adjust locator strategy as needed
#     username_field.send_keys('1320')
#
#     # Find and fill in the password field
#     password_field = driver.find_element(By.ID, 'user_password')  # Adjust locator strategy as needed
#     password_field.send_keys('Welcome@123')
#
#     # Find and click the login button
#     login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')  # Adjust locator strategy as needed
#     login_button.click()
#
#     # # Use explicit wait to assertion
#
#     time.sleep(3)
#     # Optional: Check for successful login
#     # For example, check if redirected to a dashboard or a specific page
#     assert driver.current_url == 'https://ablehrms.purestudy.com/courses_dashboard'  # Adjust expected URL as needed
#
#     # Or check for the presence of a specific element after login
#     welcome_message = driver.find_element(By.XPATH, '//h3[normalize-space()="Courses Dashboard"]')  # Adjust locator strategy as needed
#     assert welcome_message.is_displayed()

import time
from telnetlib import EC

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.order(3)
def test_addcourse(driver):
    #add course

    try:
        # Wait for the add course button to be present and click it
        add_course_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="fa fa-plus"]'))
        )
        add_course_button.click()

        print("Click to Add Course Button Successfully !!!")

    except TimeoutException:
        assert False, "The element was not found within the time limit"

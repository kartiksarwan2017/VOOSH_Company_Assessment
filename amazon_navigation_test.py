from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Function to set up the web driver
def setup_driver():
    driver = webdriver.Chrome()
    return driver
# Function to perform the navigation menu test
def test_navigation_menu(driver):
    driver.get("https://www.amazon.com")

    menu_items = [
        "Your Amazon",  # Modified link text to match the actual website
        "Today's Deals",
        "Gift Cards & Registry",
        "Customer Service",
        "Sell",
        "Registry",
        "Amazon's Response to COVID-19",
        "Home"
    ]

    for item in menu_items:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//*[text()='{item}']"))
            )
            assert element.is_displayed(), f"{item} not found in navigation menu."
            element.click()
            WebDriverWait(driver, 10).until(EC.url_changes)  # Wait for the page to load
            assert driver.current_url != "https://www.amazon.com", f"{item} link is not functioning correctly."
            driver.back()  # Go back to the homepage
        except NoSuchElementException:
            print(f"{item} not found in navigation menu.")
        except Exception as e:
            print(f"Error while testing {item}: {e}")

    driver.quit()


if __name__ == "__main__":
    driver = setup_driver()
    test_navigation_menu(driver)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

URL = "https://www.kimmoahola.net/selenium.html#"

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


def test_selenium_exercises(driver):
    driver.get(URL)

    # 1. Find element with ID `main-title` and print text
    main_title = driver.find_element(By.ID, "main-title")
    assert main_title.text != "", "main-title should have text"

    # 2. Locate paragraph with class `text-paragraph` and print text
    p = driver.find_element(By.CLASS_NAME, "text-paragraph")
    assert p.text != "", "text-paragraph should have text"

    # 3. Find input field with name `username` and enter text
    username = driver.find_element(By.NAME, "username")
    username.clear()
    username.send_keys("testuser")
    assert username.get_attribute("value") == "testuser"

    # 4. Check or uncheck the checkbox with name `check2`
    checkbox = driver.find_element(By.NAME, "check2")
    # toggle checkbox to checked state
    if not checkbox.is_selected():
        checkbox.click()
    assert checkbox.is_selected()

    # 5. Select the radio button with value `blue`
    radio_blue = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='blue']")
    radio_blue.click()
    assert radio_blue.is_selected()

    # 6. Choose "Option 3" from the dropdown with ID `dropdown`
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    # Try selecting by visible text or index
    try:
        dropdown.select_by_visible_text("Option 3")
    except Exception:
        dropdown.select_by_index(2)
    selected = dropdown.first_selected_option
    assert "Option 3" in selected.text

    # 7. Click the button with class `btn-class`
    btn = driver.find_element(By.CLASS_NAME, "btn-class")
    btn.click()

    # 8. Click the link with ID `link-id` and print its href attribute (without navigating)
    link = driver.find_element(By.ID, "link-id")
    href = link.get_attribute("href")
    assert href and href.startswith("http"), "link-id should have an absolute href"

    # 9. Get text from nested span with ID `nested-span` using a CSS selector
    nested = driver.find_element(By.CSS_SELECTOR, "#nested-span")
    assert nested.text != ""

    # 10. Find image with ID `image-id` and print its alt attribute
    img = driver.find_element(By.ID, "image-id")
    alt = img.get_attribute("alt")
    assert alt is not None

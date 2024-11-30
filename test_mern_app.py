from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the ChromeDriver
driver = webdriver.Chrome(executable_path='path_to_chromedriver')  # Replace with your ChromeDriver path

# Test Case 1: Check if the home page loads successfully
def test_home_page():
    driver.get("http://your-deployed-app-url.com")  # Replace with your app URL
    assert "Home" in driver.title, "Home page did not load properly"
    print("Test Case 1: Home page loaded successfully.")

# Test Case 2: Verify login functionality
def test_login():
    driver.get("http://your-deployed-app-url.com/login")  # Replace with your login page URL
    
    # Locate login fields and submit button
    username_input = driver.find_element(By.NAME, "username")  # Replace "username" with your field's name attribute
    password_input = driver.find_element(By.NAME, "password")  # Replace "password" with your field's name attribute
    login_button = driver.find_element(By.ID, "login-btn")  # Replace with your login button ID

    # Perform login
    username_input.send_keys("testuser")  # Replace with a valid test username
    password_input.send_keys("testpassword")  # Replace with a valid test password
    login_button.click()

    # Wait for the page to load
    time.sleep(3)

    # Verify successful login (e.g., by checking for a dashboard or user greeting)
    assert "Dashboard" in driver.page_source, "Login failed or Dashboard not found"
    print("Test Case 2: Login functionality works.")

# Run tests
try:
    test_home_page()
    test_login()
finally:
    driver.quit()

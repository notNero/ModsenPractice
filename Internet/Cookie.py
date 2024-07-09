from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Specify the path to your chromedriver
chromedriver_path = '/path/to/chromedriver'

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run browser in background mode (optional)
chrome_options.add_argument('--disable-gpu')

# Initialize the web driver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the web page
    driver.get('https://example.com')

    # Set a value in Cookies
    driver.add_cookie({'name': 'key', 'value': 'value'})

    # Get the value from Cookies
    cookie = driver.get_cookie('key')
    print(f"Value from Cookies: {cookie['value']}")

    # Remove the value from Cookies
    driver.delete_cookie('key')

    # Verify the removal of the value
    cookie_after_removal = driver.get_cookie('key')
    print(f"Value after removal: {cookie_after_removal}")

except Exception as err:
    print(f"Error: ", err)

finally:
    # Close the browser
    driver.quit()

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

    # Set a value in LocalStorage
    driver.execute_script("localStorage.setItem('key', 'value');")

    # Get the value from LocalStorage
    value = driver.execute_script("return localStorage.getItem('key');")
    print(f"Value from LocalStorage: {value}")

    # Remove the value from LocalStorage
    driver.execute_script("localStorage.removeItem('key');")

    # Verify the removal of the value
    value_after_removal = driver.execute_script("return localStorage.getItem('key');")
    print(f"Value after removal: {value_after_removal}")

except Exception as err:
    print(f"Error: ", err)

finally:
    # Close the browser
    driver.quit()

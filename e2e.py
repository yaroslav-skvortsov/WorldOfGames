from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Test function to check the score service
def test_scores_service(url):
    try:
        # Initialize the browser
        driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed
        driver.get(url)

        # Wait for the page to load
        time.sleep(2)

        # Find the score element
        score_element = driver.find_element(By.ID, "score")
        score_value = int(score_element.text)

        # Check if the score is between 1 and 1000
        if 1 <= score_value <= 1000:
            driver.quit()
            return True
        else:
            driver.quit()
            return False
    except Exception as e:
        print(f"Error during testing: {e}")
        driver.quit()
        return False

# Main function to call the test function and exit accordingly
def main_function():
    url = "http://localhost:80"  # Change to the URL of your Flask app
    result = test_scores_service(url)

    # Return -1 if the test fails, 0 if the test passes
    if result:
        print("Test Passed!")
        exit(0)
    else:
        print("Test Failed!")
        exit(-1)

if __name__ == "__main__":
    main_function()
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

def test_scores_service(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)

        driver.quit()
        return 1 <= score <= 1000

    except Exception as e:
        print(f"Error during test: {e}")
        return False


def main_function():
    test_result = test_scores_service("http://localhost:5000")
    if test_result:
        sys.exit(0)
    else:
        sys.exit(-1)

if __name__ == "_main_":
    main_function()
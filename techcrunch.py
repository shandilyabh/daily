"""
Script for scraping TechCrunch articles
"""

from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
import time

# Set up the WebDriver (Example: Chrome)
options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)  # Ensure chromedriver is in PATH

driver.get("https://techcrunch.com/category/startups/")
time.sleep(3)

posts_section = driver.find_element(By.CLASS_NAME, "wp-block-post-template")
if posts_section:
    posts = posts_section.find_elements(By.CLASS_NAME, "wp-block-post")
    for post in posts:
        print(post.text)
time.sleep(3)

driver.quit()
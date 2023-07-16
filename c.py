from selenium import webdriver
from selenium.webdriver.chrome.service import service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()

# Initialize a web driver to 
# control chrome
driver = webdriver.Firefox()

driver.fullscreen_window()

subreddit = {}

def scroll_down():
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(4)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height


time.sleep(5)
driver.get("https://www.reddit.com/r/Health/comments/13qqjru/is_organic_food_worth_the_cost/")
time.sleep(2)
scroll_down()
title = driver \
    .find_element(By.CSS_SELECTOR, "div#post-title-t3_13qqjru") \
        .text
all_times = driver \
    .find_elements(By.CSS_SELECTOR, "faceplate-timeago > time")
times = [each_post_time.get_attribute("datetime") for each_post_time in all_times]

posts = driver \
    .find_elements(By.CSS_SELECTOR, "div#-post-rtjson-content")
    
posts = [post.text for post in posts]

subreddit["texts"] = posts
subreddit["time"] = times

print(subreddit)
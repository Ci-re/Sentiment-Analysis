from selenium import webdriver
from selenium.webdriver.chrome.service import service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()

# Initialize a web driver to control chrome
driver = webdriver.Firefox()

driver.fullscreen_window()
driver.get("https://www.reddit.com/search/?q=organic+food&type=link&t=year")

data_testid = "post-title" 
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

scroll_down()

time.sleep(5)

links = driver \
    .find_elements(By.CSS_SELECTOR, "a[data-testid=post-title]")
    
#for link in links:
 #   print(link.get_attribute("href"))

web_links = [link.get_attribute("href") for link in links]
print(web_links)

def scrape_posts(url):
    time.sleep(5)
    driver.get(url)
    time.sleep(2)
    scroll_down()
    title = driver \
        .find_element(By.CSS_SELECTOR, "div#post-title-t3_13qqjru") \
            .text
    all_times = driver \
        .find_elements(By.CSS_SELECTOR, "faceplate-timeago > time")
    times = [each_post_time.get_attribute("datetime") for each_post_time in all_times]
    
    posts = driver \
        .find_elements(By.CSS_SELECTOR, "div#id=-post-rtjson-content") \
            .text
    post = list(posts)
    
    subreddit["texts"] = post
    subreddit["time"] = times
    
    return subreddit

subreddit = scrape_posts(web_links[0])
print(subreddit)

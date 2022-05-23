from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def crawler_js():
    url = "https://gesetze.berlin.de/bsbe/document/MWRE220005943"
    
    service = Service(executable_path=ChromeDriverManager().install())
    options = ChromeOptions()
    
    driver = webdriver.Chrome(service=service, options=options)

    # driver.quit()
  
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get(url)
    title = driver.title

    return title

print(crawler_js)

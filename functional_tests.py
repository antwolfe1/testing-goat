from selenium import webdriver

options = webdriver.ChromeOptions()

browser = webdriver.Chrome(options=options)
# browser.get('http://127.0.0.1:8000')
browser.get('http://localhost:8080')

assert "Congratulations" in browser.title
print("OK")
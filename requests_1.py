import requests
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func():
        t1 = time()
        result = func()
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

@timer_func
def webdrivertest():
    options=Options()
    options.add_argument('--headless')
    driver=webdriver.Chrome(chrome_options=options)
    driver.get('https://www.google.com/')
    driver.quit()

@timer_func
def request_speed():
    response = requests.get('https://www.google.com/')
    print (response.status_code)

request_speed()
webdrivertest()






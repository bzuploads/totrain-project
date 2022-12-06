import requests
from bs4 import BeautifulSoup
import os
from art import *
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--log-level=3")


PATH = (r'C:\Users\snoopy\Desktop\drivers\chromedriver.exe')


book_list = []
book_list_two = []

for x in range(1, 3):
    url = f'https://www.totrain.co.uk/product-category/e-learning/?product-page={x}'

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features="html5lib")

    div = soup.find_all('div', class_='wrap')

    for course in div:
        title = course.find(
            'h2', class_='woocommerce-loop-product__title').text
        price = course.find('bdi').text
        courses = {
            'Course': title,
            'Price': price
        }
        book_list.append(courses)

url = 'https://www.totrain.co.uk/product-category/online-training-courses/'
r = requests.get(url)

soup = BeautifulSoup(r.text, features="html5lib")

div = soup.find_all('div', class_='wrap')

for course in div:
    title = course.find(
        'h2', class_='woocommerce-loop-product__title').text
    price = course.find('bdi').text
    courses = {
        'Course': title,
        'Price': price
    }
    book_list_two.append(courses)


os.system('cls')

tprint('totrain')
print('By Braeden Haines')
print('\n')
print('[1] ' + 'e-learning courses')
print('[2] ' + 'online training courses')
print('\n')


one_or_two = input('Please choose a course list (1-2): ')
if one_or_two == '1':
    os.system('cls')
    count = 0
    for x in book_list:
        count += 1
        print(f'[{count}] ' + x.get('Course') + ' : ' +
              x.get('Price', ) + ' Plus VAT')

elif one_or_two == '2':
    os.system('cls')
    count = 0
    for x in book_list_two:
        count += 1
        print(f'[{count}] ' + x.get('Course') + ' : ' +
              x.get('Price', ) + ' Plus VAT')


course_choose = input('\nChoose a course (1-22): ')

if course_choose == '1' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/allergen-awareness/')
elif course_choose == '1' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/brcgs-site-conversion-course/')


if course_choose == '2' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/asbestos-awareness/')
elif course_choose == '2' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://www.totrain.co.uk/product/brcgs-auditing-2-day-conversion-course-issue-9/')


if course_choose == '3' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/coshh/')
elif course_choose == '3' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://www.totrain.co.uk/product/brcgs-environmental-monitoring-training/')


if course_choose == '4' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://www.totrain.co.uk/product/display-screen-equipment-assessment-dsea/')
elif course_choose == '4' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/brcgs-food-safety-culture/')


if course_choose == '5' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/equality-diversity/')
elif course_choose == '5' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/brcgs-internal-auditor-issue-9/')


if course_choose == '6' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/fire-safety-awareness/')
elif course_choose == '6' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://www.totrain.co.uk/product/brcgs-lead-auditor-course-issue-9/')


if course_choose == '7' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/gdpr/')
elif course_choose == '7' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://www.totrain.co.uk/product/brcgs-virtual-risk-assessment-course/')


if course_choose == '8' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/intro-to-fs/')
elif course_choose == '8' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/brcgs-root-cause-analysis/')


if course_choose == '9' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/labelling/')
elif course_choose == '9' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/virtual-food-sitetraining/')


if course_choose == '10' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/ladder-use/')
elif course_choose == '10' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://www.totrain.co.uk/product/brcgs-virtual-validation-verification/')


if course_choose == '11' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/level-2-food-safety/')
elif course_choose == '11' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/rsph-l3-food-safety/')


if course_choose == '12' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/level-2-food-safety-polish/')
elif course_choose == '12' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/rsph-l3-haccp-plan/')


if course_choose == '13' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/level-2-haccp/')
elif course_choose == '13' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/rsph-l4-managing-haccp/')


if course_choose == '14' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/level-2-health-safety/')
elif course_choose == '14' and one_or_two == '2':
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://www.totrain.co.uk/product/vulnerability-assessment-for-food-fraud/')


if course_choose == '15' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/management-supervisory/')
elif course_choose == '16' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/manual-handling/')
elif course_choose == '17' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/noise-awareness/')
elif course_choose == '18' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/pest-awareness/')
elif course_choose == '19' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/pest-awareness-polish/')
elif course_choose == '20' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/root-cause-analysis/')
elif course_choose == '21' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/working-at-height/')
elif course_choose == '22' and one_or_two == '1':
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.totrain.co.uk/product/working-from-home/')

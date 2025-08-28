import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# .env файл ачаалж хувьсагчид руу унших
load_dotenv()

USERNAME = os.getenv("USERNAME")   # .env доторх хэрэглэгчийн нэр
PASSWORD = os.getenv("PASSWORD")   # .env доторх нууц үг

# Chrome хөтөчийг ажиллуулах
driver = webdriver.Chrome()

# Алхам 1: Веб хуудсыг ачааллах
driver.get("https://student.must.edu.mn")

# Алхам 2: Нэвтрэх талбаруудыг олох
username = driver.find_element(By.ID, "username")   # хэрэглэгчийн нэрийн талбар
password = driver.find_element(By.ID, "password")   # нууц үгийн талбар

# Алхам 3: Нэвтрэх үйлдэл хийх
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)

# Нэвтэрсний дараа гарч ирэх popup-д зориулж жаахан хүлээх
time.sleep(3)

# ESC дарж popup-ыг хаах
actions = ActionChains(driver)
actions.send_keys(Keys.ESCAPE).perform()

# Хуудас бүрэн ачаалагдахыг дахин бага зэрэг хүлээх
time.sleep(3)

# Алхам 4: Assertion буюу үр дүн шалгах
try:
    # "Оюутны товч мэдээлэл" гэсэн текст бүхий элемент байгаа эсэхийг шалгана
    profile_link = driver.find_element(By.XPATH, "//*[contains(text(), 'Оюутны товч мэдээлэл')]")
    assert profile_link.is_displayed()
    print("✅ Нэвтрэх тест амжилттай")
except:
    print("❌ Нэвтрэх тест амжилтгүй")

# Алхам 5: Logout хийх ба хөтөчийг хаах
try:
    logout = driver.find_element(By.LINK_TEXT, "Гарах")
    logout.click()
except:
    print("⚠ Logout товч олдсонгүй")

# Хөтөчийг бүрэн хаах
driver.quit()

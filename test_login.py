import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# .env файл ачаалж хувьсагчид руу унших
load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Chrome хөтөчийг ажиллуулах
driver = webdriver.Chrome()
driver.maximize_window()

# Алхам 1: Веб хуудсыг ачааллах
driver.get("https://student.must.edu.mn")

# Алхам 2: Нэвтрэх талбаруудыг олох
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

# Алхам 3: Нэвтрэх үйлдэл хийх
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)

# Popup гарах магадлалтай тул ESC дарна
time.sleep(2)
actions = ActionChains(driver)
actions.send_keys(Keys.ESCAPE).perform()

wait = WebDriverWait(driver, 10)

# Алхам 4: "ОЮУТАН" dropdown товчийг дарах
try:
    student_dropdown = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='ОЮУТАН']"))
    )
    student_dropdown.click()
    print("✅ 'ОЮУТАН' dropdown амжилттай дарагдлаа")
except:
    print("❌ 'ОЮУТАН' dropdown олдсонгүй")
    
time.sleep(2)

# Алхам 5: Dropdown дотроос "Хувийн мэдээлэл" цэсийг дарах
try:
    profile_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='Хувийн мэдээлэл']"))
    )
    profile_menu.click()
    print("✅ 'Хувийн мэдээлэл' цэсийг амжилттай нээлээ")
except:
    print("❌ 'Хувийн мэдээлэл' цэсийг олсонгүй")
    
time.sleep(2)

# Алхам 6: Хуудас дотор "Мэдээлэл, холбооны технологийн сургууль" текст байгаа эсэхийг шалгах
try:
    faculty_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Мэдээлэл, холбооны технологийн сургууль')]")
        )
    )
    assert faculty_text.is_displayed()
    print("✅ Хувийн мэдээлэл хуудсан дээр зөв текст илэрлээ")
except:
    print("❌ Хувийн мэдээлэл хуудсан дээр текст илрээгүй")
    
time.sleep(2)

# Алхам 7: "ХИЧЭЭЛ" dropdown товчийг дарах
try:
    lessons_dropdown = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='ХИЧЭЭЛ']"))
    )
    lessons_dropdown.click()
    print("✅ 'ХИЧЭЭЛ' dropdown амжилттай дарагдлаа")
except:
    print("❌ 'ХИЧЭЭЛ' dropdown олдсонгүй")

time.sleep(2)

# Алхам 8: Dropdown дотроос "Хичээлийн хуваарь хэвлэх" цэсийг дарах
try:
    schedule_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='Хичээлийн хуваарь хэвлэх']"))
    )
    schedule_menu.click()
    print("✅ 'Хичээлийн хуваарь хэвлэх' цэсийг амжилттай нээлээ")
except:
    print("❌ 'Хичээлийн хуваарь хэвлэх' цэсийг олсонгүй")

time.sleep(2)

# Алхам 9: Хуудас дотор "Нийт сонгосон кредит" текст байгаа эсэхийг шалгах
try:
    credit_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Нийт сонгосон кредит')]")
        )
    )
    assert credit_text.is_displayed()
    print("✅ Хичээлийн хуваарь дээр 'Нийт сонгосон кредит' текст илэрлээ")
except:
    print("❌ 'Нийт сонгосон кредит' текст илрээгүй")

time.sleep(2)


# Алхам 7: Logout хийх
try:
    logout = driver.find_element(By.LINK_TEXT, "Гарах")
    logout.click()
    print("✅ Гарах товч дарж амжилттай logout хийлээ")
except:
    print("⚠ Logout товч олдсонгүй")

# Хөтөчийг хаах
driver.quit()

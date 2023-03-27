import os, sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = "ariel7234"
password = "Letscreate2gether!"
repo_name = os.environ["DIR"]

driver = webdriver.Chrome()

driver.get("https://github.com/login")
driver.find_element(by=By.ID, value="login_field").send_keys(username)
driver.find_element(by=By.ID, value="password").send_keys(password)
driver.find_element(by=By.NAME, value="commit").click()
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."

errors = driver.find_elements(by=By.CLASS_NAME, value="flash-error")

for e in errors:
    print(e.text)

if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

button_xpath = '//*[@id="repos-container"]/h2/a'
button = (
    WebDriverWait(driver, 10)
    .until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    .click()
)

driver.find_element(by=By.XPATH, value='//*[@id="repository_name"]').send_keys(repo_name)

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "The repository already exists on this account"

errors = driver.find_element(by=By.ID, value="input-check-4622")

for e in errors:
    print(e.text)

if any(error_message in e.text for e in errors):
    print("[!] Repo name is already exist")
else:
    print("[+] Repo name is available")


btn_new_xpath = '//*[@id="new_repository"]/div[6]/button'
btn_new = (
    WebDriverWait(driver, 10)
    .until(EC.element_to_be_clickable((By.XPATH, btn_new_xpath)))
    .send_keys(Keys.ENTER)
)

remoteUrl_xpath = '//*[@id="empty-setup-push-repo-echo"]/span[1]/span'
remote_url = (
    WebDriverWait(driver, 10)
    .until(EC.visibility_of_element_located((By.XPATH, remoteUrl_xpath)))
    .text
)

print(remote_url)

exit(remote_url)
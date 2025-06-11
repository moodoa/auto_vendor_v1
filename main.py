from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def wait_and_click(driver, wait, xpath):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def wait_for_presence(driver, wait, by, selector):
    return wait.until(EC.presence_of_element_located((by, selector)))

def save_screenshot(driver, path):
    dir_path = os.path.dirname(path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    driver.save_screenshot(path)


def main():
    driver = setup_driver()
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://www.cathay-cube.com.tw/cathaybk")
        wait_for_presence(driver, wait, By.CSS_SELECTOR, "h1.text-center.font-bold")
        time.sleep(2)
        save_screenshot(driver, "home.png")

        wait_and_click(driver, wait, '//*[@id="spa-root"]/div/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/header/div/div[2]/div/div[2]/div/div[1]/div[1]/div')
        wait_and_click(driver, wait, '//*[@id="spa-root"]/div/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/header/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/a[1]')

        wait_and_click(driver, wait, "/html/body/div/main/article/div/div/div/div[1]/div/div/a[6]")
        time.sleep(2)

        container = wait_for_presence(driver, wait, By.XPATH, "/html/body/div/main/article/section[6]/div/div[2]/div/div[2]")
        spans = container.find_elements(By.TAG_NAME, "span")

        for i, span in enumerate(spans, start=1):
            try:
                span.click()
                time.sleep(1)
                save_screenshot(driver, f"stopcard_screenshots/page_{i}.png")
            except Exception as e:
                print(f"點擊第 {i} 個 span 失敗: {e}")

        wait_and_click(driver, wait, '//*[@id="lnk_ButtonLink"]')
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])

        wait_and_click(driver, wait, '//*[@id="layout_0_content_0_rptSlider_hlkSliderItem_1"]')

        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//li[starts-with(@id, "layout_0_content_0_rptCardList_htmlCardsBox_") and @style="display: list-item;"]')))
        card_items = driver.find_elements(By.XPATH, '//li[starts-with(@id, "layout_0_content_0_rptCardList_htmlCardsBox_") and @style="display: list-item;"]')

        for idx, card in enumerate(card_items):
            driver.execute_script("arguments[0].scrollIntoView(true);", card)
            time.sleep(1)
            os.makedirs("card_screenshots", exist_ok=True)
            card.screenshot(f"card_screenshots/card_{idx + 1}.png")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

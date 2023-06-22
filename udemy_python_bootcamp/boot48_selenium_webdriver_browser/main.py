from selenium import webdriver
from selenium.webdriver.common.by import By



url = "https://www.fjellsport.no/turutstyr/klatreutstyr/sikringer/kamkiler/black-diamond-camalot-ultralight-4"

#chrome_executable_path = 'C:\Users\G020772\development\chromedriver'
#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
driver = webdriver.Chrome() #executable_path=chrome_driver_path)

driver.get(url)
price = driver.find_element(By.CLASS_NAME, "q as av")
print(price.text)

# driver.close()
# driver.quit()

# too many technical difficulties. Not very relevant atm. Skips ahead to boot54.
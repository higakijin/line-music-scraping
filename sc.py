from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time


options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
#options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#ラブライブ情報の取得
driver.implicitly_wait(10)
URL = "https://yoshipc.net/blog/lovelive-sunshine-songs-list/"
driver.get(URL)

list = []
print(list)

i = 1
while i <= 123:
  song = driver.find_element_by_xpath('/html/body/div/div/div/div/div/section/div[2]/article/div/div[2]/div[1]/div/table/tbody/tr[' + str(i) + ']/td[1]').text
  list.append(song)
  i += 1

print(len(list))

# /html/body/div/div/div/div/div/section/div[2]/article/div/div[2]/div[1]/div/table/tbody/tr[1]/td[1]
# /html/body/div/div/div/div/div/section/div[2]/article/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]

# /html/body/div/div/div/div/div/section/div[2]/article/div/div[2]/div[1]/div/table/tbody/tr[123]/td[1]


#linemusicのログイン
driver.implicitly_wait(10)
URL = "https://music.line.me/webapp/today"
driver.get(URL)

element = driver.find_element_by_class_name('profile_area')
element.click()

email = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/form/fieldset/div[1]/input')
email.send_keys('hm385.chejptks@gmail.com')

password = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/form/fieldset/div[2]/input')
password.send_keys('19f572b8cc')

time.sleep(3)

button = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/form/fieldset/div[3]/button')
button.click()

#検索の開始
glass = driver.find_element_by_class_name('btn_search')
glass.click()

j = 104
while j < 123:
  search = driver.find_element_by_xpath('/html/body/div[1]/div/header/div/div[1]/span/input')
  search.send_keys(list[j])
  time.sleep(5)
  search.send_keys(Keys.ENTER)
  print('検索開始')
  time.sleep(5)

  detail = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div/a')
  detail.click()

  try:
    print('詳細をクリック')
    time.sleep(5)

    add = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div/div/a[2]')
    add.click()
    print('マイプレイリストに追加')
    time.sleep(5)

    playlist = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/a[2]')
    playlist.click()
    print('プレイリスト　Aqoursを選択')
    time.sleep(5)

    confirm = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/a')
    confirm.click()
    print(list[j] + " が追加されました。")

  except:
    print(list[j] + " は失敗した")

  search.clear()
  time.sleep(5)
  print("フォームをクリア")
  print("   ")
  j += 1
# 参考: https://www.usapippi-web.com/programming/141/

# webdriverのインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# sleepメソッドのインポート
from time import sleep

# webdriver managerのインポート
from webdriver_manager.chrome import ChromeDriverManager

import requests


#必要な変数を設定
#取得したトークン
TOKEN = 'ここにAPIトークンを入力'
#APIのURL
api_url = 'https://notify-api.line.me/api/notify'
#通知内容１
send_content_01 = 'ここに商品名を入力 はまだ入荷待ちだよ。'
send_content_02 = 'ここに商品名を入力 が再入荷したよ。購入はこちら→ここに商品ページのURLを入力'

#情報を辞書型にする
TOKEN_dic = {'Authorization':'Bearer' + ' ' + TOKEN}
send_dic_01 = {'message': send_content_01}
send_dic_02 = {'message': send_content_02}

# ブラウザーを起動(ブラウザは非表示にするヘッドレス)
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

# 商品ページにアクセス
sleep(1)
driver.get('ここに商品ページのURLを入力')

# 入荷待ちのときの処理と在庫ありのときの処理
if len(driver.find_elements_by_class_name('attention')) > 0 and driver.find_elements_by_class_name('attention')[0].text == 'SOLD OUT':
    requests.post(api_url,headers=TOKEN_dic,data=send_dic_01)
else:
    requests.post(api_url,headers=TOKEN_dic,data=send_dic_02)

# ブラウザーを終了
driver.quit()
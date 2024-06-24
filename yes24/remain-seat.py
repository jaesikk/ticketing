import random

import datetime
import winsound
import time
import requests
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import scrolledtext


# print('@@ log @@ remain_seat 작동')
def yes24_remain_post():
    url = "http://m.ticket.yes24.com/OSIF/Book.asmx/GetBookWhole"

    # POST 요청에 포함될 데이터
    data = {
        "idHall": 11977,
        "idTime": 1290631,
        "block": 0,
        "channel": 16,
        "idCustomer": 15201765,
        "idOrg": 1
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        xml_data = response.text
        # print(xml_data)

        root = ET.fromstring(xml_data)
        block_remain_data = root.find('.//{http://tempuri.org/}BlockRemain').text

        block_remain_items = block_remain_data.split('^')
        # print('block_remain_items >> ', block_remain_items)
        result = {}
        for item in block_remain_items:
            if '@' in item:
                key, value = item.split('@')
                result[key] = value

        # print('---------- xml-data : result --------------')
        # print(result)
        #  result
        # dummy result
        # result = {'29': '0', '15': '0', '9': '0', '32': '1', '12': '0', '35': '0', '30': '0', '10': '0', '13': '0',
        #           '33': '0', '16': '0', '102': '0', '31': '1', '34': '0', '11': '0', '1036': '0', '28': '0', '14': '0',
        #           '1027': '0'}
        ans = {}
        for key, value in result.items():
            if value != '0':
                winsound.Beep(880, 500)
                print(f'{key}블록 {value}석 발견')
                ans[key] = value
                res = f'{key}블록 {value}석 발견'
        if ans:
            return ans, False

        now = datetime.datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        txt = f'{formatted_now} - 조회중'
        print(txt)
        return txt, True # {key블록 : valeu석} 조회중
    else:
        # 실패한 경우
        print('--------- x post fail x ----------')
        print(response.text)
        err = response.text
        return err, False


# res = {'29': '0', '15': '1', '9': '0', '32': '0', '12': '0', '35': '1', '30': '0', '10': '0', '13': '0', '33': '0', '16': '0', '102': '0', '31': '0', '34': '0', '11': '0', '1036': '0', '28': '0', '14': '0', '1027': '0'}
#
# for k, v in res.items():
#     if int(v) > 0:
#         winsound.Beep(880, 500)  # 880Hz의 주파수로 0.5초 동안 재생
#         print(k, v)
def on_button_click():
    flag = True
    try:
        while flag == True:
            result, flag = yes24_remain_post()
            print('tkitner res >> ',result)
            text_console.insert(tk.END, str(result) + '\n')
            text_console.see(tk.END)  # 항상 마지막에 추가된 내용을 보이게 함
            root.update()
            time.sleep(random.randint(1,3))
    except KeyboardInterrupt:
        result = "\nKeyboardInterrupt : 프로그램을 종료합니다."
        text_console.insert(tk.END, result + '\n')
        text_console.see(tk.END)  # 항상 마지막에 추가된 내용을 보이게 함


root = tk.Tk()
root.title("Yes24 잔여 좌석 조회")
root.geometry("500x300")

button = tk.Button(root, text="잔여좌석조회", command=on_button_click)
button.pack(pady=10)

text_console = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
text_console.pack(pady=10)

root.mainloop()

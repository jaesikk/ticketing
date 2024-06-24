# 45482

import threading
from tkinter import *

from info import set_info
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, requests
import xml.etree.ElementTree as ET

class App(threading.Thread):
    def __init__(self):
        print('@@@@@@@@@@@@@@@@@@@ @@@@@@@ @@@@@@ @@@@@@@@ @@@@@@@@ @@@@@@@@@ @@@@@@@@@@@@@@')
        super().__init__()
        self.opt = webdriver.ChromeOptions()
        self.opt.add_argument('window-size=800,600')
        # webdriver_manager를 사용하여 ChromeDriver 자동 관리
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        # self.driver = webdriver.Chrome("chromedriver", options=self.opt)
        self.wait = WebDriverWait(self.driver, 10)
        self.url = 'https://id.payco.com/oauth2.0/authorize?serviceProviderCode=TKLINK&scope=&response_type=code&state=7a8804402f1449169f02112fb0e2a83d&client_id=Z9Ur2WLH9rB59Gy4_cJ3&redirect_uri=https://www.ticketlink.co.kr/auth/callback?selfRedirect=N&userLocale=ko_KR'
        # self.url = "https://www.ticketlink.co.kr/home"
        self.driver.get(self.url)

        data = set_info()

        # tkinter
        self.dp = Tk()
        self.dp.geometry("500x500")
        self.dp.title("tikcet-link 티케팅 프로그램")
        self.object_frame = Frame(self.dp)
        self.object_frame.pack()

        # ID 라벨 및 입력창
        self.id_label = Label(self.object_frame, text="ID")
        self.id_label.grid(row=1, column=0)
        self.id_entry = Entry(self.object_frame, width=20)
        self.id_entry.grid(row=1, column=1)
        self.id_entry.insert(0, data.get('id', ''))  # data['id'] 값 설정

        # PASSWORD 라벨 및 입력창
        self.pw_label = Label(self.object_frame, text="PASSWORD")
        self.pw_label.grid(row=1, column=2)
        self.pw_entry = Entry(self.object_frame, show='*', width=20)
        self.pw_entry.grid(row=1, column=3)
        self.pw_entry.insert(0, data.get('pw', ''))  # data['pw'] 값 설정

        # BIRTH 라벨 및 입력창
        self.birth_label = Label(self.object_frame, text="BIRTH")
        self.birth_label.grid(row=1, column=4)
        self.birth_entry = Entry(self.object_frame, width=20)
        self.birth_entry.grid(row=1, column=5)
        self.birth_entry.insert(0, data.get('birth', ''))  # data['birth'] 값 설정
        self.login_button = Button(self.object_frame, text="Login", width=3, height=2, command=self.login)
        self.login_button.grid(row=3, column=1)

        self.showcode_label = Label(self.object_frame, text="공연번호")
        self.showcode_label.grid(row=4, column=0)
        self.showcode_entry = Entry(self.object_frame, width=40)
        self.showcode_entry.grid(row=4, column=1)
        self.showcode_button = Button(self.object_frame, text="직링", width=3, height=2, command=self.link_go)
        self.showcode_button.grid(row=5, column=1)
        self.ticketing_button = Button(self.object_frame, text="예매하기", width=5, height=2, command=self.ticketing)
        self.ticketing_button.grid(row=6, column=1)

        self.date_label = Label(self.object_frame, text="YYYY-MM-DD")
        self.date_label.grid(row=7, column=0)
        self.date_entry = Entry(self.object_frame, width=40)
        self.date_entry.grid(row=7, column=1)
        self.date_button = Button(self.object_frame, text="날짜 고르기", width=10, height=2, command=self.select_date)
        self.date_button.grid(row=8, column=1)

        self.time_label = Label(self.object_frame, text="HH시 mm분")
        self.time_label.grid(row=9, column=0)
        self.time_entry = Entry(self.object_frame, width=40)
        self.time_entry.grid(row=9, column=1)
        self.time_button = Button(self.object_frame, text="시간 고르기", width=10, height=2, command=self.select_time)
        self.time_button.grid(row=10, column=1)

        # self.seat_label = Label(self.object_frame, text="자리 수")
        # self.seat_label.grid(row=11, column=0)
        # self.seat_entry = Entry(self.object_frame, width=40)
        # self.seat_entry.grid(row=11, column=1)

        self.section_button = Button(self.object_frame, text="섹션 선택", width=10, height=2, command=self.select_section)
        self.section_button.grid(row=11, column=1)

        self.back_button = Button(self.object_frame, text="뒤로 가기", width=10, height=2, command=self.go_back)
        self.back_button.grid(row=12, column=1)

        self.seat_button = Button(self.object_frame, text="좌석 잡기", width=10, height=2, command=self.select_seat)
        self.seat_button.grid(row=13, column=1)

        self.seat_button = Button(self.object_frame, text="원스텝", width=10, height=2, command=self.non_stop)
        self.seat_button.grid(row=14, column=1)

        self.seat_button = Button(self.object_frame, text="잔여좌석조회", width=10, height=2, command=self.remain_seat)
        self.seat_button.grid(row=15, column=1)
        self.dp.mainloop()

    # 로그인 하기
    def login(self):
        def task():
            # login_btn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/header/div[1]/div/div[2]/ul/li[1]/a')
            # login_btn.click()
            # print('--------------- modal test 111 -----------')
            # # 모달 창이 열릴 때까지 대기 (예시로 id 입력 필드가 보일 때까지 대기)
            # WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, '//*[@id="id"]'))
            # )
            # print('--------------- modal test 222 -----------')
            id_input = self.driver.find_element(By.XPATH, '//*[@id="id"]')
            id_input.send_keys(self.id_entry.get())

            pw_input = self.driver.find_element(By.XPATH, '//*[@id="pw"]')
            pw_input.send_keys(self.pw_entry.get())

            login_confirm =  self.driver.find_element(By.XPATH,'//*[@id="loginBtn"]')
            login_confirm.click()

            # 생년월일 입력 필드가 보일 때까지 대기
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="birthday"]'))
            )

            birth_input = self.driver.find_element(By.XPATH, '//*[@id="birthday"]')
            birth_input.send_keys('19960627')

            birth_confirm = self.driver.find_element(By.XPATH, '//*[@id="confirmBtn"]')
            birth_confirm.click()


        newthread = threading.Thread(target=task)
        newthread.start()

    # 직링 바로가기
    def link_go(self):
        def task():
            # sample : 49733
            '''
                1. ticket_link_url :
                > https://www.ticketlink.co.kr/reserve/plan/schedule/588549418?menuIndex=reserve
                2. self.showcode_entry.get() :
                > 588549418
            '''
            showcode = self.showcode_entry.get()
            showcode_url = f'https://www.ticketlink.co.kr/reserve/plan/schedule/{showcode}?menuIndex=reserve'
            self.driver.get(f'{showcode_url}')

        newthread = threading.Thread(target=task)
        newthread.start()

    def ticketing(self):
        def task():
            self.driver.execute_script("jsf_pdi_GoPerfSale(1);")
        newthread = threading.Thread(target=task)
        newthread.start()

    def select_date(self):
        def task():
            print('@@ log @@ self.select_date().get() >>>> ', self.date_entry.get() )
            date_element = self.driver.find_element(By.XPATH, f'//a[@title="{self.date_entry.get()}"]')
            date_element.click()
        newthread = threading.Thread(target=task)
        newthread.start()

    def select_time(self):
        def task():
            print('@@ log @@ self.select_time().get() >>>> ', self.time_entry.get())
            time_slot_element = self.driver.find_element(By.XPATH, f'//span[contains(text(),"{self.time_entry.get()}")]')
            time_slot_element.click()
            time.sleep(2)
        newthread = threading.Thread(target=task)
        newthread.start()

    def select_seat(self):
        def task():
            print('@@ log @@ >>> select_seat')
            #TODO 잘 되는지 체크할 것
            s6_elements = self.driver.find_elements(By.XPATH, '//div[@id="divSeatArray"]//div[contains(@class, "s6")]')

            for element in s6_elements[:2]:
                # 요소 클릭
                element.click()
                print('@@ log @@  >>>>>>>>>> 클릭 완료')
        newthread = threading.Thread(target=task)
        newthread.start()

    def go_back(self):
        def task():
            element = self.driver.find_element(By.XPATH, '//*[@id="StepCtrlStep02_02"]/div[1]/div/a')
            element.click()
        newthread = threading.Thread(target=task)
        newthread.start()

    def select_section(self):
        def task():
            element = self.driver.find_element(By.XPATH, '//*[@id="area0"]')
            element.click()
        newthread = threading.Thread(target=task)
        newthread.start()

    def non_stop(self):
        def task():
            self.link_go
            self.ticketing
            self.select_date
            self.select_time
            #TODO select_section() # 개발해야함
            #select_seat()
        newthread = threading.Thread(target=task)
        newthread.start()

    def remain_seat(self):
        def task():
            print('@@ log @@ remain_seat 작동')
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
                print('--------- post success ----------')
                xml_data = response.text
                print(xml_data)

                root = ET.fromstring(xml_data)

                block_remain_data = root.find('.//{http://tempuri.org/}BlockRemain').text

                block_remain_items = block_remain_data.split('^')

                print('block_remain_items >> ', block_remain_items)
                result = {}

                for item in block_remain_items:
                    if '@' in item:
                        key, value = item.split('@')
                        result[key] = value

                print('---------- xml-data : result --------------')
                print(result)
                for key, value in result.items():
                    if value != '0':
                        print(f"Key: {key}, Value: {value}")

            else:
                print('--------- post fail ----------')
                print(response.text)

        newthread = threading.Thread(target=task)
        newthread.start()

app = App()
app.start()

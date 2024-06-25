import pprint
import random
import requests
import time
from headers import get_headers
import winsound

"""
    이건 잘됨
"""

def get_remain(showcode, num, set_price):
    # section
    url1 = f"https://www.ticketlink.co.kr/api/V2/plan/schedules/{showcode}/grades?_={num}"
    params1 = {"_": num}
    # block
    url2 = f"https://www.ticketlink.co.kr/api/V2/plan/schedules/{showcode}/blocks/grades?_={num+1}"
    params2 = {"_": num+1}
    #######################################
    headers = get_headers()

    response1 = requests.get(url1, headers=headers, params=params1)

    response2 = requests.get(url2, headers=headers, params=params2)

    if response1.status_code == 200:
        res = response1.json()
        # print(res)
        # pprint.pprint(res['data'])
        connect = []
        for item in res['data']:
            if item['remainCnt'] > 0\
                    and item['price'] > set_price:
                connect.append({
                    'gradeId': item['gradeId'],
                    'name': item['name']
                })
                pprint.pprint({
                    'gradeId': item['gradeId'],
                    'name': item['name'],
                    'price': item['price'],
                    'remainCnt': item['remainCnt']
                })
    else:
        print('[Error] request1 is not 200.')
    # print('-------------------------  DETAIL -------------------------')
    # 실제 블럭과 blockId 차 를 구하기 위함
    # -gap으로 사용
    gap = 121431 - 402

    if response2.status_code == 200:
        res = response2.json()
        sorted_items = []

        for item in res['data']:
            for c in connect:
                if item['gradeId'] == c['gradeId'] and item['remainCnt'] > 0:
                    winsound.Beep(1000, 300)
                    if item['remainCnt'] > 2:
                        winsound.Beep(1000, 200)
                        winsound.Beep(1000, 200)
                        winsound.Beep(1000, 200)
                    sorted_items.append({
                        'blockId': item['blockId'],
                        # '> 예상블록': item['blockId'] - gap,
                        'name': c['name'],
                        # 'gradeId': item['gradeId'],
                        '잔여석': item['remainCnt']
                    })

        # name으로 정렬
        sorted_by_name = sorted(sorted_items, key=lambda x: x['name'])

        pprint.pprint(sorted_by_name)
    # print('=====================================================================')
    return(sorted_by_name)


if __name__=='__main__':
    #################  input  ######################
    showcode = '390792163'
    num = 1719279116197  # showcode 고유 넘버
    set_price = 27000
    ####################################### 꿀이소리석 28000이상부터 최강야구
    cnt = 10
    while True:
        get_remain(showcode, num, set_price)
        print('=====================================================================')
        time.sleep(random.uniform(0.5,1.3))
        if cnt//10 ==0:
            time.sleep(2)
import pprint
import random
import requests
import time
from headers import get_headers

def remain_seat(blockId):
    url = 'https://www.ticketlink.co.kr/api/V2/plan/1259310931/seat-all/canverse/block2'
    headers = get_headers()
    params = blockId

    res = requests.post(url, headers=headers, params=params)

    print(res.text)


if __name__=='__main__':
    blockId = '121385'
    remain_seat(blockId)
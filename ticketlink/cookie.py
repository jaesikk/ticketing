import requests
import time


def get_cookies(url):
    s = requests.session()
    print(f'---------- 1')
    try:
        response = s.get(url)
        response.raise_for_status()

        cookies = s.cookies.get_dict()

        if not cookies:  # 쿠키가 비어있거나 None인 경우
            print("쿠키 오류. url로 정상 접속 후 재시도해주세요.")
            time.sleep(2)
            raise ValueError("쿠키 오류. url로 정상 접속 후 재시도해주세요.")
        print('cookie dict >> ',cookies)
        cookie_str = '; '.join([f"{key}={value}" for key, value in cookies.items()])
        # print(cookie_str)
        print(f'---------- 쿠키 완료')
        print('cokie str >>',cookie_str)
        return cookies

    except requests.exceptions.RequestException as e:
        print(f"HTTP 요청 오류: \n {e}")
        time.sleep(2)
        raise

    except ValueError as ve:
        print(f"값 오류: \n {ve}")
        time.sleep(2)
        raise
    
if __name__ == '__main__':
    url = 'https://www.ticketlink.co.kr/reserve/plan/schedule/1259310931?menuIndex=reserve'
    get_cookies(url)
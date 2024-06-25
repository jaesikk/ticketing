import requests
from bs4 import BeautifulSoup

"""
    get : 메인 이벤트
    response : 별거 없음
"""

url = "https://www.ticketlink.co.kr/sports/baseball/event/470"

# GET 요청을 보냅니다.
response = requests.get(url)

# 응답 상태 코드 출력 (200이면 성공)
print(f"Response Status Code: {response.status_code}")

print(response.text)
# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# # 예시: 특정 요소를 찾기 (여기서는 <title> 태그를 찾습니다)
# title = soup.find('title').get_text()
# print(f"Page Title: {title}")


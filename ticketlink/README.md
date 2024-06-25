# ticket-link

## reserve_page

url : `https://www.ticketlink.co.kr/reserve/plan/schedule/588549418?menuIndex=reserve`

```
https://www.ticketlink.co.kr/reserve/plan/schedule/{공연번호}?menuIndex=reserve
```



---

## date

- 날짜/회차 : list형식 또는 string 대입
  - string 대입 우선 시도 후, list로 ㄱㄱ

---

## section

- section_value
- find_section()
  - section들어가지 않고도 remain_seat 확인 가능한지

---

## seat

- seat_value
- find_seat()
- select_seat()
  - 연석 =>
    연석 실패시 =>

----

## ticket_type, sale





---

## delivery, confirm



---

## payment

- 무통장
- check_agreement


---
# TIP
## 공연번호 얻기
해당 예매 링크 개발자 콘솔에서 elements 보면 scheduleid 확인 가능



## 팝업 정보

예매하기 버튼이 IMG 내에 있어서 elements 파악이 어려움



### 비정상적 접근 시 URL

```
https://tketlink.dn.toastoven.net/ticketlink-cdn/error_wait.html?channel=TKL_WEB
```

:bulb: toast 라는 곳에서 ban을 한다느 힌트를 얻음

---

### 예약 팝업 예시 화면

![팝업 예시 화면](C:\Users\Administrator\Desktop\jasic\git\ticketing\ticketlink\asset\팝업 예시 화면.jpg)

---

### 팝업 클릭 방법 찾은듯

:bulb: :bulb: :bulb: 

![메인 이벤트 화면](C:\Users\Administrator\Desktop\jasic\git\ticketing\ticketlink\asset\메인 이벤트 화면.jpg)

위에가 예매, 아래가 굿즈



#### schedulid 말고 product도 있는걸 볼 수 있따.

```
scheduleid="390792163"
productid="50726"
target="_blank"

전체
<area shape="rect" coords="255,1962,488,2026" href="#" target="_blank" scheduleid="390792163" productid="50726">
```



### 팝업 화면

parent-url : `https://www.ticketlink.co.kr/sports/baseball/event/470`

url : `https://www.ticketlink.co.kr/reserve/plan/schedule/390792163?menuIndex=reserve`



---

### 자리선택

response로 받아서 확인 할 수 있다.

resquest url : `https://www.ticketlink.co.kr/api/V2/plan/1259310931/seat-all/canverse/block2`

method : post

payload : blockId

---

popup_entry => 안됨

remain_block => 됨

remain_seat => 안됨

차이 분석하기 : toast.com의 쿠키를 추가 활용해볼 것

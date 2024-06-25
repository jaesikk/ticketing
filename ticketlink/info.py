import json

def set_info():
    try:
        with open('info.json', 'r',encoding='utf-8') as file:
            info = json.load(file)
        return info
    except:
        print('>>> [set_info] login_info.json 오류')


<<<<<<< HEAD
def get_cookie():
    try:
        with open('cookies.json', 'r',encoding='utf-8') as file:
            info = json.load(file)
        print('---')
        for i in info:
            print(i)
        return info
    except FileNotFoundError:
        print(f"File not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from : {e}")

if __name__=='__main__':
    get_cookie()
=======
if __name__=='__main__':
    set_info()
>>>>>>> b687fa43ae1c9d55a174ce25f82d7cf4a6e278d8

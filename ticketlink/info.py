import json

def set_info():
    try:
        with open('info.json', 'r',encoding='utf-8') as file:
            info = json.load(file)
        return info
    except:
        print('>>> [set_info] login_info.json 오류')


if __name__=='__main__':
    set_info()
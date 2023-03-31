import requests

with open("dataset_3378_3.txt", 'r') as f:
    data = f.readline().strip()

    r = requests.get(data)
    while True:
        if not r.text.startswith('We'):
            r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
            print(r.text)
            continue
        else:
            print('Содержимое последнего файла:')
            print(r.text)
            break
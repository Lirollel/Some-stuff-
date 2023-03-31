import requests 

with open("dataset_3378_2.txt", 'r') as f:
    data = f.readline().strip()
print(data)

r = requests.get(data)
answer = len(r.text.splitlines())
print(answer)
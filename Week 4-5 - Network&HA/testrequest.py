import threading
import requests

def thread_function(url):
    response = requests.get(url)

numberOfRequest = int(input('Enter Number of Request: '))

urlTarget = 'http://'+ input('Enter Load Balancer DNS: ')

for oneRequest in range(numberOfRequest):
    thread = threading.Thread(target=thread_function, args=(urlTarget,))
    print("Send Request: "+ str(oneRequest+1))
    thread.start()

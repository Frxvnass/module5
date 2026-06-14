import requests
import threading

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()

    for post in posts[:5]:
        print(post["title"])
        print(post["body"])

except requests.ConnectionError:
    print("no internet connection")
except Exception as e:
    print(f"error: {e}")


import time
def read_book():
    time.sleep(3)
    print("Reading book done")

def listen_music():
    time.sleep(2)
    print("Listening music done")

def drink_tea():
    time.sleep(1)
    print("Drinking tea done")


def run_threads(threads):
    for t in threads:
        t.start()
    for t in threads:
        t.join()


threads = [
    threading.Thread(target=read_book),
    threading.Thread(target=listen_music),
    threading.Thread(target=drink_tea),
]

run_threads(threads)
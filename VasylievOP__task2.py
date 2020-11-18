import os
import requests
from threading import Thread


print(os.listdir())
if os.path.exists("FilesScript"):
    print("FilesScript существует")
else:
    print("FilesScript не существует")
    os.mkdir("FilesScript")
    print("FilesScript создан")

os.chdir("FilesScript")
print(os.listdir())


def inputArrUrl(arr=[]):
    url = input("Enter URL:")
    if url == '':
        return arr
    else:
        arr.append(url)
        return inputArrUrl(arr)

treadID = 1
def downloadImg(*url):
    global treadID
    print(f"Thread started: {treadID}")
    url = ''.join(url)
    if url == '':
        return 0
    else:
        filename = url.split('/')[-1]
        print(filename)
        if os.path.exists(filename):
            print(f"{filename} существует")
        else:
            print(f"{filename} создан")
            file = open(filename, "wb")  # открываем файл для записи, в режиме wb
            content_n = requests.get(url, stream=True)  # делаем запрос
            file.write(content_n.content)  # записываем содержимое в файл; как видите - content запроса
            file.close()
    print(f"Thread finished: {treadID}")
    treadID += 1


threads = []
listURLs = inputArrUrl()
for i in listURLs:
    thread_n = Thread(target=downloadImg, args=(i,))
    threads.append(thread_n)
    thread_n.start()
    thread_n.join()

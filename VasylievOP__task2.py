import os
from threading import Thread
import requests

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


def downloadImg(treadID, *url):
    print(f"Thread started: {treadID}")
    url = ''.join(url)
    if url == '':

        return treadID
    else:
        filename = url.split('/')[-1]
        print(filename)
        if os.path.exists(filename):
            print(f"{filename} существует")
        else:
            print(f"{filename} создан")
            # открываем файл для записи, в режиме wb
            file = open(filename, "wb")
            content_n = requests.get(url, stream=True)  # делаем запрос
            # записываем содержимое в файл; как видите - content запроса
            file.write(content_n.content)
            file.close()
    print(f"Thread finished: {treadID}")


threads = []
listURLs = inputArrUrl()
threadID = 1
for i in listURLs:
    thread_n = Thread(target=downloadImg, args=(threadID, i))
    threads.append(thread_n)
    threadID += 1
    thread_n.start()
    thread_n.join()

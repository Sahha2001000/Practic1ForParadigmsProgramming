from threading import Thread


def logThread(word, threadID):
    print(f'Thread started: {threadID}')
    word = "".join(word)
    print(f"Argument: {word}")
    print(f'Thread finished: {threadID}\n')


threads = []
words = ['KEY', 'NEW', 'BOOK', 'SAD']
print(f"{words}\n")

i = 1
for word in words:
    thread_n = Thread(target=logThread, args=(word, i))
    threads.append(thread_n)
    thread_n.start()
    thread_n.join()
    i += 1

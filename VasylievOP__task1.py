from threading import Thread

threadID = 1


def sequenceToArguments(*sequence):
    global threadID
    sequence = list(sequence)
    print(f"Thread {threadID} started\n")
    for i in sequence:
        print(i)
    print(f"Thread {threadID} ended\n")
    threadID += 1


sequenceWord = input("Enter your str sequenc, please: ")

thread_1 = Thread(target=sequenceToArguments, args=(sequenceWord))
thread_2 = Thread(target=sequenceToArguments, args=(sequenceWord))
thread_3 = Thread(target=sequenceToArguments, args=(sequenceWord))
thread_4 = Thread(target=sequenceToArguments, args=(sequenceWord))

thread_1.start()
thread_1.join()

thread_2.start()
thread_2.join()

thread_3.start()
thread_3.join()

thread_4.start()
thread_4.join()

# import datetime
# import time
# import threading

# class Student:
#     def __init__(self) -> None:
#         self.run = False
#         self.count = 0
#         self.current1 = datetime.datetime.now()
#         self.current2 = datetime.datetime.now()
#         self.interval = datetime.timedelta(seconds=1)


#     def start(self):
#         self.run = True
#         self.work()

#     def stop(self):
#         self.run = False

#     def get_count(self):
#         return self.count

#     def work(self):
#         self.current1 = datetime.datetime.now()
#         while(self.run):
#             self.current2 = datetime.datetime.now()
#             # print (self.current2 - self.current1 > datetime.timedelta(seconds=1) and self.current2 - self.current1 > datetime.timedelta(seconds=2))
#             if (self.current2 - self.current1 > datetime.timedelta(seconds=1) and self.current2 - self.current1 > datetime.timedelta(seconds=2)):
#                 self.current1 = datetime.datetime.now()
#                 self.count += 1
                
#     def ask(self):
#         wait_time = input("Đếm trong bao lâu nữa?")
#         self.start()
#         self.t0 = datetime.datetime.now()
#         if self.t1 - self.t0 == wait_time:
#             self.t1 = datetime.datetime.now()
        

# def main():
#     student = Student()
#     t = threading.Thread(target=student.start)
#     # Người dùng nhập start thì student đếm
#     # Người dùng nhập stop thì dừng và nói final_count
#     # Người dùng nhập pause thì dừng và đợi, nói count hiện tại
#     # Người dùng nhập continue thì tiếp tục và hỏi tiếp tục trong bao lâu? sau khi hết thời gian tiếp tục thì dừng (stop)
#     # Người dùng nhập say thì học sinh nói count hiện tại

#     # Non-blocking
#     command = str(input()).lower()
    

#     if command == "start":
#         t.start()
    
#     elif command == "stop":
#         student.stop()
#         t.join()
#         print("FINAL: ",student.get_count())

#     elif command == "pause":
#         student.stop()
#         print("PAUSE: ",student.get_count())

#     elif command == "continue":
#         t.start()

#     while(1):

        
#         a.stop()
#         t.join()
#         print("FINAL: ", a.get_count())

# if __name__ == "_main_":
#     main()

import queue

import threading

import time
exitFlag = 0
class myThread (threading.Thread):

   def init(self, threadID, name, q):

        threading.Thread.init(self)

        self.threadID = threadID

        self.name = name

        self.q = q

   def run(self):

        print ("Starting " + self.name)

        process_data(self.name, self.q)

        print ("Exiting " + self.name)
def process_data(threadName, q):

    while not exitFlag:

        queueLock.acquire()

        if not workQueue.empty():

            data = q.get()

            queueLock.release()

            print (f"{threadName} processing {data}" )

        else:

            queueLock.release()

            time.sleep(1)
threadList = ["Thread-1", "Thread-2", "Thread-3"]

nameList = ["One", "Two", "Three", "Four", "Five"]

queueLock = threading.Lock()

workQueue = queue.Queue(10)

threads = []

threadID = 1
#Create new threads
for tName in threadList:

   thread = myThread(threadID, tName, workQueue)

   thread.start()

   threads.append(thread)

   threadID += 1
#Fill the queue
queueLock.acquire()

for word in nameList:

   workQueue.put(word)

queueLock.release()
#Wait for queue to empty
while not workQueue.empty():

   pass
#Notify threads it's time to exit
exitFlag = 1
#Wait for all threads to complete
for t in threads:

   t.join()

print ("Exiting Main Thread")
import re

# var='chary is busy with his work'
# s=re.match("chary",var)
# print(s)
# print(s.group())
# print(s.span())   # it gives len of word
# print(s.start())
# print(s.end())
#======================================
# var='chary is busy with his work'
# s=re.search("with",var)
# print(s)
# print(s.group())
#--=================----------------
# var='chary is busy with his work'
# s=re.search("work",var,re.I)
# print(s)
# print(s.group())
#===============================
# var="""chary is busy with h is work
# chary is talking with friends
# chary is playing cricket"""
# s=re.match("chary",var,re.M)
# print(s)
# print(s.group())
#======================================
# var="<html><body><head></body>"
# s=re.search('<.*>',var)                 -->          it is deep serach
# print(s.group())

#--------------------------------------

# var="html body<head>/body"
# s=re.search('<.*?>',var)               -->       it is narrow search
# print(s.group())

# ===================================

# var='dhoni is better than kohili'
# s=re.search(".* is .*",var)
# print(s.group())
#
#=============================================
# var='dhoni is better than kohili'
# s=re.search("(.*) is (.*)",var)
# print(s.group(1))
# print(s.group(2))

#===============================================

# var='dhoni scored 200 in against RCB @ 2022 with 8 avg per OVER!!!'
# data=re.findall("\d{1,4}",var)
# print(data)
#============================================================================
# var='dhoni scored 200 in against RCB @ 2022 with 8 avg per OVER!!!'
# data=re.findall("\D{1,4}",var)
# print(data)
#============================================================================
# var='dhoni scored 200 in against RCB @ 2022 with 8 avg per OVER!!!'
# data=re.findall("\w",var)
# print(data)
#============================================================================
# var='dhoni scored 200 in against RCB @ 2022 with 8 avg per OVER!!!'
# data=re.findall("\w*",var)
# print(data)
#============================================================================
# var='dhoni scored 200 in against RCB @ 2022 with 8 avg per OVER!!!'
# data=re.findall("\w+",var)
# print(data)
#============================================================================
# var='dhoni scored 200 in against RCB @ 2022 with 8 avg per OVER!!!'
# data=re.findall("\S",var)
# print(data)

# output: ['d', 'h', 'o', 'n', 'i', 's', 'c', 'o', 'r', 'e', 'd', '2', '0', '0', 'i', 'n', 'a', 'g', 'a', 'i', 'n', 's', 't', 'R', 'C', 'B', '@', '2', '0', '2', '2', 'w', 'i', 't', 'h', '8', 'a', 'v', 'g', 'p', 'e', 'r', 'O', 'V', 'E', 'R', '!', '!', '!']

#============================================================================

# var='dhoni scored 200 in against RCB @ 2022 with 8 avg per OVER!!!'
# data=re.findall("\W",var)
# print(data)

#output:  [' ', ' ', ' ', ' ', ' ', ' ', '@', ' ', ' ', ' ', ' ', ' ', ' ', '!', '!', '!']
#============================================================================


#Multi threading  --- >  GIL(gLOBSAL iNTERPRETER lAW)

# #SEQUENCIAL
# import time
# import threading
# def fun1():
#     print('one')
#     print(time.ctime())                 #using function call
#
# def fun2():
#     print('two')
#     print(time.ctime())
#
# fun1()
# fun2()



#THREADING
#
# import time
# import threading
# def fun1():
#     print('one')
#     print(time.ctime())
#
# def fun2():
#     print('two')
#     print(time.ctime())
#
# t1=threading.Thread(target=fun1)
# t2=threading.Thread(target=fun2)
#
# t1.start()
# t2.start()


import time
import threading
# def fun1(name):
#     print(name)
#     print(time.ctime())
#     time.sleep(2)
#
# def fun2(name):
#     print(name)
#     print(time.ctime())
#
# t1=threading.Thread(target=fun1,args=('dhoni',))
# t2=threading.Thread(target=fun2,args=('chary',))
#
# t1.start()
# t2.start()

# t1.join()
# t2.join()
#====================
#
#
# import time
# import threading
# def fun1(name,delay):
#     counter=0
#     while counter<5:
#         print(name)
#         print(time.ctime())
#         time.sleep(delay)
#         counter+=1
#
# t1=threading.Thread(target=fun1,args=('dhoni',2))
# t2=threading.Thread(target=fun1,args=('chary',4))
#
# t1.start()
# t2.start()
#

# ++++++++++++++++++++++++++++++++++
#
# import time
# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
#
#
#
#
# def multithreading(func, args, workers):
#     with ThreadPoolExecutor(workers) as ex:
#         res = ex.map(func, args)
#     return list(res)
#
#
# def multiprocessing(func, args, workers):
#     with ProcessPoolExecutor(workers) as ex:
#         res = ex.map(func, args)
#     return list(res)
#
#
# def cpu_heavy(x):
#     print('I am', x)
#     start = time.time()
#     count = 0
#     for i in range(10**8):
#         count += i
#     stop = time.time()
#     return start, stop
#
# #
# # def visualize_runtimes(results, title):
# #     start, stop = np.array(results).T
# #     plt.barh(range(len(start)), stop - start)
# #     plt.grid(axis='x')
# #     plt.ylabel("Tasks")
# #     plt.xlabel("Seconds")
# #     plt.xlim(0, 22.5)
# #     ytks = range(len(results))
# #     plt.yticks(ytks, ['job {}'.format(exp) for exp in ytks])
# #     plt.title(title)
# #     return stop[-1] - start[0]
#
#
# (multithreading(cpu_heavy, range(4), 4), "Multithreading")
# (multiprocessing(cpu_heavy, range(4), 4), "Multiprocessing")

# =============================================================


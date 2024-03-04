import threading
import time
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    print("Function completed")
time1=time.perf_counter()
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])
t1.start()
t2.start()
t3.start()
time2=time.perf_counter()
print("Performace: ",time2-time1)
#This can be used in a better way using concurrent.futures module.
'''
import concurrent.futures
import time
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return "Function completed"

def main():
    time1 = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(func, seconds) for seconds in [4, 2, 1]]

        for future in concurrent.futures.as_completed(results):
            print(future.result())

    time2 = time.perf_counter()
    print("Performance: ", time2 - time1)

if __name__ == "__main__":
    main()
'''
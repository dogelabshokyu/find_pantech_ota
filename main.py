import requests
import multiprocessing
import time


f = open("pantech_apk.txt", 'w')
fail = open("pantech_apk_fail.txt", 'w+')
req_fail = open("pantech_req_fail.txt", 'w')

def check_last():
    file_last = fail
    line = file_last.readlines()
    if len(line) == 0:
        return 0
    else:
        last = line[len(line)-1]
        last_check = int(last, 16)
        return last_check

def enter_s(num = 0):
    i = 73300775185
    if check_last() >= i:
        i = check_last()
    else:
        i = 73300775185
    while i <= num: 
        hex_num = str(format(i, 'x')).zfill(10)
        url = "http://update.pantech.onestopfile.co.kr/apkmanager/Upload/PKG/2014/"+hex_num+".apk"
        try:
            get_code = requests.get(url).status_code
        except:
            req_fail.write(str(hex_num)+"Req Error")
            get_code = requests.get(url).status_code
        if get_code == 404:
            fail.write(str(hex_num)+"\n")
        else:
            print(hex_num+".apk")
            f.write(url+"\n")
        i += 1
def get_count(num, p=4):
    list = []
    allocate = int(num/p)
    for n in range(p):
        list.append(allocate)
    list[p-1] += num%p
    print("Works/process : ", list)
    return list

if __name__ == "__main__":
    start_time = time.time()
    num = int(1099511627776)
    process = []
    for i in get_count(num, 10):
        p = multiprocessing.Process(target=enter_s, args=(i,))
        process.append(p)
        p.start()
    for p in process:
        p.join()
    print("End")
    print(time.time() - start_time)
    f.close()
    fail.close()
    req_fail.close()


import os
def ping():
    host = {'Camperdown': '192.168.1.1','Eastwood': '192.168.2.1','Artarmon':'192.168.3.1'}
    response=[]
    area = list(host.keys())
    for i in host.values():
        response.append(os.system('ping -n 1 %s' %(i)))

    for i in range(len(response)):
        if response[i] == 0:
            print(area[i] + " is alive")
        else:
            print(area[i] + " is dead")



ping()
os.system('pause')

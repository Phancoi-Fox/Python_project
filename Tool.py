import requests, os, sys
from datetime import datetime
from time import sleep

def fivex_delay(c):
	while(c > 1):
		c -= 1
		bn=">> Delay - "+str(c)+'\r'
		for n in bn:
			sys.stdout.write(n)
			sys.stdout.flush()
			sleep(0.05)
		sleep(0.05)
		print(' '*len(bn),end='\r')


while True:
    token = input("Enter token: ")
    getprofile = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token).json()
    if 'success' in getprofile:
        user_id = getprofile['data']['user']
        xu = getprofile['data']['xu']
        xudie = getprofile['data']['xudie']
        print('Account: ' + user_id + '\n'+
              'Current Coin: '+ xu + '\n'+
              'Died Coin: ' + xudie)
        sleep(1)
        break
    else:
        print('Token is invalid!')

#Config
while True:

    uid = int(input("Enter ID nick to run: "))
    config = requests.get('https://traodoisub.com/api/?fields=tiktok_run&id='+ str(uid) + '&access_token='+ token).json()
    if 'success' in config:
        account = config['data']['uniqueID']
        msg = config['data']['msg']
        print('ID: '+ account+'\n'+
              'Message: '+ msg)
        sleep(1)
        break
    else: 
        print('Config fail')
os.system('clear')
while True:
    print("Choose 1 to like"+'\n'
          "Choose 2 to follow")
    typeofjob = int(input("Enter: "))
    if typeofjob == 1 or typeofjob == 2: 
        break
    else: 
        print("Enter type of job again!")
delay = int(input("Time to delay: "))
while True:
    stop = int(input("Enter the number of task ( >= 10): "))
    if stop >= 10:
        break
s = 0

while True:
    while True:
        try:
            if typeofjob == 1:
                get_job = requests.get('https://traodoisub.com/api/?fields=tiktok_like&access_token=' + token).json()
            if typeofjob == 2:
                get_job = requests.get('https://traodoisub.com/api/?fields=tiktok_follow&access_token=' + token).json()
            if 'data' in get_job: 
                break
        except:
            print("Network Error!")
    list_job = get_job['data']
    for i in range(0, len(list_job)):
        try:
            s += 1
            id_job = list_job[i]['id']
            link_job = list_job[i]['link']
            type_job = list_job[i]['type']
            time_to = datetime.now().strftime("%H:%M:%S")
            os.system("cmd /c start "+str(link_job) if os.name == "nt" else "termux-open-url "+str(link_job))
            complete = "Job: " + str(s) + '\n',"ID Job: " + id_job + '\n',"Link Job: "+link_job + '\n',"Time: " + time_to + '\n'
            print('---------------------------------------------------------------------------')
            for j in complete:
                sys.stdout.write(j)
                sys.stdout.flush()
                sleep(0.025)
            sleep(1)
            fivex_delay(delay)

            if typeofjob == 1:
                get_coin1 = requests.get('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE_CACHE&id='+ id_job + '&access_token=' + token).json()
            if typeofjob == 2:
                get_coin1 = requests.get('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id='+ id_job + '&access_token=' + token).json()
            if int(get_coin1['cache']) % 10 == 0:
                sleep(1)
                while True:
                    try:
                        if typeofjob == 1:
                            get_coin2 = requests.get('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE&id=TIKTOK_LIKE_API&access_token=' + token).json()
                        if typeofjob == 2:
                            get_coin2 = requests.get('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token=' + token).json()
                        if 'success' in get_coin2:
                            break
                    except:
                        print('Network Error!')
                add_coin = '@'*len(str(s))
                mess = get_coin2['data']['msg']
                current_coin = get_coin2['data']['xu']
                time_to_print = datetime.now().strftime("%H:%M:%S")
                print("\n")
                print('============================================')
                print(add_coin, time_to_print, mess, current_coin)
                print("============================================")
                print("\n")
            if s == stop: break
        except:
            print("Network Error!")
    if s == stop: break
print("Thanks for your using!")


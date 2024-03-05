"""
API Tester

Andrew Kotyck

"""

import requests
import json
import time
import threading
import os

from datatypes import dictt




astro = "https://api.wheretheiss.at/v1/satellites/25544"
connor = 'https://api.github.com/users/connorwilkinscs'


def iss(url, event: threading.Event):
        try:
            while not event.is_set():
                response = requests.get(url)
                data = dictt(response.json())
                data.show()
                print()
                time.sleep(10)
        except Exception as e:
            print(str(e))
            stop_event.set()



def githubber(url, event: threading.Event):
    response = requests.get(url)
    data = dictt(response.json())
    reposurl = data['repos_url']
    response2 = requests.get(reposurl)
    repos = list(response2.json())
    for i in repos:
        try:
            #print('\n#### V #### DICTIONARY #### V ####')
            # dictt(i).show()
            print(i['name'])
            #print('#### ^ #### DICTIONARY #### ^ ####\n')
        except Exception as e:
            print(e)
    
        
    
    #repos.show()



if __name__ == '__main__':
    stop_event= threading.Event()
    # issthread = threading.Thread(target=iss, args=(connor, stop_event))
    
    # #issthread.start()
    # print('starting thread...')
    
    # try:
    #     while True:
    #         time.sleep(5)
    # except KeyboardInterrupt:
    #     print('Interrupted')
    #     stop_event.set()
    # except Exception as e:
    #     print(e)
    #githubber(connor, stop_event)

    # os.system('git init')
    # os.system('git add datatypes.py')
    # os.system('git add main.py')
    # os.system('git commit -a -m "programmatic commit"')
    # os.system('git branch experimental')
    os.system('git switch experimental')
    os.system('git commit -a')

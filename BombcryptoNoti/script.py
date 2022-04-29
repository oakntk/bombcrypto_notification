import requests
import time
import pyautogui
import threading
from datetime import datetime

#pip3 install opencv-python
url = 'https://notify-api.line.me/api/notify'
token = 'rWFHtfwV8jCsQNfD25J7I3hRHEcbA1QpOUStYBk0bVp'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer'+token}

pyautogui.FAILSAFE= True
now = datetime.now()
current_time = now.strftime("%H%M%S")
print("Current Time =", current_time)

def connectwallet():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H%M%S")
        time.sleep(5)
        r= None 
        while r is None:
            btn_connectwallet = pyautogui.locateOnScreen('images/connectwallet1.jpg', grayscale=True, confidence=0.5)
        print(r)
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'saveimages/disconnect/'+str(current_time)+'.jpg')
        img = {'imageFile': open('saveimages/disconnect/'+str(current_time)+'.jpg','rb')}
        data = {'message':'เกมหลุด'}
        headers = {'Authorization':'Bearer ' + token}
        session = requests.Session()
        session_post = session.post(url, headers=headers, files=img, data =data)
        print(session_post.text) 
        time.sleep(300)

def newmap():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H%M%S")
        btn_newmap = pyautogui.locateOnScreen('images/newmap.jpg' or 'images/newmap1.jpg', confidence=0.9)
        if btn_newmap is not None:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'saveimages\disconnect'+str(current_time)+'.jpg')
            img = {'imageFile': open('saveimages/disconnect'+str(current_time)+'.jpg','rb')}
            data = {'message':'New map'}
            headers = {'Authorization':'Bearer ' + token}
            session = requests.Session()
            session_post = session.post(url, headers=headers, files=img, data =data)
            print(session_post.text) 
            time.sleep(30)

def unknown():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H%M%S")
        btn_unknown = pyautogui.locateOnScreen('images/unknown.jpg', confidence=0.9)
        if btn_unknown is not None:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'saveimages\disconnect'+str(current_time)+'.jpg')
            img = {'imageFile': open('saveimages/disconnect'+str(current_time)+'.jpg','rb')}
            data = {'message':'Unknown'}
            headers = {'Authorization':'Bearer ' + token}
            session = requests.Session()
            session_post = session.post(url, headers=headers, files=img, data =data)
            print(session_post.text) 
            time.sleep(30)

def socketerror():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H%M%S")
        btn_socketerror = pyautogui.locateOnScreen('images/socketerror.jpg', confidence=0.9)
        if btn_socketerror is not None:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'saveimages\disconnect'+str(current_time)+'.jpg')
            img = {'imageFile': open('saveimages/disconnect'+str(current_time)+'.jpg','rb')}
            data = {'message':'Disconnected'}
            headers = {'Authorization':'Bearer ' + token}
            session = requests.Session()
            session_post = session.post(url, headers=headers, files=img, data =data)
            print(session_post.text) 
            time.sleep(30)

thrdisconnect = threading.Thread(target=connectwallet)
# thrdisconnect1 = threading.Thread(target=unknown)
# thrdisconnect2 = threading.Thread(target=newmap)
# thrdisconnect3 = threading.Thread(target=socketerror)
thrdisconnect.start()
# thrdisconnect1.start()
# thrdisconnect2.start()
# thrdisconnect3.start()


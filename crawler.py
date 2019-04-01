import requests
import time
import webbrowser
import http.client as httplib
import urllib

host  = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# Fill in here
account  = ""
password = ""
 
def send_sms(text, mobile):
    params = urllib.parse.urlencode({'account': account, 'password' : password, 'content': text, 'mobile':mobile,'format':'json' })
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

url = ['https://www.microsoftstore.com.cn/refurbishedsurface/certified-refurbished-surface-pro/p/mic2408',
       'https://www.microsoftstore.com.cn/refurbishedsurface/certified-refurbished-surface-pro/p/mic2407']

headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
        }

num=0
while True: 
    for i in url:
        num+=1
        print(str(num) + 'th try at - ' + time.ctime())
        resp = requests.get(i, headers=headers).text
        if(resp.find('加入购物车')>0):
            # Fill in here
            mobile = ""
            text = "您的验证码是：6666。请不要把验证码泄露给其他人。"
            print(send_sms(text, mobile))
            webbrowser.open(i)        
            with open('f.txt', 'wt') as f:
                print('Find at ' + str(num) + 'th try at - ' + time.ctime(), file=f)
            break
        time.sleep(30)
    if(resp.find('加入购物车')>0):
        break
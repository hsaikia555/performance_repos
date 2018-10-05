import requests
import json
import config
import time
def logIn():
    try:

        session=requests.session()
        URL=config.PROTOCOL+"://"+config.HOST+":"+config.PORT+"/bedrock-app/services/rest/login"
        print(URL)
        requestJson={"username": config.USERNAME,"password": config.PASSWORD}
        print(requestJson)
        response=session.post(URL,json=requestJson)
        print(response.text)
        print(response.headers['JSESSIONID'])
        if int(response.status_code) == 200:
            print("login successful")
        else:
            print("unsucessful long")
            exit()
        return session
    except Exception as e:
        print("Some Exception has been found:",e)






#test1=time.strftime('%Y%m%d%H%M%S')
#print(test1)



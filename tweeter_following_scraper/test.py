from datetime import datetime
from messager import tweet_discord,following_discord
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os

'''
Parameter : target_acc, Is the account username which follow someone.
            following, Is the new following added into list.

Repr : Function sends the message using slack webhook on the channel

       #twitter-new-account-follows

'''


username = 'bot_citadel'
password = 'discorddev'
email = 'Jacobtheovieira@gmail.com'

def loop_used(driver,target_acc):
    driver.get(f'https://twitter.com/{target_acc}/following')
    time.sleep(3)
    main_h_div = driver.find_element(By.XPATH, '//div[@data-testid="primaryColumn"]')
    user_list = main_h_div.find_elements(By.XPATH,'//div[@data-testid="UserCell"]')
    # print(user_list)
    USER_LIST = []
    for ul in user_list:
        text_list = str(ul.text).split('\n')
        user = ""
        for u_name in text_list[:2]:
            if '@' in u_name:
                user =  u_name
                # print(user)
        USER_LIST.append(user)

    user_in_file =[]
    file_name = str(target_acc) + '_file.txt'
    try:
        if os.path.isfile(file_name):
            user_in_file = open(file_name,'r').read()
            user_in_file = str(user_in_file).split('\n')
    except:
        user_in_file = []
    USER_LIST = list(set(USER_LIST))
    users_to_send=[]
    new_file = open(str(file_name),'w')
    for name in USER_LIST:
        if str(name) in user_in_file:
            print('USER EXIST')
        else:
            users_to_send.append(name)
        try:
            new_file.write(str(name))
            new_file.write('\n')
        except:
            print(str(name)+' not written')
    new_file.close()
    if len(users_to_send) == 0:
        print('NO NEW USERS')
        return False
    return ' , '.join(users_to_send)

def scrap_tweet(driver,target_acc):
    messages = ''
    driver.get(f'https://twitter.com/{target_acc}/')
    time.sleep(3)
    # main_h_div = driver.find_element(By.XPATH, '//div[@data-testid="primaryColumn"]')
    tweet_list = driver.find_elements(By.TAG_NAME, 'article')
    message_LIST = []
    user_in_file = []
    file_name = str(target_acc) + '_tweets_file.txt'
    new_file = open(str(file_name), 'w')
    try:
        if os.path.isfile(file_name):
            user_in_file = open(file_name, 'r').read()
    except:
        user_in_file = []

    for ul in tweet_list:
        try:
            # text_list = str(ul.text).split('\n')
            if str(target_acc) in str(ul.text):
                text = ul.find_element(By.XPATH,'./div/div/div/div[2]/div[2]/div[2]/div[1]')
                # print(text.text)
                if str(text.text) in user_in_file:
                    print('tweet exists')
                else:
                    try:
                        message_LIST.append(str(text.text))
                        new_file.write(str(text.text))
                        new_file.write('\n')
                    except:
                        pass
        except:
            pass
        new_file.close()
    time.sleep(3)
    if len(message_LIST) == 0:
        return False
    return message_LIST

def main(username,password,target_acc,filename):
    s = Service(ChromeDriverManager().install())
    ua = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument(ua)
    driver = webdriver.Chrome(service=s,options=chrome_options)
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get('https://twitter.com/i/flow/login')
    time.sleep(5)
    user = driver.find_element(By.NAME, 'username')
    user.send_keys(username)
    time.sleep(1)
    user.send_keys(Keys.ENTER)
    try:
        time.sleep(3)
        user = driver.find_element(By.NAME, 'password')
        user.send_keys(password)
        time.sleep(1)
        user.send_keys(Keys.ENTER)
    except:
        pass
    time.sleep(5)
    target_account = ['@ak_xxiv','@ZssBecker', '@elliotrades', '@ryandcrypto', '@danielesesta', '@cryptoAGC',
                      '@ANordicRaven','theosyris13']
    for target_acc in target_account:
        try:
            messages = scrap_tweet(driver, target_acc)
            print(messages)
            if messages != False:
                tweet_discord(messages, target_acc)
            else:
                print('EMAIL NOT SENT--- NO NEW TWEETS FOUND')
        except:
            print(target_acc+' not scrapped for tweets')
            pass
        try:
            users = loop_used(driver,target_acc)
            if users != False:
                following_discord(users,target_acc)
            else:
                print('EMAIL NOT SENT--- NO NEW USERS FOUND')
        except:
            print(target_acc + ' not scrapped for followings')
            pass
    driver.close()
    driver.quit()
if __name__ == '__main__':
    main(username,password,target_acc='',filename='')



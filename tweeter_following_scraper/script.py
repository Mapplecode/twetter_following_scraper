def send_slack_msg(target_acc,following):
    '''
    Parameter : target_acc, Is the account username which follow someone.
                following, Is the new following added into list.

    Repr : Function sends the message using slack webhook on the channel 

           #twitter-new-account-follows 

    '''
    try:
        url = "https://hooks.slack.com/services/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"
        payload = {
        "text": f"{target_acc} just followed {following} \n https://twitter.com/{following}"
        }
        res = requests.post(url,data=json.dumps(payload))
        logging.info('send_slack_msg function run successfully.')
        return res
    except Exception as e:
        logging.error(e)

def loop_used(all_divs,target_acc,filename):
    try:
        for div in all_divs:
            following = div.text.split("Follow")[0].split("@")[-1]
            if os.path.exists(filename):
                with open(filename) as f:
                    following_list = f.read()
                exists = following_list.split("\n")
                # print(len(exists))
                if f"@{following}" in following_list:  
                    print(f"{following} already exists.")
                else:
                    print(f"{target_acc} just followed {following} \n https://twitter.com/{following}")
                    time.sleep(3)
                    # send_slack_msg(target_acc,following)
                    with open(filename,"a+") as f:
                        f.write(f"@{following}")
            else:
                with open(filename,"a+") as f:
                    f.write(f"@{following}")
        logging.info('loop_used function run successfully.')
    except Exception as e:
        logging.error(e)

def main(username,password,target_acc,filename):
    '''
    Parameter : username, Username of your twitter account.
                password, password of your twitter account.

    Repr : Function sends the message using slack webhook on the channel 

           #twitter-new-account-follows 

    '''
    try:
        s = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=s,options=chrome_options)
        driver.maximize_window()
        actions = ActionChains(driver)
        driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        user = driver.find_element(By.NAME, 'username')
        user.send_keys(username)
        user.send_keys(Keys.ENTER)
        time.sleep(5)
        user = driver.find_element(By.NAME, 'password')
        user.send_keys(password)
        user.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.get(f'https://twitter.com/{target_acc}/following')
        time.sleep(3)

        all_divs = driver.find_elements(By.XPATH,  '//div[@data-testid="UserCell"]')
        loop_used(all_divs,target_acc,filename)
        driver.close()
        logging.info('main function run successfully.')
    except Exception as e:
        logging.error(e)
        
if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.options import Options

    import os.path
    import requests
    import json
    import logging
    import logging
    logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG,format='%(asctime)s %(message)s')

    # creds
    username = 'sparshk3333'
    password = 'Pass@123'
    
    # print("[INFO] Start Execution!!")
    logging.info('Start Execution!!')
    # taget account .
    with open('target_list.txt') as file:
        acc_to_scrape = file.read()
    for target_acc in acc_to_scrape.split('\n'):
        # destination_folder
        filename = f"Target_acc_data\{target_acc}.csv"
        main(username,password,target_acc,filename)
        # print(f'[INFO] Scraping Done for {target_acc}')
        logging.info(f'Scraping Done for {target_acc}')
        logging.info(f'File stored at the destination {filename}')
    # print("[INFO] END")
    logging.info("[INFO] END")
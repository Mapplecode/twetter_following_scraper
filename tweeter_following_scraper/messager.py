from datetime import datetime
import requests

'''
Parameter : target_acc, Is the account username which follow someone.
            following, Is the new following added into list.

Repr : Function sends the message using slack webhook on the channel

       #twitter-new-account-follows

'''
def tweet_discord(message,target_acc):

    date_now = str(datetime.now().date())
    time_now = str(datetime.now().time())
    content = ''
    # content += '\n'
    # content +='DATE - '+date_now+'\n'
    # content += 'TIME - ' + time_now + '\n'
    # content +='##################################'+ '\n'
    # content += '##################################'+ '\n'
    # content += '\n'
    content += str(target_acc)+' Tweeted :\n'+('\n'.join(message))+'\n'
    content += '\n'
    # content += '=============================='+ '\n'
    # content += '=============================='+ '\n'
    # content += '\n'
    # res = requests.post(url,data=json.dumps(payload))
    url = 'https://discord.com/api/webhooks/910235427745697832/SuK1Ga8nIenNULRG2TnX5yswjLqUz7GVMSmGdtZUKyY4WvoE3ZK1k6EUUXiRRFioLiQy'
    payload = {'user name': 'user_tweets',
               'content': content}
    response = requests.request("POST", url, data=payload)
    print('DISCORD MESSAGE SENT FOR - '+str(target_acc))
    print(response.text)
    return response.text



def following_discord(following,target_acc):
    date_now = str(datetime.now().date())
    time_now = str(datetime.now().time())
    content = ''
    # content +='DATE - '+date_now+'\n'
    # content += 'TIME - ' + time_now + '\n'
    # content +='##################################'+ '\n'
    # content += '##################################'+ '\n'
    content += '\n'
    content += str(target_acc)+' Started Following :\n'+(following)+'\n'
    # content += '\n'
    # content += '=============================='+ '\n'
    # content += '=============================='+ '\n'
    content += '\n'
    # res = requests.post(url,data=json.dumps(payload))
    url = "https://discord.com/api/webhooks/910235427745697832/SuK1Ga8nIenNULRG2TnX5yswjLqUz7GVMSmGdtZUKyY4WvoE3ZK1k6EUUXiRRFioLiQy"

    payload = {'user name': 'twitter bot',
               'content': content}


    response = requests.request("POST", url, data=payload)
    print('DISCORD MESSAGE SENT FOR - '+str(target_acc))
    print(response.text)
    return response.text
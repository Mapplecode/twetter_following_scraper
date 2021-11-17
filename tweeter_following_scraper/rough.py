# height_1 = (main_h_div.size.get('height'))
# b=True
# MAX_TRY = 0
# try:
#     while(b):
#         try:
#             main_h_div_path = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div'
#             main_h_div2 = driver.find_element(By.XPATH, main_h_div_path)
#             user_list = main_h_div2.find_elements(By.XPATH, '//div[@data-testid="UserCell"]')
#             for ul in user_list:
#                 text_list = str(ul.text).split('\n')
#                 _user = ""
#                 for u_name in text_list[:2]:
#                     if '@' in u_name:
#                         _user =  u_name
#                         print(_user)
#                     if _user != '':
#                         USER_LIST.append(_user)
#                     loc = ul.location_once_scrolled_into_view
#             time.sleep(2)
#             height_2 = (main_h_div2.size.get('height'))
#             if height_2 == height_1:
#                 b=False
#             else:
#                 height_1 = height_2
#         except Exception as e:
#             print(e)
#             if MAX_TRY != 10:
#                 MAX_TRY = MAX_TRY +1
#             else:
#                 b=False
# except:
#     pass
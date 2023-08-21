import re;
# txt = ' sam '
# x = re.search('\S', txt)
# print(x)
users = input('username: ')
username = ['max', 'john', 'vash']
if not isinstance(users, str):
    raise TypeError('not a match')
else:
    username_found = False
    for user in username:
        if re.search(user, users, re.IGNORECASE):
          username_found = True
          print(f'welcome {user}')
          break
    if not username_found:
        print('user not found')
# assignment=> http status code
#     if re.search(user, users, re.IGNORECASE):
#         print(f'welcome {user}')
# else:
#     print('username not recognized')
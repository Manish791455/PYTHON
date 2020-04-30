user_database = {'usernames_list' : ['manish', 'darpan', 'mohmmad', 'sandeep', 'prasanth'],

'manish_password' : 'mani',
'darpan_password' : 'singh',
'mohmmad_password' : 'zulfekhar',
'sandeep_password' : 'deepu',
'prasanth_password' : 'prasan'


}
print('welcome to next level')
print('enter username')
user_name = input() .strip() .lower() 
if user_name in user_database['usernames_list']:
    print('hey {} please enter your password to continue '.format(user_name))
else:
    print('you are not registered, please register and continue')  
user_password = input() .strip() 
if user_password == user_database[user_name+'_password']:
    print('welcome to next level')  
else:
    print('you have entered incorrect password')      
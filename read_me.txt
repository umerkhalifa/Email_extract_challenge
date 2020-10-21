
# Steps to avoid using acutal password

1. Login into your gmail account 
2. Click "Manage Google Account" drop down
3. Click "security" (left side)
4. Click "App passwords" in "sign in to Google"
5. Upon clicking "App passwords" you will be asked to type your password
6. Choose "mail" in "select app" and "device" (e.g. "windows computer") "select device". 
7. Click "generate" once the app and device is chosen (16 digits password will be generated).
8. Use the 16 digits as temporary password.  


# Steps for running the code
open the run.py file and perform the following steps
1. Install imapclient (e.g. pip install imapclient)
2. import datetime and os
3. change the directory ( path of file directory where "sub_sort" is saved) (e.g. os.chdir(r'c:\......')
4. import sub_sort
5. call the function email_sort from sub_sort and fill the credentials (e.g. output = sub_sort.email_sort(username, password, subject, since))
6. Print the output (e.g. print(output)

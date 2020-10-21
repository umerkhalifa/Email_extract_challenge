# Note: Please install the imapclient before to run any code
# pip install imapclient 

import datetime
import os 
os.chdir(r'') # Note: Please add the directory where the sub_sort file is saved
import sub_sort

# Add credentials
username = '' # include email id (e.g. lovealert@gmail.com)
password = '' # use email password or generate temporary password (e.g. love@123)
subject = 'Thank you for applying' 
since = datetime.date(2018,8,22) # include year, month, date (e.g. 2018,8,22)

# Run the code
output = sub_sort.email_sort(username, password, subject, since)

print(output)
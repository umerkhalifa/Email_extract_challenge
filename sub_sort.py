import imapclient
import smtplib
import pandas as pd

def email_sort(username, password, subject, since):
    lst_envelope = []
    lst_subject = []
    lst_date = []

    imap_server = 'imap.gmail.com'
    server = imapclient.IMAPClient(imap_server, ssl=True)
    server.login(username, password)
    select_info = server.select_folder('INBOX')
    messages = server.search(['subject',subject, 'since', since])
    for msgid, data in server.fetch(messages, ['ENVELOPE']).items():
        envelope = data[b'ENVELOPE']
        lst_envelope.append(str(envelope.sender[0]))
        lst_subject.append(envelope.subject.decode())
        lst_date.append(envelope.date)

    dict = {'sender':lst_envelope, 'subject': lst_subject, 'date': lst_date}  
    data = pd.DataFrame(dict)
    return data

if __name__ == '__main__':
    email_sort()

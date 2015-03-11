#!/usr/bin/env python

import imaplib

username = 'zhaoyb@travelsky.com'
password = '2u2nqcedks'

mail_server = 'pop3.travelsky.com'

i = imaplib.IMAP4_SSL(mail_server)
print i.login(username, password)
print i.select('INBOX')
for msg_id in  i.search(None, 'ALL')[1][0].split():
    print msg_id
    outf = open('./mail/%s.eml' % msg_id, 'w')
    outf.write(i.fetch(msg_id, '(RFC822)')[1][0][1])
    outf.close()
i.logout()

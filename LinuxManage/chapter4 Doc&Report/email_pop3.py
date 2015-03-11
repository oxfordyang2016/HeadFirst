#!/usr/bin/env python

import poplib

username = 'zhaoyb@travelsky.com'
password = '2u2nqcedks'

mail_server = 'pop3.travelsky.com'

p = poplib.POP3(mail_server)
p.user(username)
p.pass_(password)
for msg_id in  p.list()[1]:
    print msg_id
    outf = open('./mail/%s.eml' % msg_id, 'w')
    outf.write('\n'.join(p.retr(msg_id)[1]))
    outf.close()
p.quit()

__author__ = 'aidong'

import sys
from BeautifulSoup import BeautifulSoup as Soup

def parseLog(file):
    handler = open(file).read()
    soup = Soup(handler)
    for message in soup.findAll('message'):
        msg_attrs = dict(message.attrs)
        f_user = message.find('from').user
        f_user_dict = dict(f_user.attrs)
        # print "%s: %s [%s @ %s]" % (f_user_dict[u'friendlyname'],
        #                             message.find('text').decodeContents(),
        #                             msg_attrs[u'date'],
        #                             msg_attrs[u'time'])
        print  msg_attrs


if __name__ == "__main__":
    parseLog('test.xxx')

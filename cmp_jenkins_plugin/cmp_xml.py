__author__ = 'aidong'

# from BeautifulSoup import BeautifulSoup, SoupStrainer
# import re
#
# file = open("C:\\WorkSpace\\9.5xmain_automation_test\\cmp_jenkins_plugin\\ipg110104.xml", "rb")
# print "aaa"
# print(file)
# listing = SoupStrainer('entry', text = re.compile('SEQUENCE LISTING'))
# #print(listing)
# soup = BeautifulSoup(file, parseOnlyThese = listing)
# print soup.prettify()
# file.close()
#


import sys
from BeautifulSoup import BeautifulSoup as Soup


def intersection_with_different_longname_or_version(a_list,b_list):
    ret=[]
    for a in a_list:
        for b in b_list:
            if a != b:
                if "{:30.30}".format(a) == "{:30.30}".format(b):
                    ret.append(a+"    "+" in cm")
                    ret.append(b+"    "+" in smant")
                    break
    return ret
def difference_with_different_shortname(a_list,b_list):
    ret=[]
    for a in a_list:
        found_b=None
        for b in b_list:
            if a == b or "{:30.30}".format(a) == "{:30.30}".format(b):
                found_b=b
                break
        if found_b==None:
            ret.append(a+"    "+" in cm")

    for b in b_list:
        found_a=None
        for a in a_list:
            if a == b or "{:30.30}".format(a) == "{:30.30}".format(b):
                found_a=a
                break
        if found_a==None:
            ret.append(b+"    "+" in smant")
    return ret

def parseLog(file):
#    file = sys.argv[1]
    handler = open(file).read()
    soup = Soup(handler)
    #print soup.contents
    plugins=  soup.findAll('plugin')
    sorted_plugins=sorted(plugins,key=lambda plugin: plugin.shortname.text)      #good
    plugins.sort(key=lambda plugin: plugin.shortname.text)                              #good
    #a=plugins.sort(key=lambda plugin: plugin.shortname.text) #bad
    #print plugins
    ret=[]
    for plugin in plugins:
    #for plugin in sorted_plugins:
        #str=long_name
        ret.append('{:30.30}     {:40.40}   {:30.30}'.format(plugin.shortname.text, plugin.longname.text,plugin.version.text))

        #long_name_attrs = dict(long_name.attrs)
        #print long_name.text
        # short_name = long_name.find('shortName').user
        # f_user_dict = dict(f_user.attrs)
        # print "%s: %s [%s @ %s]" % (f_user_dict[u'friendlyname'],
        #                             message.find('text').decodeContents(),
        #                             msg_attrs[u'date'],
        #                             msg_attrs[u'time'])
        #print "hahahah"
        #print long_name
        #print "%s" % (long_name.find('text'))
        #print "%s" % (long_name_attrs)
    return ret

def write_str_to_file(_f, vars):
    for var in vars:
        #_f.write("%s = %s\n" % (name, repr(val)))
         _f.write('{:150.150} \n'.format(var))
if __name__ == "__main__":
    a=parseLog('C:\\WorkSpace\\9.5xmain_automation_test\\cmp_jenkins_plugin\\cm.plugin.xml')
    b=parseLog('C:\\WorkSpace\\9.5xmain_automation_test\\cmp_jenkins_plugin\\smant.plugin.xml')



    print len(a)
    print len(b)
#    print len(c)


    # for a_ in a:
    #     print a_
    #
    # for b_ in b:
    #     print b_

    cm_plugin_file = open('cm.plugin', 'w')
    write_str_to_file(cm_plugin_file, a)
    cm_plugin_file.close
    smant_plugin_file = open('smant.plugin', 'w')
    write_str_to_file(smant_plugin_file, b)
    smant_plugin_file.close


    a_sorted_list=sorted(set(a)) # is a must    but is a list and not set
    b_sorted_list=sorted(set(b)) # is a must

    # for b_ in b_sorted_list:
    #     print b_

    print 'plugin count in cm='+str(len(a))
    print 'plugin count in smant='+str(len(b))

    c_sorted_list=sorted(set(a).intersection(set(b)))
    # for c_ in c_sorted_list:
    #     print c_

    print 'totally same plugins both in cm and smant='+str(len(c_sorted_list))
    totally_same_plugin_file = open('totally.same.plugin', 'w')
    write_str_to_file(totally_same_plugin_file, c_sorted_list)
    totally_same_plugin_file.close

    d_sorted_list=difference_with_different_shortname(a,b)
    print 'totally different plugins for cm and smant='+str(len(d_sorted_list))
    totally_different_plugin_file = open('totally.different.plugin', 'w')
    write_str_to_file(totally_different_plugin_file, d_sorted_list)
    totally_different_plugin_file.close

    e_sorted_list=intersection_with_different_longname_or_version(a,b)
    print 'same plugins with different version or long name='+str(len(e_sorted_list)/2)
    diff_version_plugin_file = open('different.version.or.longname.but.same.plugin', 'w')
    write_str_to_file(diff_version_plugin_file, e_sorted_list)
    diff_version_plugin_file.close
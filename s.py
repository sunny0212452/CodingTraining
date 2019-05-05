# -*- coding:utf-8 -*-
#将字符串中的空格替换成%20
def replaceSpace(s):
    # write code here
    l = len(s)
    print 'l:',l
    num_blank=0
    for i in s:
        if i==' ':
            num_blank+=1
    l_new = l+num_blank*2
    print 'l_new:',l_new
    index_old = l-1
    index_new = l_new
    s_new=[' ']*l_new
    while(index_old >= 0 and index_new > index_old):
        if s[index_old]==' ':
            #index_new-=1
            s_new[index_new-1]='0'
            #index_new-=1
            s_new[index_new-2]='2'
            #index_new-=1
            s_new[index_new-3]='%'
            index_new-=3

        else:

            print index_new
            s_new[index_new-1]=s[index_old]
            index_new-=1

        index_old-=1
    ss=''
    print s_new
    for i in s_new:
    	ss+=str(i)
    return ss


s='We are happy.'
print "s:",s
s1=replaceSpace(s)
print "s1:",s1
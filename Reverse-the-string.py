#coding:utf-8
#"逆轉字符串--輸入一個字符串，將其逆轉并輸出。"

stringX = raw_input("請隨意輸入一個字符串:")

#方法一：
string1 = stringX[::-1]
print 'string1:', string1


#方法二：
string2 = list(stringX)

string2.reverse()

string3 = ''.join(string2)

print "string3:",string3

#方法三
string4 = list(stringX)

string5 = string4[::-1]

string6 = ''.join(string5)

print "string6:",string6

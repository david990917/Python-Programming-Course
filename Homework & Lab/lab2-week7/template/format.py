# -*- coding: cp936 -*-

# 利用函数编程：先输入一个字符串，再根据该字符串的长度给出如下形状的输出。
# *********************
# *********************
# $$$$             $$$$
# $$$$             $$$$
# ==== some string ====
# $$$$             $$$$
# $$$$             $$$$
# *********************
# *********************

def star(n):
    print n * "*"
    print n * "*"

def dollar(n):
    print "%s%s%s" % (4*"$",(n-8)*" ",4*"$")
    print "%s%s%s" % (4*"$",(n-8)*" ",4*"$")

def main():
    s = raw_input("输入一个字符串：")
    n = len(s) + 10
    star(n)
    dollar(n)
    print "%s%s%s" % (4*"="+" ",s," "+4*"=")
    dollar(n)
    star(n)

main()
    

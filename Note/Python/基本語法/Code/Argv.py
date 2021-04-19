import sys

#顯示所有參數
print(sys.argv)

#如果參數大於一個以上。
if len(sys.argv)>1:
    print(sys.argv[1])  #顯示第一個參數

if len(sys.argv)>2:
    print(sys.argv[2])  #顯示第一個參數
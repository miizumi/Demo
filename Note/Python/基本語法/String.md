# String 字串


<br/>

## Slicing 切割
可以提取字串某部分的值<br/>
+ ### String[索引值]
    ```python
        str='Python'      
        newStr=str[2]   #這裡意指取str的第三個字 (0,1,2)
        print(newStr)   #print：t

        #可以從最後面算起取字!
        newStr=str[-2]   
        print(newStr)   #print：o
    ```
+ ### String[起始,結束,間隔]
    ```python
        str='Python'

        #間隔取字
        newStr=str[0:5:2]   #間隔概念與range相同
        print(newStr)       #print：pto

        #部分取字，間隔參數不給預設為1    
        newStr=str[2:5] #結束會在結束值「之前」，就停下，與range概念相同
        print(newStr)   #print：tho

        #起始值不給預設從頭開始取
        print(str[:3])  #print：pyt

        #結束值不給預設取到最後
        print(str[2:])  #print：thon

        #都不給就...
        print(str[:])  #print：python

        #也能從最後面取子字串
        print(str[-5:-2])   #print：yth

        #還能把字串倒著取!
        print(str[::-1])    #print：nohtyp


        #間隔為負數時，起始與結束也要反過來，意思是起始值要小於結束。        
        str='01234567'
        print(str[5:2:-1])      #print：543

        print(str[-1:-6:-1])    #print：76543
    ```
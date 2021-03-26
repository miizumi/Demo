# Class 類別
注：物件導向對有些人來說很難。

Object 是所有物件的始祖!  

類別的主要成份為二
+ Method   方法
+ Property 屬性
  
```python
    class Myclass(object):   #必須繼承一個物件，基本為object

        ix=0    #屬性
        iy=0    #相當於class的全域變數

        #初始化的方法，可以在宣告物件的時候執行內容。
        def __init__(self):  #self為指定自己本身，必定為第一個參數。
            print("物件建立成功") 

            #基本上self必打，是一種規範，但不需要帶入任何變數
        
        def SetMethod(self,x,y):   #可以帶入參數，同理init也可以。
            self.ix=x   #若要操作CLASS的屬性，要呼叫self底下的屬性。
            self.iy=y
        
```
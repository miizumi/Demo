import aiml

#宣告一個aiml的核心
kernel=aiml.Kernel()

#指定使用的XML檔案
kernel.learn('1.AIML.xml')

#無限迴圈(按Ctrl+C)
while True:
    try:
        talk=input('說話啊>>') #讓使用者輸入對話。
        response=kernel.respond(talk)   #跟據對話關鍵字取對應字串。

        #有些版本執行，出錯不會跳到except，會得到空字串。
        if response=='':    #當收到空字串時
            response="再說一次阿"

        print(response) #顯示回傳值給使用者。
    except:
        print("再說一次阿")    #找不到關鍵字給予其他回應

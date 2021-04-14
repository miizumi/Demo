import aiml

kernel=aiml.Kernel()
kernel.learn('2.AIML_Var.xml')

while True:
    try:
        talk=input('您好，有甚麼能為您服務的>>')
        response=kernel.respond(talk)

        if response=='':
            response="麻煩再說一次。"

        print(response)
    except:
        print("麻煩再說一次。")

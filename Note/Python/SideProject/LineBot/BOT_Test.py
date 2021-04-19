import aiml

kernel=aiml.Kernel()
kernel.learn('LineBot_AIML.xml')

text='學員登入'

response = kernel.respond(text)
print(response)
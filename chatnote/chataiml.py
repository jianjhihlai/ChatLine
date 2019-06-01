import aiml
import sys
import os
import glob

mybot_path = './aimldata'
#切換到語料庫所在工作目錄
os.chdir(mybot_path)

mybot = aiml.Kernel()
files = glob.glob('*.aiml')
for learn_file in files:
    mybot.learn(learn_file)
# mybot.learn("basic_chat.aiml")
# mybot.respond('load aiml b')
  
while True:
    message = input("Enter your message >> ")
    if message == "結束對話":
        exit()
    else:
        bot_response = mybot.respond(message)
    print(bot_response)



# def get_module_dir(name):
#     path = getattr(sys.modules[name], '__file__', None)
#     if not path:
#         raise AttributeError('module %s has not attribute __file__' % name)
#     return os.path.dirname(os.path.abspath(path))

# alice_path = get_module_dir('aiml') + '/botdata/alice'

# os.chdir(alice_path)

# alice = aiml.Kernel()
# alice.learn("startup.xml")
# alice.respond('LOAD ALICE')

# while True:
#     print(alice.respond(input("Enter your message >> ")))
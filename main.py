# An SMS Simulation class SMSMessage(object):
hasBeenRead = False messageText = text fromNumber = number # identify how we declare boolean , string and number variables
def __init__(self,hasBeenRead,messageText,fromNumber): 
    self.hasBeenRead = False self.messageText = text self.fromNumber = number 
def MarkASRead(self): 
    if userChoice == read: 
        self.hasBeenRead = True 

def add_sms():
def get_count():
def get_message():
def get_unread_messages():
def remove():

no_1 = SMSMessage(False, "Hello", "0798653452")
no_2 = SMSMessage(False, "WYD", "0845673864")
no_3 = SMSMessage(False, "How are you?", "0631873298")

SMSStore = [] userChoice = ""
while userChoice != "quit":
    userChoice = raw_input("What would you like to do - read/send/quit?")
    if userChoice == "read":
        # Place your logic here elif userChoice == "send": # Place your logic here elif userChoice== "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
class SMSMessage:
    def __init__(self,messageText,fromNumber): 
        self.hasBeenRead = False 
        self.messageText = messageText 
        self.fromNumber = fromNumber

    def add_sms():
        pass
    def get_count():
        pass
    def get_message():
        pass
    def get_unread_messages():
        pass
    def remove():
        pass

no_1 = SMSMessage(False, "Hello", "0798653452")
no_2 = SMSMessage(False, "WYD", "0845673864")
no_3 = SMSMessage(False, "How are you?", "0631873298")

SMSStore = [] 
userChoice = ""
while userChoice != "quit":
    userChoice = raw_input("What would you like to do - read/send/quit?")
    if userChoice == "read":
        # Place your logic here elif userChoice == "send": # Place your logic here elif userChoice== "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
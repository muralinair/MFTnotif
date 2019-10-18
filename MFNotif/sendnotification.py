import json
import smtplib


class Sendnotification():
    configarations = None
    format = {
        "info": """From: {}\n
                   To: {}\n
                   Subject: {}\n\n
                   \n Package with order ID: {} has a changed status: {}""",
        "error": """From: {}\n
                   To: {}\n
                   Subject: {}\n\n 
                   \n Package with order ID: {} has encountered Error: {}\n
                   Please find logs for additional information"""
    }

    def __init__(self):
        with open("notification.config.json", "r") as read_file:
            self.configarations = json.load(read_file)
        print(self.configarations)

    def formatMessage(self,send_to,type,OrderID,status):
        returnDict={
            "TO":"",
            "FROM":"",
            "BODY":""
        }
        SUBJECT = "MF Notification for OrderID: {}".format(OrderID)
        returnDict["TO"]=send_to
        returnDict["FROM"]=self.configarations["email"]["FROM"]
        returnDict["BODY"]=self.format[type].format(returnDict["FROM"],returnDict["TO"],SUBJECT,OrderID,status)
        return returnDict
    
    def sendEmail(self, valueDict):
        server_ssl = smtplib.SMTP_SSL(self.configarations["email"]["SMTP"], self.configarations["email"]["PORT"])
        server_ssl.ehlo()
        server_ssl.login(self.configarations["email"]["USERNAME"],self.configarations["email"]["PASSWORD"] )
        print(valueDict)
        server_ssl.sendmail(valueDict["FROM"], valueDict["TO"], valueDict["BODY"])
        server_ssl.close()


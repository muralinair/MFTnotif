import sendnotification
import MySQLdb
import time
import copy
import json


class DBMonitor():
    db = None
    c = None
    dbconfig = None

    def __init__(self):
        with open("dbconfig.json", "r") as read_file:
            self.dbconfig = json.load(read_file)
        self.db = MySQLdb.connect(
            self.dbconfig["HOST"], self.dbconfig["USERNAME"], self.dbconfig["PASSWORD"], self.dbconfig["DBNAME"])
        self.c = self.db.cursor()
        self.c.execute("""
                    DROP TRIGGER IF EXISTS insert_status_change
                    """)
        self.c.execute("""CREATE TRIGGER `insert_status_change` AFTER INSERT ON `{}`
                     FOR EACH ROW 
                     INSERT INTO {}(orderIdchange,ordersstatuschange) VALUES (NEW.ordersId,NEW.ordersStatus)
                     """.format(self.dbconfig["SOURCETABLE"], self.dbconfig["DESTINATIONTABLE"]))
        self.db.commit()
        self.c.execute("""
                    DROP TRIGGER IF EXISTS update_status_change
                    """)
        self.c.execute("""CREATE TRIGGER `update_status_change` AFTER UPDATE ON `{}`
                     FOR EACH ROW 
                     UPDATE {} SET ordersstatuschange=NEW.ordersStatus where orderIdchange=NEW.ordersId
                     """.format(self.dbconfig["SOURCETABLE"], self.dbconfig["DESTINATIONTABLE"]))
        self.db.commit()

    def startMonitor(self):
        self.c.execute("select * from dblayer_statuschangetemptable")
        data = self.c.fetchall()
        self.db.commit()
        while True:
            self.c.execute("select * from dblayer_statuschangetemptable")
            data_new = self.c.fetchall()
            time.sleep(3)
            if(data != data_new):
                s = sendnotification.Sendnotification()
                set_data = set(data)
                set_data_new = set(data_new)
                set_diff = set_data_new.difference(set_data)
                for entry in set_diff:
                    if(entry[2].lower() != "error"):
                        s.sendEmail(s.formatMessage(
                            "krishna.and.flute@gmail.com", "info", entry[1], entry[2]))
                    else:
                        s.sendEmail(s.formatMessage(
                            "krishna.and.flute@gmail.com", "error", entry[1], entry[2]))
                data = copy.deepcopy(data_new)
            self.db.commit()
        self.db.close()


if __name__ == "__main__":
    d = DBMonitor()
    d.startMonitor()

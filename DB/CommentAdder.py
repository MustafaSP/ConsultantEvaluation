import sqlite3


class CommentAdder:
    def __init__(self,name,surname,mail,consultant,commentType,commentText,orderDate,uid,dbPath):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.consultant = consultant
        self.commentType = commentType
        self.commentText = commentText
        self.orderDate = orderDate
        self.uid = uid
        self.dbPath = dbPath
        self.dbInitilazier()

    def dbInitilazier(self):
        self.Opener()
        self.conn.execute('''CREATE TABLE IF NOT EXISTS Comment
                     (
                     ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                     UID INTEGER NOT NULL,
                     Name   TEXT NOT NULL,
                     Surname    TEXT NOT NULL,
                     Mail   TEXT NOT NULL,
                     Consultant   TEXT NOT NULL,
                     CommentType   TEXT NOT NULL,
                     Comment  TEXT NOT NULL,
                     OrderDate   DATE NOT NULL
                    
                      );''')
        self.conn.commit()
        self.Closer()

    def Closer(self):
        self.conn.close()

    def Opener(self):
        self.conn = sqlite3.connect(self.dbPath)

    def commentAppend(self):
        self.Opener()
        self.conn.execute(''
                          'INSERT INTO Comment (UID,Name,Surname,Mail,Consultant,CommentType,Comment,OrderDate) \
                        VALUES ( ?,?,?,?,?,?,?,? )',
                          (self.uid, self.name, self.surname, self.mail, self.consultant, self.commentType, self.commentText, self.orderDate))
        self.conn.commit()
        self.Closer()



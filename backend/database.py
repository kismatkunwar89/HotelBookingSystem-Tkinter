import mysql.connector as ms
class DBConnect:
    def __init__(self):
        self.con=ms.connect(host='localhost',user='root',password='unostamsik',\
                            database='softwarica_hotel')
        self.cur=self.con.cursor()

    def insert(self,query,values):
        self.cur.execute(query,values)
        self.con.commit()

    def select(self,query):
        self.cur.execute(query)
        records=self.cur.fetchall()
        return records

    def update(self,query,value):
        self.cur.execute(query,value)
        self.con.commit()

    def search(self, qry):
        self.cur.execute(qry)
        return self.cur.fetchall()


    def delete(self,query,value):
        self.cur.execute(query,value)
        self.con.commit()

    def view(self, query, values=""):
        self.query = query
        self.values = values
        self.cur.execute(self.query, self.values)
        return self.cur.fetchall()

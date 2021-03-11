import mysql.connector as ms
class DBConnect:
    def __init__(self):
        self.con=ms.connect(host='localhost',user='root',password='unostamsik',\
                            database='kkk')
        self.cur=self.con.cursor()

    def insert(self,query,values):
        """
                       Function to do insert in a database.
                       :param query:
                       :type query:
                       :param values:
                       :type values:
               """
        self.cur.execute(query,values)
        self.con.commit()

    def select(self,query):
        """
                        Function to select data.
                        :param query:
                        :type query:
                        :param values:
                        :type values:
                        :rtype: list:
                """
        self.cur.execute(query)
        records=self.cur.fetchall()
        return records

    def update(self,query,value):
        """
                        Function to do update in a database.
                        :param query:
                        :type query:
                        :param values:
                        :type values:
                """
        self.cur.execute(query,value)
        self.con.commit()


    def delete(self,query,value):
        """
                        Function to do delete in a database.
                        :param query:
                        :type query:
                        :param values:
                        :type values:
                """
        self.cur.execute(query,value)
        self.con.commit()

    def view(self, query, values=""):
        self.query = query
        self.values = values
        self.cur.execute(self.query, self.values)
        return self.cur.fetchall()

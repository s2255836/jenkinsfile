import pymysql
# table create


class SQLPLAY():
    '''這是一個叫做 SQLPLAY 的類別'''

    def __init__(self):
        '''這是一個初始化'''
        Connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='demo'
        )
        self.cursor = Connection.cursor()

    def create(self):
        '''這是一個表'''
        sql = """CREATE TABLE users(
                id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(20),
                password VARCHAR(20))"""
        self.cursor.execute(sql)
        self.Connection.commit()
        self.Connection.close()

    def insert(self):
        '''這是一個插入'''
        # insert data into table
        sql = "INSERT INTO users(username, password) VALUES (%s, %s)"
        for i in range(0, 3):
            self.cursor.execute(sql, ('user' + str(i), 'password' + str(i)))
            self.Connection.commit()
        self.Connection.close()

    def get(self):
        '''這是一個查表'''
        # select data
        sql = "SELECT id, username from users"
        self.cursor.execute(sql)
        while True:
            result = self.cursor.fetchone()  # fetchall()
            if not result:
                break
            print(result)
        self.Connection.close()

    def update(self, password, user):
        '''這是一個更新'''
        # update
        sql = "update users set password=%s where username=%s"
        self.cursor.execute(sql, (password, user))
        self.Connection.commit()
        self.Connection.close()

    def remove(self, userid):
        '''這是一個刪除'''
        # delete
        sql = 'DELETE from users where id=%s'
        self.cursor.execute(sql, (userid,))
        self.Connection.commit()
        self.Connection.close()

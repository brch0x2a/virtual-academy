import pymysql

IP = "localhost"
PASS = "wrf!C:w(>7:&"


db = pymysql.connect(IP, "brch", PASS, "mes")


class User_table:
    def __init__(self, nick_name, email, password):
        self.nick_name = nick_name
        self.email = email
        self.password = password

    def create(pnick_name,  pemail, ppassword):

        db = pymysql.connect(IP, "brch", PASS, "academy")

        nick_name = str(pnick_name)
        email = str(pemail)
        password = str(ppassword)

        cursor = db.cursor()

        sql = "INSERT INTO User_table(fname, email, password)"\
            "Values(%s, %s, %s)"

        cursor.execute(sql, (nick_name, email, password))

        db.commit()

        cursor.close()

        db.close()


        return "Listo"






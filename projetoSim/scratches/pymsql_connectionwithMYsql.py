import pymysql
from projetoSim.scratches import secrets


def mysqlConn():
    dbConn = pymysql.connect(
        host='localhost',
        user='root',
        password=secrets.password,
        db='simChallenge')

    cur = dbConn.cursor()
    cur.execute('select * from equipes')
    res = cur.fetchall()
    print(res)
    dbConn.close()

if __name__ == '__main__':
    mysqlConn()

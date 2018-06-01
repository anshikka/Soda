import MySQLdb as sql

def connectToSQLdb(host, user, paswd, db):
    db = sql.connect(host, user, paswd, db, charset = 'utf8mb4')
    db.autocommit(True)
    return db

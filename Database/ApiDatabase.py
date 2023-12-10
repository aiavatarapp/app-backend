import psycopg2
import numpy as np
from flask import Flask, jsonify, request


def createDatabase():
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")
    cur = conn.cursor()
    cur.execute(''' 
       CREATE TABLE IF NOT EXISTS USERS(
      id SERIAL PRIMARY KEY,
      andoridUUID    varchar,
      email       varchar,
      lifeTime       varchar,
      coin       varchar,
      purchaseToken       varchar,
      timeStamp       varchar
      )''')
    conn.commit()
    conn.close()
    print("successful database")

def showAllData():
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS;")
    results = cur.fetchall()

    resultMap = {
        "data": []
    }
    arr = np.array(results)

    # count
    cur.execute("select count(*) from USERS")
    count = cur.fetchone()[0]

    for k in range(0, count):
        resultMap["data"].append({
            "id": arr[k][0],
            "andoridUUID": arr[k][1],
            "email": arr[k][2],
            "lifeTime": arr[k][3],
            "coin": arr[k][4],
            "purchaseToken": arr[k][5],
            "timeStamp": arr[k][6],
        })
    return resultMap

def userPurchaseSearch(purchaseToken):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")
    cur = conn.cursor()

    cur.execute("SELECT * FROM USERS WHERE purchaseToken = %s", [purchaseToken])

    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    for k in rows:
        myMap["data"].append({
            "id": k[0],
            "andoridUUID": k[1],
            "itemType": k[2],
            "itemMaxCount": k[3],
            "itemCurrentSize": k[4],
            "purchaseToken": k[5],
        })
    return myMap

    conn.close()
    return "hata"

def searchPurchaseTokenForDeleteFunc(purchaseToken):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")


    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE purchaseToken = %s", [purchaseToken])
    rows = cur.fetchall()
    for k in rows:
        print("search verisi " + k[5])
        conn.close()
        return k[5]


def userPurchaseDelete(purchaseToken):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")
    cur = conn.cursor()

    if searchPurchaseTokenForDeleteFunc(purchaseToken) == purchaseToken:
        cur.execute("DELETE FROM USERS WHERE purchaseToken = %s ", [purchaseToken])
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False


# en son Burda kalındı purchaseToken göre kullanıcının itemCurrentSize 1 artır
# burda update postgre sql de update işlemi yapılcak
def userItemCurrentSizePlusFunc(purchaseToken, isReset):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE purchaseToken = %s", [purchaseToken])
    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    for k in rows:
        myMap["data"].append({
            "id": k[0],
            "andoridUUID": k[1],
            "itemType": k[2],
            "itemMaxCount": k[3],
            "itemCurrentSize": k[4],
            "purchaseToken": k[5],
        })

    # kullanıcının itemCurrentSize 1 artırmak için
    myCountStr = str(int(rows[0][4]) + 1)

    # kullanıcının itemCurrentSize sıfırlamak için
    if isReset == "true":
        myCountStr = 0

    print(myCountStr)
    # update işlemini burda yapıcaz
    cur.execute("UPDATE USERS set itemCurrentSize = %s where purchaseToken = %s", [myCountStr, rows[0][5]])
    conn.commit()

    conn.close()
    return True


############################### New Path is here ##########################


def UserEmailGetAllField(email):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = %s", [email])
    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    for k in rows:
        myMap["data"].append({
            "id": k[0],
            "andoridUUID": k[1],
            "email": k[2],
            "lifeTime": k[3],
            "coin": k[4],
            "purchaseToken": k[5],
            "timeStamp": k[6],
        })
        return myMap

    conn.close()
    myMap = {
        "data": [

        ]
    }

    myMap["data"].append({
        "id": "false",
        "andoridUUID": "false",
        "email": "false",
        "lifeTime": "false",
        "coin": "false",
        "purchaseToken": "false",
        "timeStamp": "false",
    })
    return myMap


def insertDatabase(andoridUUID, email, lifeTime, coin, purchaseToken, timeStamp):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO USERS (andoridUUID, email, lifeTime, coin, purchaseToken, timeStamp) VALUES (%s, %s, %s, %s, %s, %s )",
        (andoridUUID, email, lifeTime, coin, purchaseToken, timeStamp))
    conn.commit()
    conn.close()
    print("Insert Succesful")


def deleteCoin(email, isReset):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")

    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = %s", [email])
    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    for k in rows:
        myMap["data"].append({
            "id": k[0],  # 1
            "andoridUUID": k[1],  # 344f1e68032f1b5c
            "email": k[2],  # test@gmail.com
            "lifeTime": k[3],  # false
            "coin": k[4],  # 500
            "purchaseToken": k[5],  # pdoimjkomfghgnphndgmdpip.AOadmflkad
            "timeStamp": k[6],  # 232425356
        })

    # kullanıcının itemCurrentSize 1 artırmak için
    myCountStr = str(int(rows[0][4]) - 1)

    # kullanıcının itemCurrentSize sıfırlamak için
    if isReset == "true":
        myCountStr = 0

    print(myCountStr)
    # update işlemini burda yapıcaz
    cur.execute("UPDATE USERS set coin = %s where andoridUUID = %s", [myCountStr, rows[0][1]])
    conn.commit()

    conn.close()
    return True


def deleteLifetimeFunc(email, isReset):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")


    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = %s", [email])
    rows = cur.fetchall()

    myMap = {
     "data": [
     ]
    }

    for k in rows:
        myMap["data"].append({
        "id": k[0],  # 1
        "andoridUUID": k[1],  # 344f1e68032f1b5c
        "email": k[2],  # test@gmail.com
        "lifeTime": k[3],  # false
        "coin": k[4],  # 500
        "purchaseToken": k[5],  # pdoimjkomfghgnphndgmdpip.AOadmflkad
        "timeStamp": k[6],  # 232425356
    })

# kullanıcının itemCurrentSize 1 artırmak için
    myCountStr = str(int(rows[0][4]) - 1)

# kullanıcının itemCurrentSize sıfırlamak için
    if isReset == "true":
        myCountStr = 0

    print(myCountStr)
    # update işlemini burda yapıcaz
    cur.execute("UPDATE USERS set lifeTime = %s where andoridUUID = %s", ["false", rows[0][1]])
    conn.commit()

    conn.close()
    return True


def addCoin(email, isReset, newCoinCount):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")


    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = %s", [email])
    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    for k in rows:
        myMap["data"].append({
        "id": k[0],  # 1
        "andoridUUID": k[1],  # 344f1e68032f1b5c
        "email": k[2],  # test@gmail.com
        "lifeTime": k[3],  # false
        "coin": k[4],  # 500
        "purchaseToken": k[5],  # pdoimjkomfghgnphndgmdpip.AOadmflkad
        "timeStamp": k[6],  # 232425356
    })

# kullanıcının itemCurrentSize 1 artırmak için
    newCoinSize = int(newCoinCount)
    rowCurrentSize = int(rows[0][4])
    myCountStr = str(rowCurrentSize + newCoinSize)

# kullanıcının itemCurrentSize sıfırlamak için
    if isReset == "true":
        myCountStr = 0

# update işlemini burda yapıcaz
    cur.execute("UPDATE USERS set coin = %s where email = %s", [myCountStr, rows[0][2]])
    conn.commit()

    conn.close()
    return True


def addLifetime(email, isReset):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")


    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = %s", [email])
    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    for k in rows:
        myMap["data"].append({
        "id": k[0],  # 1
        "andoridUUID": k[1],  # 344f1e68032f1b5c
        "email": k[2],  # test@gmail.com
        "lifeTime": k[3],  # false
        "coin": k[4],  # 500
        "purchaseToken": k[5],  # pdoimjkomfghgnphndgmdpip.AOadmflkad
        "timeStamp": k[6],  # 232425356
    })

# kullanıcının itemCurrentSize 1 artırmak için
# newCoinSize = int(newCoinCount)
# rowCurrentSize = int(rows[0][4])
# myCountStr = str (rowCurrentSize + newCoinSize)

# kullanıcının itemCurrentSize sıfırlamak için
    if isReset == "true":
        myCountStr = 0

# update işlemini burda yapıcaz
    cur.execute("UPDATE USERS set lifeTime = %s where email = %s", ["lifetime", rows[0][2]])
    conn.commit()

    conn.close()
    return "true"


def addTimeStamp(email, isReset, timeStamp):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")


    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = %s", [email])
    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    for k in rows:
        myMap["data"].append({
        "id": k[0],  # 1
        "andoridUUID": k[1],  # 344f1e68032f1b5c
        "email": k[2],  # test@gmail.com
        "lifeTime": k[3],  # false
        "coin": k[4],  # 500
        "purchaseToken": k[5],  # pdoimjkomfghgnphndgmdpip.AOadmflkad
        "timeStamp": k[6],  # 232425356
    })

# kullanıcının itemCurrentSize 1 artırmak için
# newCoinSize = int(timeStamp)
# rowCurrentSize = int(rows[0][6])
    myCountStr = str(timeStamp)

# kullanıcının itemCurrentSize sıfırlamak için
    if isReset == "true":
        myCountStr = 0

# update işlemini burda yapıcaz
    cur.execute("UPDATE USERS set timeStamp = %s where email = %s", [myCountStr, rows[0][2]])
    conn.commit()

    conn.close()
    return True


def searchAndoridUUIDFunc(andoridUUID):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")


    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE andoridUUID = %s", [andoridUUID])
    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    print(rows)
    if str(rows) != "[]":
        for k in rows:
            myMap["data"].append({
            "id": k[0],
            "andoridUUID": k[1],
            "email": k[2],
            "lifeTime": k[3],
            "coin": k[4],
            "purchaseToken": k[5],
            "timeStamp": k[6],
        })
    if andoridUUID == myMap["data"][0]["andoridUUID"]:
        return "true"
    conn.close()
    return "false"


def searchEmailFunc(email):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")


    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = %s", [email])
    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    print(rows)
    if str(rows) != "[]":
        for k in rows:
            myMap["data"].append({
            "id": k[0],
            "andoridUUID": k[1],
            "email": k[2],
            "lifeTime": k[3],
            "coin": k[4],
            "purchaseToken": k[5],
            "timeStamp": k[6],
        })
    if email == myMap["data"][0]["email"]:
        return "true"
    conn.close()
    return "false"


def searchCoinFunc(email):
    conn = psycopg2.connect(database="d5mkgv5966rr8l",
                            user="yrauvzjaoldxwx",
                            password="e33f6020bd0e0fa7db65c505e448b99c4741ae3726dbe5ac712dbe9fd2cb2d93",
                            host="ec2-54-73-22-169.eu-west-1.compute.amazonaws.com",
                            port="5432")


    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = %s", [email])
    rows = cur.fetchall()

    myMap = {
        "data": [
        ]
    }

    print(rows)
    if str(rows) != "[]":
        for k in rows:
            myMap["data"].append({
            "id": k[0],
            "andoridUUID": k[1],
            "email": k[2],
            "lifeTime": k[3],
            "coin": k[4],
            "purchaseToken": k[5],
            "timeStamp": k[6],
        })

    conn.close()
    return myMap["data"][0]["coin"]

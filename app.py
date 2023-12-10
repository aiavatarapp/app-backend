from Database import ApiDatabase
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#PASSED
ApiDatabase.createDatabase()
personList = []



########################################## REAL FIELD ##########################################################################


#PASSED FOR LOCAL
@app.route("/")
def root_folder():
    return jsonify("working now :)")

#PASSED FOR LOCAL
@app.route("/GetAllUser")
def showData_folder():
    veri = ApiDatabase.showAllData()
    return jsonify(veri)

#PASSED FOR LOCAL
@app.route("/CreateUser", methods=['POST'])
def CreateUser():
    request_data = request.data  # getting the response data
    request_data = json.loads(request_data.decode('utf-8'))  # converting it from json to key value pair

    #create Field
    andoridUUID = request_data["andoridUUID"]
    email = request_data["email"]
    lifeTime = request_data["lifeTime"]
    coin = request_data["coin"]
    purchaseToken = request_data["purchaseToken"]
    timeStamp = request_data["timeStamp"]


    #Insert Database
    ApiDatabase.insertDatabase(andoridUUID=andoridUUID,email=email,lifeTime=lifeTime,coin=coin,purchaseToken=purchaseToken,timeStamp=timeStamp)

    personList.clear()
    personList.append(andoridUUID)
    personList.append(email)
    personList.append(lifeTime)
    personList.append(coin)
    personList.append(purchaseToken)
    personList.append(timeStamp)

    myMap = {
        "data": [
        ]
    }

    myMap["data"].append({
    "andoridUUID": andoridUUID,
    "email": email,
    "lifeTime": lifeTime,
    "coin": coin,
    "purchaseToken": purchaseToken,
    "timeStamp": timeStamp,
        })

    return jsonify(myMap)

#PASSED FOR LOCAL -AndoridUUIDGetData VERINCE KULLANICININ TUM BILGILERI GELIR
@app.route("/UserEmailGetAllField",methods=['GET', 'POST'])
def UserEmailGetAllField():
    request_data = request.data  # getting the response data
    request_data = json.loads(request_data.decode('utf-8'))  # converting it from json to key value pair
    email = request_data["email"]
    #timeStamp geri göndercek bu timeStamp
    return jsonify(ApiDatabase.UserEmailGetAllField(email))

#PASSED FOR LOCAL -AndoridUUIDGetData VERINCE UUID VARmı DIYE SORGULAR
@app.route("/AndoridUUIDSearchData",methods=['GET', 'POST'])
def AndoridUUIDSearchData():
    request_data = request.data  # getting the response data
    request_data = json.loads(request_data.decode('utf-8'))  # converting it from json to key value pair
    andoridUUID = request_data["andoridUUID"]
    #timeStamp geri göndercek bu timeStamp
    return jsonify(result = ApiDatabase.searchAndoridUUIDFunc(andoridUUID))

#PASSED FOR LOCAL -EMAIL VERINCE  VARmı DIYE SORGULAR TRUE YADA FALSE DONDURUR
@app.route("/SearchEmailFunc",methods=['GET', 'POST'])
def SearchEmailFunc():
    request_data = request.data  # getting the response data
    request_data = json.loads(request_data.decode('utf-8'))  # converting it from json to key value pair
    email = request_data["email"]
    #timeStamp geri göndercek bu timeStamp
    return jsonify(result = ApiDatabase.searchEmailFunc(email))

#PASSED FOR LOCAL
@app.route("/AddCoin",methods=['GET', 'POST'])
def AddCoin():
    request_data = request.data
    request_data = json.loads(request_data.decode('utf-8'))
    email = request_data["email"]
    isReset = request_data["isReset"]
    newCoinCount = request_data["newCoinCount"]
    # sqlden silinirse true yada false döndürcek
    return jsonify(result=ApiDatabase.addCoin(email,isReset,newCoinCount))

#PASSED FOR LOCAL
@app.route("/AddLifetime",methods=['GET', 'POST'])
def AddLifetime():
    request_data = request.data
    request_data = json.loads(request_data.decode('utf-8'))
    email = request_data["email"]
    isReset = request_data["isReset"]
    return jsonify(result=ApiDatabase.addLifetime(email,isReset))

#PASSED FOR LOCAL
@app.route("/AddTimeStamp",methods=['GET', 'POST'])
def AddTimeStamp():
    request_data = request.data
    request_data = json.loads(request_data.decode('utf-8'))
    email = request_data["email"]
    isReset = request_data["isReset"]
    timeStamp = request_data["timeStamp"]
    # sqlden silinirse true yada false döndürcek
    return jsonify(result=ApiDatabase.addTimeStamp(email,isReset,timeStamp))

#PASSED FOR LOCAL
@app.route("/DeleteCoin",methods=['GET', 'POST'])
def DeleteCoin():
    request_data = request.data
    request_data = json.loads(request_data.decode('utf-8'))
    email = request_data["email"]
    isReset = request_data["isReset"]
    # sqlden silinirse true yada false döndürcek
    return jsonify(result=ApiDatabase.deleteCoin(email,isReset))

@app.route("/DeleteLifetimeUser",methods=['GET', 'POST'])
def DeleteLifetimeUser():
    request_data = request.data
    request_data = json.loads(request_data.decode('utf-8'))
    email = request_data["email"]
    isReset = request_data["isReset"]
    # sqlden silinirse true yada false döndürcek
    return jsonify(result=ApiDatabase.deleteLifetimeFunc(email,isReset))


#PASSED FOR LOCAL
@app.route("/SearchCoin",methods=['GET', 'POST'])
def SearchCoin():
    request_data = request.data
    request_data = json.loads(request_data.decode('utf-8'))
    email = request_data["email"]
    # sqlden silinirse true yada false döndürcek
    return jsonify(result=ApiDatabase.searchCoinFunc(email))




# heroku ya yuklerken  app.run() yap !!
if __name__ == "__main__":
    app.run()














@app.route("/userPurchaseSearch",methods=['GET', 'POST'])
def userPurchaseSearchFunc():
    request_data = request.data  # getting the response data
    request_data = json.loads(request_data.decode('utf-8'))  # converting it from json to key value pair
    purchaseToken = request_data["purchaseToken"]
    #timeStamp geri göndercek bu timeStamp
    return jsonify(result = ApiDatabase.userPurchaseSearch(purchaseToken))

@app.route("/userPurchaseDelete",methods=['GET', 'POST'])
def userPurchaseDeleteFunc():
    request_data = request.data
    request_data = json.loads(request_data.decode('utf-8'))
    purchaseToken = request_data["purchaseToken"]
    # sqlden silinirse true yada false döndürcek
    return jsonify(result=ApiDatabase.userPurchaseDelete(purchaseToken))

@app.route("/userItemCurrentSizePlus",methods=['GET', 'POST'])
def userItemCurrentSizePlusFunc():
    request_data = request.data
    request_data = json.loads(request_data.decode('utf-8'))
    purchaseToken = request_data["purchaseToken"]
    isReset = request_data["isReset"]
    # sqlden silinirse true yada false döndürcek
    return jsonify(result=ApiDatabase.userItemCurrentSizePlusFunc(purchaseToken,isReset))




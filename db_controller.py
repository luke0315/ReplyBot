import  pymongo
from bson.objectid import ObjectId
import json,time
import os
#上一層目錄
path= os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)) 

with open(path+'\\mongodbURL.json', "r", encoding = "utf8") as file:
    data = json.load(file)
client = pymongo.MongoClient(data['url'])
db = client.Banana
coll_api = db.api
coll_keyword = db.keyword


#新增資料
#coll_keyword.insert_one({'keyword':'apple','reply':'趕快下船啦幹'}) 

#搜尋token
def find_api_token():
    result = coll_api.find_one()
    return result

#搜尋keyword
def find_keyword_reply(keyWord):
    myKeyword=keyWord
    if coll_keyword.find_one({"keyword":{"$regex":myKeyword}}):#判斷資料庫內是否有關鍵字
        result = coll_keyword.find_one({"keyword":{"$regex":myKeyword}})
        resultReply = result['reply']
        return resultReply
def find_keyword(keyWord):
    myKeyword=keyWord
    
    for i in coll_keyword.find():
        dbkeyword=i['keyword']
        if dbkeyword in myKeyword:
            result = coll_keyword.find_one({"keyword":{"$regex":dbkeyword}})
            resultReply = result['reply']
            print(resultReply)
            return resultReply





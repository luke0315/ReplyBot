import  pymongo
from bson.objectid import ObjectId
import json,time

client = pymongo.MongoClient("mongodb+srv://banana:bananana@discordbanana.3sz82.mongodb.net/?retryWrites=true&w=majority")
db = client.Banana
coll_api = db.api
coll_keyword = db.keyword


#新增資料
#coll_keyword.insert_one({'keyword':'安安 嗨 hi','reply':'吵阿小'}) 

#搜尋token
def find_api_token():
    result = coll_api.find_one()
    return result

#搜尋keyword
def find_keyword_reply(keyWord):
    myKeyword=keyWord

    result = coll_keyword.find_one({"keyword":{"$regex":myKeyword}})
    resultReply = result['reply']
    return resultReply

print(find_keyword_reply('hi')) #測試
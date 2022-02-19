from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.4mjjk.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'bob',
    'age':27
}

db.users.insert_one(doc)
import pymongo
import dns # required for connecting with SRV
from config.config import cfg 

client = pymongo.MongoClient(f'mongodb+srv://{cfg.data["db_username"]}:{cfg.data["db_password"]}@sdpbot-db-p6xgc.mongodb.net/sdpbot_db?retryWrites=true&w=majority')
db = client.sdpbot_db

# jojo = db.jojo

# cur = jojo.find()
# for doc in cur:
#     print(doc['stands']) 
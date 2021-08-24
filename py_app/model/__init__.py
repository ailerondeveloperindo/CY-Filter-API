import pymongo
import ..config as cfg

class DB_PYMONGO:
    def CreateClientObject(self)
        return MongoClient(cfg.DATABASE_HOST,cfg.DATABASE_HOST_PORT)

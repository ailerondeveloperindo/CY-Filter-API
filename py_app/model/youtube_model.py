from pymongo import MongoClient
from config import Config

class Youtube_Model:

    def __init__(self):
        cfg = Config()
        # initialize a Mongo Client Object
        self.mongo_client = MongoClient(cfg.DATABASE_HOST,cfg.DATABASE_HOST_PORT)
        
        # initialize an object that points to Youtube Collection on Database
        self.youtube_col = self.mongo_client.cy_filter.Youtube

    def get_devkey(self):
        # returns api_key from youtube collection
        return self.youtube_col.find_one()['api_key']

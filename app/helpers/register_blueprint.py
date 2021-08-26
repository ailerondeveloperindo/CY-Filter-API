import sys
import os
import importlib

class Register_Blueprint:

    # blueprint_list_obj = views object from config.py
    def __init__(self, flask_app_obj, blueprint_list_obj):
        self.bl_ls_obj = blueprint_list_obj
        self.fl_obj = flask_app_obj
        self.import_blueprint()
    
    def import_blueprint(self):

        # iterates through config.py's views and import view module based on it's naming
        for blueprint in self.bl_ls_obj:
            module = importlib.import_module('views.' + blueprint, blueprint)
            self.fl_obj.register_blueprint(getattr(module, blueprint))

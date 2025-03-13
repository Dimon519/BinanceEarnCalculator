import json
import os

class Settings():
    def __init__(self):
        self.api_key = None
        self.api_secret = None
        self.auto_convert = False
        self.profit = 0
        self.load_settings()

    
    def build_data(self):
        data = {
            'secret1': self.api_key,
            'secret2': self.api_secret,
            'convert': self.auto_convert
        }
        return data
        
    def writer(self):
        with open("setting.json", "w") as file:
            json.dump(self.build_data(), file, indent= 4)

    def load_settings(self):
        if not os.path.exists("setting.json"):
            return [False]
        
        with open("setting.json", "r") as file:
            data = json.load(file)

        self.api_key, self.api_secret, self.auto_convert = data['secret1'], data['secret2'], data['convert'] 

        return [True, self.api_key, self.api_secret, self.auto_convert]         
    
    def update_settings(self, *args):
        self.api_key, self.api_secret, self.auto_convert = args[0], args[1], args[2]
        self.writer()
    
    def update_convert(self, *args):
        self.auto_convert = args[0]
        self.writer()
    
    def clear_settings(self):
        self.api_key, self.api_secret, self.auto_convert = '', '', False
        self.writer()
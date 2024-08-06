from src.ABC.ObjectAbstract import ObjectAbstract
from flask import jsonify
from datetime import datetime
from src.utils.ErrorCodeFactory import ErrorCodeFactory


error_code_factory = ErrorCodeFactory()

class ResponeTemplate(ObjectAbstract):
    def __init__(self, request_trans_id: str, code: int, data: dict, reponse_time = None) -> None:
        if code is None:
            raise ValueError("The code must not be None")
        if data is None:
            raise ValueError("The data must not be None")
        if reponse_time is None:
            reponse_time = datetime.now()
        
        self.code, self.message = error_code_factory.get_error_code(code)
        self.data = data
        self.reponse_time = reponse_time.strftime("%Y-%m-%d %H:%M:%S")
        self.request_trans_id = request_trans_id
        super().__init__()
        
    def to_dict(self):
        return {
            "code":self.code,
            "message":self.message,
            "reponse_time":self.reponse_time,
            "request_trans_id":self.request_trans_id,
            "data":self.data,
        }
    
    
    def to_jsonify(self):
        return jsonify(self.to_dict())

from src.utils.load_config import load_error_code

class ErrorCodeFactory(object):
    def __init__(self, *args):
        self.error_code_mapping = {100: "Error when get error code"}
        self.load_mapping_error_code()
        

    def get_error_code(self, code: int):
        code = code if code in self.error_code_mapping else 100
        return code, self.error_code_mapping.get(code)

    def load_mapping_error_code(self):
        conf = load_error_code()
        if  conf:
            for key in conf:
                self.error_code_mapping[key] = conf.get(key)
        pass
    
        
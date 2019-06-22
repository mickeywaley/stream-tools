import json


class Result:

    def __init__(self, success=True, data=None, message=None):

        self.success = success
        self.data = data
        self.message = message

    def to_json(self):
        return json.dumps({
            "success": self.success,

            "data": self.data,

            "message": self.message
        })

    @staticmethod
    def gen_success(data, message = None):
        ret = Result(success=True, data = data, message=message)
        return ret.to_json()

    @staticmethod
    def gen_fail(data, message=None):
        ret = Result(success=False, data=data, message=message)
        return ret.to_json()

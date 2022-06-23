import json
import logging

from common.Mylogging import MyLogger


class checkBack:
    back = None
    mylog = MyLogger()
    mylog.create_logger()

    def __init__(self, back):
        self.back = back

    def check_param(self, level=0, url=None, expect_result=None):
        try:
            self.assertEqual(200, self.back.status_code)
        except AssertionError as ae:
            logging.error("{}请求错误返回结果是:{}".format(url, self.back.text))
            return "error"
        if level == 1:
            try:
                json_response = json.loads(self.back.text)
                self.assertEqual(0, json_response["result"])
            except AssertionError as ae:
                logging.error("{}请求返回结果result不符合预期:{}".format(url, self.back.text))
                return "error"
        elif level == 2:
            try:
                json_response = json.loads(self.back.text)
                self.assertEqual(expect_result, json_response)
            except AssertionError as ae:
                logging.error("{}请求返回结果是:{},预期返回结果:{}".format(url, self.back.text, expect_result))
                return "error"
        return "successful"

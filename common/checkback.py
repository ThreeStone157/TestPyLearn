import json
import logging

from common.mylogging import MyLogger


# 接口返回校验类 分为3级：0级是只校验返回的状态200，1级是校验部分的字段数据，2级是校验返回和配置预期返回是否一致
class CheckBack:
    back = None
    my_log = MyLogger()
    my_log.create_logger()

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
        return "success_back"

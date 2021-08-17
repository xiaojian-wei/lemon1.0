# -*- coding: utf-8 -*-
# @Author:ASUS
# @File :run.py
# @Software :PyCharm
# @Time :2021/8/15 22:04

# 完整的接口自动化测试
from common.method import read_case, api_func, write


def execute_func(fileName, sheetName, cloumn):
    cases = read_case(fileName, sheetName)
    for case in cases:
        case_id = case.get('case_id')
        case_url = case.get('url')
        # eval函数 --运行被字符串包裹的Python表达式
        # 拓展：eval("3+2") 运行被字符串包裹的Python表达式 结果为5
        case_data = eval(case.get('data'))
        case_expect = eval(case.get('expect'))

        # 获取期望code、msg信息
        expect_code = case_expect['code']
        expect_msg = case_expect['msg']
        print('预期结果：code为{}，msg为{}'.format(expect_code, expect_msg))

        # 调用接口
        real_result = api_func(url=case_url, data=case_data)
        # 获取实际的code、msg
        real_code = real_result['code']
        real_msg = real_result['msg']
        print('实际结果：code为{}，msg为{}'.format(real_code, real_msg))

        # 断言
        if expect_code == real_code and expect_msg == real_msg:
            print('第{}条测试用例执行通过'.format(case_id))
            final_re = 'Passed'
        else:
            print('第{}条测试用例执行不通过'.format(case_id))
            final_re = 'Failed'
        print('*' * 30)

        # 写入最终的测试结果到excel
        write(fileName, sheetName, case_id + 1, cloumn, final_re)


# 调用execute_func函数执行接口用例自动化测试
# 注册
# execute_func('../test_data/testcase_api_wuye.xlsx', 'register', 8)
# 登录
execute_func('C:\\Users\\ASUS\\.jenkins\\workspace\\scb22\\test_data\\testcase_api_wuye.xlsx', 'login', 8)

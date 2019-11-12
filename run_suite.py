import unittest

from app import PRO_PATH
from case.test_ihrm_employee import TestEMP
from case.test_ihrm_login import TestLogin
# from HTMLTestRunner import HTMLTestRunner
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(TestLogin('test_login_success'))#登陆

suite.addTest(TestEMP('test_emp_add'))#添加员工
suite.addTest(TestEMP('test_emp_update'))#修改员工
suite.addTest(TestEMP('test_emp_get'))#查询员工
suite.addTest(TestEMP('test_emp_delete'))#删除员工



# runner = unittest.TextTestRunner()
# runner.run(suite)

#生成测试报告
with open(PRO_PATH+"/report/report.html","wb")as f:
    runner = HTMLTestRunner(f,title="人力资源管理系统测试报告",description="测试了员工模块的曾删改查相关接口")
    runner.run(suite)



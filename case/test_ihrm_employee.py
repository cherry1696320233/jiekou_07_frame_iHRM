import logging
import unittest
import requests

import app
from api.employeeAPI import EmployeeDeal



class TestEMP(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.Emp_Deal = EmployeeDeal()

    def tearDown(self):
        pass
    #case增
    def test_emp_add(self):
        logging.info("增加员工")
        response = self.Emp_Deal.add_emp_func(self.session,username="908fjfia",
                                               mobile="150890890712",)
        #获取新增员工的id
        id = response.json().get("data").get("id")
        #把id赋值给app问价里的ID
        app.ID = id
        print(response.json())#.{'success': True, 'code': 10000, 'message': '操作成功！',
        #  'data': {'id': '1193825341986394112'}}

        #断言
        self.assertEqual(True,response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功",response.json().get("message"))
    #case改
    def test_emp_update(self):
        logging.info("更改员工")
        response = self.Emp_Deal.update_emp_func(self.session,app.ID,"jdimaing")
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
    #case查
    def test_emp_get(self):
        logging.info("查询员工")
        response= self.Emp_Deal.get_emp_func(self.session,app.ID)
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
    #case删
    def test_emp_delete(self):
        logging.info("删除员工")
        response= self.Emp_Deal.delete_emp_func(self.session,app.ID)
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))





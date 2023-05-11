import unittest
from ..api.employee import EmployeeAPI

# 创建员工测试类
class TestEmployee(unittest.TestCase):
    employee_id = None

    # 前置处理
    def setUp(self):
        self.employee_api = EmployeeAPI()

    # 后置处理
    # def teardown(self):
    #     pass

    def test02_add_employee(self):
        add_employee_data = {
            "username": "jack0709t0728004",  # 用户名唯一
            "mobile": "13212072804",  # 手机号唯一
            "timeOfEntry": "2020-07-09",
            "formOfEmployment": 1,
            "workNumber": "072804",  # 员工ID唯一性
            "departmentName": "销售",
            "departmentId": "1266699057968001024",
            "correctionTime": "2020-07-30T16:00:00.000Z"
        }
        # 获取相应结果
        response = self.employee_api.add_employee(add_employee_data=add_employee_data)
        print(response.json())

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

        # 提取员工ID 后面查询、修改、删除会用到
        # response.json():"{"data":{"id":"123"}}"
        TestEmployee.employee_id = response.json().get("data").get("id")
        print(TestEmployee.employee_id)

        # todo








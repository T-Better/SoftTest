import unittest
import requests
from .. import app

# 创建接口类
class EmployeeAPI:
    # 初始化employeeapi所用到的url
    def __init__(self):
        self.url_add_employee = app.BASE_URL + "/api/sys/user"
        self.url_update_employee = app.BASE_URL + "/api/sys/user/{}"
        self.url_get_employee = app.BASE_URL + "/api/sys/user/{}"
        self.url_delete_employee = app.BASE_URL + "/api/sys/user/{}"

    # 添加员工
    def add_employee(self, add_employee_data):  # TODO headers_data
        return requests.post(url = self.url_add_employee, json = add_employee_data, headers = app.headers_data)

    # 员工修改
    def update_employee(self, employee_id, update_data):
        url = self.url_update_employee.format(employee_id)
        return requests.put(url=url, json = update_data, headers = app.headers_data)

    # 员工删除
    def delete_employee(self, employee_id):
        url = self.url_update_employee.format(employee_id)
        return requests.delete(url=url, headers = app.headers_data)









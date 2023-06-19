
# 公共断言方法
def common_assert(case, response, status_code=200, success=True, code=10000, message="操作成功"):
    """
    需要断言状态码、响应结果、响应码、响应的message
    case:login.json中的每个case,这里case对应的是self
    """
    case.assertEqual(status_code, response.status_code)
    case.assertEqual(success, response.json().get("success"))
    case.assertEqual(code, response.json().get("code"))
    case.assertIn(message, response.json().get("message"))

# 公共断言方法
def common_assert(case, response,status_code=200, success=True,code=10000,message="操作成功"):
    case.assertEqual(status_code, response.status_code)
    case.assertEqual(success, response.json().get("success"))
    case.assertEqual(code, response.json().get("code"))
    case.assertIn(message, response.json().get("message"))








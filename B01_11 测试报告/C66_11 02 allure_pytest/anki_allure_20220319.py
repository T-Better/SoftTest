import allure

@allure.attach('在fixture前置操作里面添加一个附件txt','fixture迁至附件',allure.attachment_ytpe.txt)
def attach_file_in_module_scope_fixture_with_finalizer(request):
    pass













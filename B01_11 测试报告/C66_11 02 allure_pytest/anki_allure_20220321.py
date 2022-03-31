import allure

@allure.attach()
def attach_file_in_module_scope_fixture_with_finalizer(request):
    pass

@allure.attach.file('./reports.html',attachment_type=allure.attachment_type.HTML)
def test_multiple_attachments():
    pass

@allure.step('第一步')
def test_02():
    pass

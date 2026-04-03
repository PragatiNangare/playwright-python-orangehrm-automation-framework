from pages.pim_page import PIMPage
from pages.employee_page import AddEmployeePage
from pages.login_page import LoginPage
from utils.data_loader import load_test_data
import random
import pytest

@pytest.mark.parametrize("employee",load_test_data()["employees"])
def test_add_employee(login_page,employee):
    emp_id = str(random.randint(1000, 9999))
    pim = PIMPage(login_page.page)
    pim.navigate_to_add_employee()

    add_emp = AddEmployeePage(login_page.page)
    add_emp.enter_first_name(employee["first_name"])\
    .enter_middle_name(employee["middle_name"])\
    .enter_last_name(employee["last_name"])\
    .enter_employee_id(emp_id)\
    .click_save()
    assert add_emp.is_employee_created()


def test_add_employee_missing_required_fields(login_page):
    emp_id = str(random.randint(1000, 9999))
    pim = PIMPage(login_page.page)
    pim.navigate_to_add_employee()

    add_emp = AddEmployeePage(login_page.page)
    add_emp.enter_middle_name("H")\
    .enter_employee_id(emp_id)\
    .click_save()

    assert add_emp.is_first_name_error_visible()
    assert add_emp.is_last_name_error_visible()

def test_duplicate_employee_id(login_page):
    emp_id = str(random.randint(1000, 9999))
    pim = PIMPage(login_page.page)
    pim.navigate_to_add_employee()

    add_emp = AddEmployeePage(login_page.page)
    add_emp.enter_first_name("John")\
    .enter_middle_name("H")\
    .enter_last_name("Doe")\
    .enter_employee_id(emp_id)\
    .click_save()
    login_page.page.locator("h6:has-text('Personal Details')").wait_for()
    

    pim.navigate_to_add_employee()
    add_emp.enter_first_name("John")\
    .enter_middle_name("H")\
    .enter_last_name("Doe")\
    .enter_employee_id(emp_id)\
    .click_save()
    

    assert add_emp.is_employee_id_duplicate_error_visible()

    

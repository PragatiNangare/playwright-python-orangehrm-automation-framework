from pages.employee_list_page import EmployeeListPage
from pages.pim_page import PIMPage
from pages.employee_page import AddEmployeePage
import random

def test_search_employee(login_page):
    pim = PIMPage(login_page.page)
    add_emp = AddEmployeePage(login_page.page)
    pim.navigate_to_add_employee()
    emp_id = str(random.randint(1000, 9999))
    first_name = "John"
    middle_name = "D"
    last_name = "Doe"
    search_name = f"{first_name} {middle_name}"
    add_emp.enter_first_name(first_name)\
    .enter_middle_name(middle_name)\
    .enter_last_name(last_name)\
    .enter_employee_id(emp_id)\
    .click_save()


    emp_pg =EmployeeListPage(login_page.page)
    pim.go_to_employee_list()
    emp_pg.search_employee_by_name(first_name)

    assert emp_pg.is_employee_present()
    
    
    
   



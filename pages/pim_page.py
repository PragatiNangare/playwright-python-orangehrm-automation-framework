class PIMPage():
    def __init__(self,page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.add_employee_button = page.get_by_role("link",name= 'Add Employee')
        self.employee_list_tab= page.get_by_text("Employee List", exact=True)

    def click_pim_menu(self):
        self.pim_menu.click()
        return self
    
    def click_add_employee(self):
        self.add_employee_button.click()
        return self
    
    def navigate_to_add_employee(self):
        return self.click_pim_menu().click_add_employee()
    
    def go_to_employee_list(self):
        self.employee_list_tab.click()
        return self


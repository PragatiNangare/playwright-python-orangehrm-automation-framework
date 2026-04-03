class AddEmployeePage():
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.get_by_role("textbox", name="First Name")
        self.middle_name_input = page.get_by_role("textbox", name="Middle Name")
        self.last_name_input = page.get_by_role("textbox", name="Last Name")
        self.employee_id_input = page.locator("input.oxd-input").nth(4)
        self.save_button = page.get_by_role("button", name="Save")
        self.success_message = page.get_by_text(" Successfully Saved")
        self.first_name_required_error=page.get_by_text("Required", exact=True).nth(0)
        self.last_name_required_error =page.get_by_text("Required", exact=True).nth(1)
        self.employee_id_duplicate_error= page.get_by_text("Employee Id already exists")



    def enter_first_name(self,first_name):
        self.first_name_input.fill(first_name)
        return self
    
    def enter_middle_name(self,middle_name):
        self.middle_name_input.fill(middle_name)
        return self
    
    def enter_last_name(self,last_name):
        self.last_name_input.fill(last_name)
        return self
    
    def enter_employee_id(self,emp_id):
        self.employee_id_input.fill(emp_id)
        return self
    
    def click_save(self):
        self.save_button.click()
        return self
    
    def is_employee_created(self):
        self.success_message.wait_for(timeout=5000)
        return self.success_message.is_visible()
    
    def is_first_name_error_visible(self):
        self.first_name_required_error.wait_for(state="visible")
        return self.first_name_required_error.is_visible()

    def is_last_name_error_visible(self):
        self.last_name_required_error.wait_for(state="visible")
        return self.last_name_required_error.is_visible()
    
    def is_employee_id_duplicate_error_visible(self):
        self.employee_id_duplicate_error.wait_for(state="visible")
        return self.employee_id_duplicate_error.is_visible()




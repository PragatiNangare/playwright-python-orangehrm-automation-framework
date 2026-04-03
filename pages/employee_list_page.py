class EmployeeListPage():
    def __init__(self,page):
        self.page = page
        self.employee_name_input = page.get_by_role("textbox", name="Type for hints...").nth(0)
        self.employee_id_input = page.get_by_label("Employee Id")
        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")
        self.no_records_found_message = page.get_by_text("No Records Found")
        
    def search_employee_by_name(self,firstname):
        self.employee_name_input.fill(firstname)
        self.search_button.click()
        return self
    
    def is_employee_present(self):
        return self.no_records_found_message.is_hidden()
    
    


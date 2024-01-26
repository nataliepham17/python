class Employee:
    def __init__(self, first_name, last_name, emp_number):
        self.first_name = first_name
        self.last_name = last_name
        self.emp_number = emp_number
    
    # Getter
    @property
    def print_emp_info(self):  # demonstration - add a new function within a class
        print(f"{self.emp_number} {self.first_name} {self.last_name}")
              
    # Setter
    def first_name(self, temp):
        self.first_name = temp
        
    def last_name(self, temp):
        self.last_name = temp
        
    def emp_number(self, temp):
        self.emp_number = temp
        


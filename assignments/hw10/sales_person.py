"""
Name: Vinicius Nunes Lopes
sales_person.py
"""

class SalesPerson:
    """
    This class shows information about an employee
    """
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def enter_sale(self, sales_amount):
        self.sales.append(float(sales_amount))

    def get_sales(self):
        return self.sales

    def total_sales(self):
        total = 0
        for sale in self.sales:
            total = total + sale
        return total

    def met_quota(self, quota):
        return quota <= self.total_sales()

    def compare_to(self, other):
        self_sales = self.total_sales()
        other_sales = other.total_sales()
        if other_sales > self_sales:
            return -1
        if other_sales < self_sales:
            return 1
        return 0

    def __str__(self):
        return str(self.get_id()) + "-" + self.name + ":" + str(self.total_sales())

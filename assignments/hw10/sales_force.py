"""
name: Vinicius Nunes Lopes
sales_force.py
"""

from sales_person import SalesPerson

class SalesForce:
    """
    This class shows information for a group of sales people
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        sales_force_list = open(file_name, "r")
        for line in sales_force_list.readlines():
            attributes = line.split(", ")
            person = SalesPerson(int(attributes[0]), attributes[1])
            list_sales = attributes[2].split()
            for sale in list_sales:
                person.enter_sale(float(sale))
            self.sales_people.append(person)

    def quota_report(self, quota):
        data = []
        for person in self.sales_people:
            data_person = [person.get_id(), person.get_name(), person.total_sales(),
                           person.met_quota(quota)]
            data.append(data_person)
        return data

    def top_seller(self):
        top_seller = []
        for i in range(len(self.sales_people)):
            for j in range(i + 1, len(self.sales_people)):
                if self.sales_people[j].compare_to(self.sales_people[i]) > 0:
                    self.sales_people[i], self.sales_people[j] = self.sales_people[j
                                                                 ], self.sales_people[i]
        top_seller.append(self.sales_people[0])
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales() >= top_seller[0].total_sales():
                top_seller.append(self.sales_people[i])
            else:
                break
        return top_seller

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            if self.sales_people[i].get_id() == employee_id:
                return self.sales_people[i]
        return None

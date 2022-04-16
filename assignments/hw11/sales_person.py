""""
Darla Valderrama
hw.11, sales_person.py
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self):
        return self.name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        total = self.total_sales()
        if total > quota:
            return True
        else:
            return False

    def compare_to(self, other):
        my_total = self.total_sales()
        other_total = other.total_sales()
        if my_total > other_total:
            return 1
        elif other_total > my_total:
            return -1
        else:
            return 0

        def __str__(self):
            return str(self.employee_id) + "_" + self.name + ":" + str(self.total_sales())



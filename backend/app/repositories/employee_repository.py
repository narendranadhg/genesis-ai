from app.data.employees import employees
from app.data.addresses import addresses


class EmployeeRepository:

    def get_all_employees(self):
        return employees

    def get_employee_by_id(self, employee_id: int):
        for employee in employees:
            if employee["id"] == employee_id:
                return employee
        return None

    def search_employees(self, keyword: str):
        keyword = keyword.lower()

        return [
            employee
            for employee in employees
            if keyword in employee["name"].lower()
            or keyword in employee["city"].lower()
        ]

    def get_employee_address(self, employee_id: int):
        return addresses.get(employee_id)
from app.repositories.employee_repository import EmployeeRepository


repository = EmployeeRepository()


def get_all_employees():
    return repository.get_all_employees()


def get_employee(employee_id: int):
    return repository.get_employee_by_id(employee_id)


def search_employees(keyword: str):
    return repository.search_employees(keyword)


def get_employee_address(employee_id: int):
    return repository.get_employee_address(employee_id)
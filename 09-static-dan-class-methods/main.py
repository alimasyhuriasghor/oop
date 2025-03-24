import datetime as dt
import random
import string

class Employee:

    # Private class variable
    __total_employee = 0

    def __init__(self, name: str, salary: int, schedule: str) -> None:
        self.name = name
        self.salary = salary
        self.schedule = schedule
        self.id = "".join(random.choice(string.digits) for _ in range(6))

    @staticmethod
    def work_day(date):
        data = {
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7
        }

        for key in data:
            if date == key:
                date = data[key]
                if dt.date.today().isoweekday() == date:
                    return True
                else:
                    return False


# Create the instance of an employee class
gerry = Employee("Gerry", 500000, "Monday")

print(gerry.work_day(gerry.schedule))
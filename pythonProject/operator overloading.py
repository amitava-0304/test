class A:

    def __init__(self, name, salary, role, lang):

        self.name = name

        self.salary = salary

        self.role = role

        self.lang = lang

    def print_details(self):

        return f"The employee is {self.name}, Salary is {self.salary} and Role is {self.role}"



    def __gt__(self, other):

        return self.salary > other.salary



    def __truediv__(self, other):

        return self.salary / other.salary



    def __mul__(self, other):

        return self.salary * other.salary



    def __repr__(self):

        return f"Details: ({self.name}, {self.salary}, {self.role})"

    def __str__(self):

        return f"She knows {self.lang}"



a = A("Leah", 50000, "UX Designer", ['HTML-CSS-JS', 'Python', 'C-C++'])

r = A("Rhythm", 100000, "Cyber Security Instructor", ['HTML-JS', 'Python', 'Linux commands'])



print(repr(a))

print(a)

print(a.print_details(), end="\n\n")

print(r > a)

print(r / a)

print(a * r)

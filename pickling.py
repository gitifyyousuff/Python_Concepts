import pickle
class Employee:

    def __init__(self,name,role,age):
        self.name = name
        self.role = role
        self.age = age

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age}, role={self.role})"

emp1 = Employee("Yousuff","Tech Lead",30)
emp2 = Employee("ABD","Manager",39)

print(repr(emp1))

# Serializing the objects or instances in the file
with open('employee.pkl','wb') as file:
    pickle.dump(emp1,file)
    pickle.dump(emp2,file)


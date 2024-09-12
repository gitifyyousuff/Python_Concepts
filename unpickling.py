import pickle
class Employee:

    def __init__(self,name,role,age):
        self.name = name
        self.role = role
        self.age = age

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age}, role={self.role})"

# Deserialize the list of objects from the file
with open('employee.pkl','rb') as file:
    emp1 = pickle.load(file)
    emp2 = pickle.load(file)

print(emp1)
print(emp2)
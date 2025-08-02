#initiate a class
class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing attributes/data.")
        self.id=123
        self.designation="sde"
        self.salary=500000
        print("Attributes or data have been initiated.")
    
    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")

#create an object or instance of the class
sam=employee()

#Example use cases of the above :  
# print(sam.salary)

# sam.travel("Kerala")

print(type(sam))
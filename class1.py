class Employer():
    def __init__(self, name, sales, bonushrs, basesalary):
        # Initialize the Employer object with the provided parameters
        self.name = name
        self.sales = sales
        self.bonushrs = bonushrs
        self.basesalary = basesalary
    
    def info(self):
        # Display information about the employee
        print(" Name is {}. Base salary is {}. Sales are {}.Bonus hrs is {}".format(self.name, self.basesalary, self.sales, self.bonushrs))
    
    # The following method is commented out because it's not implemented in the code
    # def calculateNetSalary():

# Create instances of the Employer class
emp1 = Employer( "Youssef",567 , 31,30000)
emp2 = Employer( "adam",348 , 65,6000)

# Display information about each employee
emp1.info()
emp2.info()
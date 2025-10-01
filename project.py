class School_Bus():
    def __init__(self, name, fare, capacity):
         self.name = name
         self.fare = fare
         self.capacity = capacity
         self.total_fare = self.fare * self.capacity 
         self.tax_fare = self.total_fare * 0.1
         self.final_fare = self.total_fare + self.tax_fare
        
         Bus = School_Bus("SML ISUZU S7", 100, 50)
         print("Vehicle Name:", Bus.name, "Fare:", Bus.fare, "Capacity:", Bus.capacity, "Total Fare:", Bus.total_fare, "Tax Fare:", Bus.tax_fare, "Final Fare:", Bus.final_fare)
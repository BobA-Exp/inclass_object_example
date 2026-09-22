class TemperatureReading:
    default_unit = "Celsius"  #! Class-wide (static) attribute
    
    #Instance method
    def __init__(self, celsius):
        # self.celsius = celsius     --- Public attribute
        # self._celsius = celsius   --- Protected attribute
        self.__celsius = celsius  #--- Private atttribute, so it will be subject to name mangling >  _TemparatureReading__celsius

    # Property methods
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, celsius):
        if celsius < -273.15:
            raise ValueError("Temperature cannot drop below absolute zero (-273.15 °C)")
        self.__celsius = celsius

    @classmethod
    def construct_from_farenheit(cls, farenheit):
        celsius = (farenheit - 32) * (5/9)
        return cls(celsius) 

    @staticmethod
    def validate_celsius(celsius):
        return celsius >= -273.15
        

temp1 = TemperatureReading(25)  # Object instantiation

temp2 = TemperatureReading.construct_from_farenheit(70)  # Object instantiation through a class method

print(TemperatureReading.validate_celsius(25))  # Static method call
print(TemperatureReading.validate_celsius(-273.15))  # Static method call
print(TemperatureReading.validate_celsius(-273.16))  # Static method call   



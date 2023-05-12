##static//
import datetime
class Employee:
    num_emp = 0
    raise_amt=1.04
    def __init__(self,first,last,pay) -> None:
        self.first =first 
        self.last =last
        self.pay=pay

    @staticmethod ##logical connection with class 
    def is_working(day):
        if day.weekday==5 or day.weekday()==6:
            return False
        else :
            return True

my_date =datetime.date(2023,1,1)
print(Employee.is_working(my_date))
'''
## HEre in above code static method is_working have 
logical connection with class Employee but it doesnot 
depend upon instance and class variable instead it work
independetly 
''' 

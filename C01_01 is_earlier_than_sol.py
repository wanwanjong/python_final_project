class Time():
    
    def __init__(self, h, m, s):
    
        self.hour = h
        self.minute = m
        self.second = s


    def print_normally(self):
    
        print('%d:%d:%d' %(self.hour, self.minute, self.second), end = "")
        
        
    def is_earlier_than(self, another_time):
    
        total_second_self = self.cal_time()
        total_second_another = another_time.cal_time()
        
        if(total_second_self < total_second_another):
            return True
        else:
            return False


    def cal_time(self): 
    
        return self.hour * 3600 + self.minute * 60 + self.second




"""
t1 = Time(12, 30, 40)
t2 = Time(13, 10, 5)
if t1.is_earlier_than(t2):
    print("t1 is earlier than t2")
else:
    print("t1 is not earlier than t2")
"""


time_values = input().split()
time_values = [int(tv) for tv in time_values]

t1 = Time(time_values[0], time_values[1], time_values[2])
t2 = Time(time_values[3], time_values[4], time_values[5])
t3 = Time(time_values[6], time_values[7], time_values[8])

if t1.is_earlier_than(t2):
    if t1.is_earlier_than(t3):
        t1.print_normally()    
    else:
        t3.print_normally()
else:
    if t3.is_earlier_than(t2):
        t3.print_normally()
    else:
        t2.print_normally()
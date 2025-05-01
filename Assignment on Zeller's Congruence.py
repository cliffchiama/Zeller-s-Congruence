class DateCalculator:
    def __init__(self,year , month , day ):
        self.year = year
        self.month = month
        self.day = day

    def calculate_weekday(self):
        #Adjusting for Jan and Feb
        if self.month == 1 or self.month ==2:
            self.month +=12
            self.year -=1

        q = self.day
        m = self.month
        y = self.year
        k = self.year % 100
        j = self.year // 100

        h = ((q + (13*(m + 1)) // 5) + k + (k // 4) + (j // 4) + (5*j)) % 7

        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return days[int(h)]

date = DateCalculator(2025 , 5 , 2)
print(date.calculate_weekday())








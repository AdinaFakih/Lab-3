class Test(Date):
  def __init__(self,day,month,year):
    Date.__init__(self,day,month,year)

if __name__ == "__main__":
months = ['jan','feb','march','april','may','june','july','august','september','oct','november','dec']
date = Test(1,'june',1998)
date.isLeapYear(2019)
print("Total Days :",date.NumberOfDaysInMonth('april'))
date.addDays(7,months)
date.subtractDays(14,months)
class Date:
  def __init__(self,day,month,year):
    self.day = day
    self.month = month
    self.year = year

  def get_day(self): 
    return self.day 

  def set_day(self, x): 
    self.day = x 

  def get_month(self): 
    return self.month 

  def set_month(self, x): 
    self.month = x  

  def get_year(self): 
    return self.year 

  def set_year(self, x): 
    self.year = x  

  def NumberOfDaysInMonth(self,month):
    if month == 'February':
      return 28
    if month in ['January','March','May','July','August','October','December']:
      return 31
    if month in ['April','June','September','November']:
      return 30
  
  def isLeapYear(self):
    year=int(input('Enter year to be checked: ')) 
    if(year%4 == 0 and year%100 != 0 or year%400 == 0):
      print('The year is a leap year!')
    else: 
      print("The year isn't a leap year!")

  def addDays(self,adddays,months):
    adddays=self.get_day()+adddays
    self.currdays = self.NumberOfDaysInMonth(self.get_month())
    if self.currdays>=adddays:
      self.set_day(adddays)
    else:
      adddays=adddays-self.currdays 
      self.set_month(months[months.index(self.get_month())+1])
      self.set_day(adddays)

  def subtractDays(self,subdays,months):
    subdays=self.get_day()-subdays
    if subdays <= 0:
      self.set_month(months[months.index(self.get_month())-1])
      self.currdays=self.NumberOfDaysInMonth(self.get_month())
      subdays=self.currdays+subdays
      self.set_day(subdays)
    else:
      self.set_day(subdays)
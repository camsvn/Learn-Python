import datetime

class bday:    
    def __init__(self,year,month,day,hour=0,minute=0,second=0):
        self.year=year
        self.month=month
        self.day=day
        self.hour=hour
        self.minute=minute
        self.second=second        
    
    def age(self):
        born=datetime.datetime(self.year,self.month,self.day,self.hour,self.minute,self.second)
        today=datetime.datetime.today()        
        delta=today-born               
        
        age=int(delta.days/365)        
        
        return age
    
    def nextbday(self):
        born=datetime.datetime(self.year,self.month,self.day,self.hour,self.minute,self.second)
        today=datetime.datetime.today()
        
        nextbday=born.replace(year=self.year+self.age()+1)
        
        delta=nextbday-today
        
        deltahours,deltaminute=divmod(delta.seconds,3600)
        deltaminute,deltasecond=divmod(deltaminute,60)
        
        return '%d days, %.2d Hours , %.2d Minutes, %.2d Seconds' %(delta.days,deltahours,deltaminute,deltasecond)
        
        
name=input('Enter Name of the person: ')
print('\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Rules:\n\t-> Date Format YYYY/MM/DD\n\n\t-> Time Format HH:MM:SS')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

year,month,day=input('Enter Date Of Birth: ').split('/')
#Since the input is of type list Explicit Integer Conversion Required
year=int(year) 
month=int(month)
day=int(day)

hour,minute,second=input('Enter Time Of Birth: ').split(':')
#Since the input is of type list Explicit Integer Conversion Required
hour=int(hour)
minute=int(minute)
second=int(second)

person=bday(year,month,day,hour,minute,second)
print('\n========================================================================================')
print('-> Age of {} is {} '.format(name,person.age()))
print("-> %s's Birthday is in %s" %(name,person.nextbday()))
print('========================================================================================')

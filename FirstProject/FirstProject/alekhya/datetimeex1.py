'''
import time;
sysdatetime=time.time();
print(sysdatetime);



import time;
currenttime=time.time();
print(currenttime);


#time.altzone
import time;
print(time.altzone);

'''
'''
#time.asctime()
datetime=time.localtime();
print((time.asctime(datetime));



#time.sleep(sec)
import time;
print(time.ctime());
time.sleep(6);
print(time.ctime());


#time.ctime()
import time;
datetime=time.ctime
print(datetime);


#digital-clock
import time;
while True:
        ct=time.localtime(time.time())
        print(ct[3],":",ct[4],":",ct[5],end="\t\r");
        time.sleep(1)
        '''
        
#calender module
import calendar;
#print(calendar.calendar(2022,4,3,6));
#print(calendar.firstweekday());
print(calendar.isleap(2020));
#print(calendar.isleap(2022));
#print(calendar.leapdays(2022,2035));
#print(calendar.month(2022,10,2,1));
#print(calendar.monthcalendar(2022,10));
#print(calendar.monthrange(2022,10));
#print(calendar.prcal(2022,2,1,6));
#print(calendar.prmonth(2022,10,3,2));
#calendar.setfirstweekday(5);
#calendar.prmonth(2022,10,2,1);
#print(calendar.weekday(2022,11,1));


'''
#datetime module
import datetime;
date1=datetime.datetime.now();
print(date1);
'''
'''

import calendar;

print(calendar.firstweekday());
print(calendar.isleap(2020));
print(calendar.leapdays(2020,2030));
print(calendar.month(2020,11,2,1));
print(calendar.monthcalendar(2020,11));
print(calendar.monthrange(2020,2));

'''

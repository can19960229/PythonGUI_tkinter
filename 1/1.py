#DayDayUoQ1.py

dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("{:.2f},{:.2f}".format(dayup,daydown))

#DayDayUoQ3.py
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    m = ((i % 7) == 6 or (i % 7) == 0)
    if m:
    #if i % 7 in [6,0]:
        print(m,i,end="")
        dayup = dayup * (1 - dayfactor)
    else: 
        dayup = dayup * (1 + dayfactor)
print("{:.2f}".format(dayup))

#DayDayUoQ4.py
def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else: 
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while dayUp(dayfactor)< 37.78:
    dayfactor +=0.001
print("工作日努力的参数是：{:.3f}".format(dayfactor))


#Q5.py
weekstr = "星期一星期二星期三星期四星期五星期六星期日"
str = eval(input())
pos = (str - 1) * 3
print(weekstr[pos:pos+3])


n = eval(input())

for i in range(1,n+1,2):
    
	print("{0:^{1}}".format('*'*i,n))

#Q6.py
weekstr = "一二三四五六日"
str = eval(input())
print("星期"+weekstr[str-1])

for i in range(12):
    print(chr(9800 + i),end="")





            
    

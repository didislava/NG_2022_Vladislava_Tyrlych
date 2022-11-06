# user enters the number of seconds
enter_numb_sec = int(input("enter the number of seconds "))

numb_days = enter_numb_sec//86400
numb_hours = ((enter_numb_sec-(numb_days*86400))//3600)
numb_min = ((enter_numb_sec-(numb_hours*3600)-(numb_days*86400))//60)
numb_sec = enter_numb_sec-((numb_min*60)+(numb_hours*3600)+(numb_days*86400))

#print (str(numb_days))
print (str(numb_days) + ":" + str(numb_hours) + ":" + str(numb_min) + ":" + str(numb_sec))

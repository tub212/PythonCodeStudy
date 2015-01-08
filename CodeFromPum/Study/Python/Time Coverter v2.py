'''Time Coverter v2'''
#Comment
def time_converter(hour, minute):
    hour_mod = hour%12
    mintime = minute
    if hour < 24 and hour >= 22:
        if mintime < 10:
            print str(hour_mod)+ ":" +"0"+ str(mintime) + " PM"
        elif mintime >= 10:    
            print str(hour_mod)+ ":" + str(mintime) + " PM"
    elif hour > 12 and hour < 22:
        if mintime < 10:
            print "0" + str(hour_mod) + ":" +"0"+ str(mintime) + " PM"
        elif mintime >= 10:    
            print "0" + str(hour_mod) + ":" + str(mintime) + " PM"        
    elif hour == 12:
        if mintime < 10:
            print "12" + ":" +"0"+ str(mintime) + " PM"
        elif mintime >= 10:    
            print "12" + ":" + str(mintime) + " PM"
    elif hour >= 10 and hour < 12:
        if mintime < 10:
            print str(hour_mod)+ ":" +"0"+ str(mintime) + " AM"
        elif mintime >= 10:    
            print str(hour_mod)+ ":" + str(mintime) + " AM"
    elif hour >= 0 and hour <= 9:
        if mintime < 10:
            print "0" + str(hour_mod)+ ":" +"0"+ str(mintime) + " AM"
        elif mintime >= 10:    
            print "0" + str(hour_mod)+ ":" + str(mintime) + " AM"   
    elif hour == 0:
        if mintime < 10:
            print "00:" +"0" + str(mintime) + " AM" 
        elif mintime >= 10:
            print "00:" + str(mintime) + " AM"  
time_converter(input(), input())        
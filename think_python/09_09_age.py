def age():

    # loop through mom's age when son was born
    for m in range(10,50):
        
        i=0       #son's age
        count = 0 #count of age reverses
        ages = [] #list of ages reverse

        # loop through years (mom maximum age = 99)
        while i <= 99-m:
            if str(m+i).zfill(2)[::-1] == str(i).zfill(2):
                count+=1
                ages+=[(i,m+i)]

            i+=1
        
        if count == 8:
            print ages
            print 'Son age is: '+ str(ages[5][0])


age()    

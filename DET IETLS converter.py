# DET --> IELTS conversion
print("This is a Duolingo English Test(DET) to IELTS Academic converter\n")
while True:
    scr = input("Please enter your DET score > ") 
    try:   
        if int(scr) < 95:
            print("Not acceptable")
            break       
        if int(scr) > 160:
            print("Out of the range")
            break        
        if int(scr) in range(155,161):
           ieltsband = 9
        if int(scr) in range(145,151):
            ieltsband = 8.5
        if int(scr) in range(135,141):
            ieltsband = 8
        if int(scr) in range(125,131):
            ieltsband = 7.5
        if int(scr) in range(115,121):
            ieltsband = 7
        if int(scr) in range(105,111):
            ieltsband = 6.5
        if int(scr) in range(95,101):
            ieltsband = 6
        print("DET score",int(scr),
              "= IELTS Academic",ieltsband)      
        if ieltsband > 6.5 :
            print("--> Apply to our MSc/MA programs!")    
        if ieltsband <= 6.5 :
            print("--> Apply to our BSc/BA programs!") 
    except:
            print("Invalid input.")
            

    

#print "Anirud " 4 times   // rsion head recu
count = 0

def funct():
    global count

    if count ==4:
        return
    
    print("Anirudh")
    count +=1
    funct()
funct()   
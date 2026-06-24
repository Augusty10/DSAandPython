# tail recursion (Print  Name n times )

count = 0 
def func():
    global count

    if count ==4:
        return
    count +=1 
    func()
    print("Anirudh ")
func()

x = " "
run = False
while x != "stop" :
    x = input(">>>")
    if x == "start" :
        if  not run :
            print("car is started")
            run = True
        else :
            print("car is already started")
    
    elif x == "slow" :
        if  run:
            print("car is stopped")
            run  = False
        else:
            print("car is already stoppes")
    else:
        print('i didnt understand')
    
    

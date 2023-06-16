from pprint import pprint as pp
import random
ticket_details={}
while True:
    while True:
        try:
            name=input("Enter your name: ")
            if any(i.isdigit() for i in name):
                raise Exception("Name should not contain any numbers")
            else:
                break
        except Exception as e:
            print(e)
    while True:
        try:           
            age=int(input("Enter your age: "))
            if age>0:
                break
        except Exception as e:
            print(e)

    flights={"Hyd_Mum":["SPICEJET","INDIGO","QATAR","ETIHAD"],
             "Mum_Del":["DELTA","INDIGO","EMIRATES","AIRINDIA"],
             "Del_Hyd":["SINGAPORE","ETIHAD","WESTERN","SWISS"],
             "Hyd_Kol":["QATAR","BRITISH","SPICEJET","LUFTHANSA"]}
    
    print("choose a route: ")
    for i in range(0,4):
        print(str(i)+":"+list(flights)[i])

    while True:
        try:
            route_num=int(input("\n"))
            if route_num > 3 or route_num < 0:
                raise Exception("Enter the number between 0 to 3")
            if route_num > -1 or route_num < 4:
                break
        except Exception as e:
            print(e)
    
    
    print("Choose Airlines: ")
    airline_list=flights[list(flights)[route_num]]
    pp(airline_list)
    for i in range(0,4):
        print(str(i)+":"+airline_list[i])
    
    while True:
        try:
            flight_num=int(input("\n"))
            if flight_num > 3 or flight_num < 0:
                raise Exception("Enter the number between 0 to 3")
            if flight_num > -1 or flight_num < 4:
                break
        except Exception as e:
            print(e)
    
    flight_name=airline_list[flight_num]
    ticket=flight_name[0:2]+str(random.randint(1,1000))
    ticket_details[name]=ticket
    pp(ticket_details)
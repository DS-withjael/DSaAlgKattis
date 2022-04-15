
### Functions
Flights_Dict = {}

def delay_flight(time, delay):
    destination = Flights_Dict[time]
    hr, mn, sc = int(time[0:2]), int(time[3:5]), int(time[6:8])

    add_sc = int(delay)
    add_sc = add_sc % (24*3600)
    add_hr = add_sc // 3600
    add_sc %= 3600
    add_mn = add_sc // 60
    add_sc %= 60

    hr += add_hr
    mn += add_mn
    sc += add_sc

    if sc >= 60:
        sc -= 60
        mn += 1
    if mn >= 60:
        mn -= 60
        hr += 1
    if hr >= 24:
        hr -= 24

    if len(str(hr)) < 2:
        hr = str(hr)
        hr = '0' + hr
    if len(str(mn)) < 2:
        mn = str(mn)
        mn = '0' + mn
    if len(str(sc)) < 2:
        sc = str(sc)
        sc = '0' + sc
    new_time = f"{hr}:{mn}:{sc}"
    Flights_Dict.pop(time)
    Flights_Dict.setdefault(new_time, destination)
    return   

def next_departure(time):
    second_list = [i for i in Flights_Dict.keys()]
    
    second_list.append(time)
    second_list = sorted(second_list)

    start_index = second_list.index(time)
    second_list = second_list[start_index:]
    
    return print(second_list[1], Flights_Dict[second_list[1]])
    
def count_flights(t1, t2):
    second_list = [i for i in Flights_Dict.keys()]
    second_list.append(t1)
    second_list.append(t2)
    second_list = sorted(second_list)

    t1_index = second_list.index(t1)
    # the last occurence of t2 in the list:
    t2_index = len(second_list) - 1 - second_list[::-1].index(t2)

    second_list = second_list[t1_index+1:t2_index]
    return print(len(second_list))

def main():
    flights , ops = map(int, input().split())

    for _ in range(flights):
        flight = input().split()
        time, destination = flight
        Flights_Dict.setdefault(time, destination)
    # print(Flights_Dict)

    for _ in range(ops):
        operation = input().split()
        # print(operation)

        if operation[0] == "destination":
            try:
                print(Flights_Dict[operation[1]])
            except KeyError:
                print("-")

        elif operation[0] == "cancel":
            Flights_Dict.pop(operation[1])

        elif operation[0] == "delay":
            delay_flight(operation[1], operation[2])

        elif operation[0] == "reroute":
            Flights_Dict[operation[1]] = operation[2]

        elif operation[0] == "next":
            next_departure(operation[1])

        elif operation[0] == "count":
            count_flights(operation[1], operation[2])

if __name__ == "__main__":
    main()
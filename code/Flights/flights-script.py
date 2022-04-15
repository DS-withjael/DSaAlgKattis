
### Functions
Flights_Dict = {}

def new_flight(time, destination):
    Flights_Dict.setdefault(time, destination)

def cancel_flight(time):
    Flights_Dict.pop(time)

def convert_time(time_string):
    hr = time_string[0:2]
    mn = time_string[3:5]
    sc = time_string[6:8]
    return int(hr), int(mn), int(sc)

def convert_delay(seconds):
    seconds = int(seconds)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hour, minutes, seconds

def delay_flight(time, delay):
    destination = Flights_Dict[time]
    hr, mn, sc = convert_time(time)
    add_hr, add_mn, add_sc = convert_delay(delay)

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

def reroute_flight(time, new_destination):
    Flights_Dict[time] =  new_destination

def show_destination(time):
    try:
        print(Flights_Dict[time])
    except KeyError:
        print("-")
    
def convert_to_sec(time):
    seperated_time = convert_time(time)
    hr, mn, sc = seperated_time
    total_seconds = sc + mn*60 + hr*3600
    return total_seconds    

def next_departure(time):
    second_list = list()
    for i in Flights_Dict.keys():
        seconds = convert_to_sec(i)
        second_list.append(seconds)

    second_list.append(convert_to_sec(time))
    second_list = sorted(second_list)

    start_index = second_list.index(convert_to_sec(time))
    second_list = second_list[start_index:]

    hr, mn, sc = convert_delay(second_list[1])
    if len(str(hr)) < 2:
        hr = str(hr)
        hr = '0' + hr
    if len(str(mn)) < 2:
        mn = str(mn)
        mn = '0' + mn
    if len(str(sc)) < 2:
        sc = str(sc)
        sc = '0' + sc
    next_depart = f"{hr}:{mn}:{sc}"
    return print(next_depart, Flights_Dict[next_depart])
    
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
        new_flight(time, destination)

    for _ in range(ops):
        operation = input().split()

        if operation[0] == "destination":
            show_destination(operation[1])

        elif operation[0] == "cancel":
            cancel_flight(operation[1])

        elif operation[0] == "delay":
            delay_flight(operation[1], operation[2])

        elif operation[0] == "reroute":
            reroute_flight(operation[1], operation[2])

        elif operation[0] == "next":
            next_departure(operation[1])

        elif operation[0] == "count":
            count_flights(operation[1], operation[2])

if __name__ == "__main__":
    main()
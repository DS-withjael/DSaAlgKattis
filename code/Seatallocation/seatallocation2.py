
def main():
    global seats, allocated_seats, max_dict
    parties, seats = input().split()
    parties, seats = int(parties), int(seats)
    quotient_dict = {}
    allocated_seats = {}
    max_dict = {}
    for i in range(0, parties):
        votes = int(input())
        quotient_dict.setdefault(i, votes)
        allocated_seats.setdefault(i, 0)
        max_dict.setdefault(i, votes)
    allocate_seats(quotient_dict, seat_no=0)
    for i in allocated_seats:
        print(allocated_seats[i])

def allocate_seats(quotient_dict, seat_no):
    if seat_no >= seats:
        return quotient_dict
    else:
        party, max = find_max(quotient_dict)
        allocated_seats[party] += 1
        if allocated_seats[party] == 0:
            quotient = max/(2)
            # print("Max_party= ", party, "Max_value=", max, "Quotient_Calc=", max_dict[party], "/", 2, "=", quotient)
        else:
            quotient = max_dict[party]/(allocated_seats[party]+1)
            # print("Max_party= ", party, "Max_value=", max, "Quotient_Calc=", max_dict[party], "/", allocated_seats[party]+2, "=", quotient)
        quotient_dict[party] = quotient
        seat_no +=1
        # print(quotient_dict)
        # print(" ")
        return allocate_seats(quotient_dict, seat_no)
    
def find_max(d):
    max = 0
    for i, j in d.items():
        if j > max:
            max = j
            index = i
    return index, max

if __name__ == "__main__":
    main()
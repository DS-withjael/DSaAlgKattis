from itu.algs4.sorting.max_pq import MaxPQ

def main():
    parties, seats = input().split()
    seat_list = []
    quotient_dict = {}
    parliament = MaxPQ()
    for _ in range(int(parties)):
        votes = int(input())
        parliament.insert(votes)
    # print(parliament.max())
    calculate_quotient(0, int(parties), int(parliament.max()), seat_list, parliament, quotient_dict)
    

def calculate_quotient(party, parties, max, seat_list, parliament, quotient_dict):
    if party >= parties:
        return print(seat_list, quotient_dict)
    elif party == 0:
        seat_list.append(1)
        quotient_dict.setdefault(0, 1)
        parliament.del_max()
        return calculate_quotient(1, parties, parliament.max(), seat_list, parliament, quotient_dict)
    elif party >= 0:
        quotient = max/parties
        if quotient > quotient_dict[party-1]:
            try:
                seat_list[party] += 1
            except IndexError:
                seat_list.append(1)
            quotient_dict[party] = quotient
            party+=1
            return calculate_quotient(party, parties, parliament.max(), seat_list, parliament, quotient_dict)
        else:
            seat_list[party-1] += 1
            quotient_dict[party] = quotient
            party+=1
            return calculate_quotient(party, parties, parliament.max(), seat_list, parliament, quotient_dict)


if __name__ == "__main__":
    main()
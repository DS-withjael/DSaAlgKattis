from itu.algs4.sorting.max_pq import MaxPQ

def seat_allocation():
    maxpq = MaxPQ()
    n,m = map(int, input().split()) #n = parties, m = total seats

    seats = [0] * int(n)
    votes, votes_chang = [], []
    print(seats)

    for _ in range(0, n):
        noOfVotes = int(input())
        votes.append(noOfVotes)
        votes_chang.append(noOfVotes)
        maxpq.insert(noOfVotes)

    for _ in range(0, m):
        temp_var = maxpq.max()
        seats[votes_chang.index(temp_var)] += 1
        new_in = votes[votes_chang.index(temp_var)] / (seats[votes_chang.index(temp_var)] + 1)
        maxpq.del_max()
        votes_chang[votes_chang.index(temp_var)] = new_in
        maxpq.insert(new_in)
        
    for i in seats:
        print(i)

seat_allocation()

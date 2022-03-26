from itu.algs4.sorting.max_pq import MaxPQ

def main():
    priorQue = MaxPQ()
    parties, total_seats = map(int, input().split())
    seats = []
    votes, votes_quotient = [], []
    
    i = 0
    while i < parties:
        seats.append(0)
        election_votes = int(input())
        votes.append(election_votes)
        votes_quotient.append(election_votes)
        priorQue.insert(election_votes)
        i+=1

    # print(seats, votes, votes_quotient)
    j = 0
    while j < total_seats:
        max = priorQue.max()
        seats[votes_quotient.index(max)] += 1
        quotient = votes[votes_quotient.index(max)] / (seats[votes_quotient.index(max)]+1)
        priorQue.del_max()
        votes_quotient[votes_quotient.index(max)] = quotient
        priorQue.insert(quotient)
        j+=1

    for i in seats:
        print(i)

if __name__ == "__main__":
    main()
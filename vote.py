def vote(votes):
    vote_count = {}
    for num in votes:
        if num in vote_count:
            vote_count[num] += 1
        else:
            vote_count[num] = 1
    winner = None
    max_votes = 0
    for num, count in vote_count.items():
        if count > max_votes:
            max_votes = count
            winner = num
    return winner


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
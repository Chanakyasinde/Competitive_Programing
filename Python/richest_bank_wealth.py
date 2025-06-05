def max_wealth(accounts):
    transpose = zip(*accounts)

    return max(sum(bank) for bank in transpose)

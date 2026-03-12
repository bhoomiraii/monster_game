import random

events = [0, 1, 2]
weights = [20, 50, 30]

def selector(events=events, weights=weights):
    return random.choices(events, weights=weights, k=1)[0]
    
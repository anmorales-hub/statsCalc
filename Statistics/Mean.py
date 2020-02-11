from MathOperations.addition import Addition
from MathOperations.division import Division

def mean(data):
    num_values = len(data)
    total = 0

    for num in data:
        total = Addition.sum(total, num)
    return Division.quotient(total, num_values)
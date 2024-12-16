import random

def generate_access_sequence(num_pages, sequence_length):
    return [random.randint(0, num_pages - 1) for _ in range(sequence_length)]
#!/usr/bin/env python3

def return_evens(sequence):
    even_numbers = [num for num in sequence if num % 2 == 0]
    return even_numbers

# Example usage:
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = return_evens(sequence)
print(result)

#exclamation
def make_exclamation(sentences):
    sentences_with_exclamation = [sentence + '!' for sentence in sentences]
    return sentences_with_exclamation

# Example usage:
sentence_list = ["Hello", "How are you", "Have a great day"]
result = make_exclamation(sentence_list)
print(result)

#!/usr/bin/python3

def remove_char_at(str, n):
    modified_sentence = ""
    for i in range(len(str)):
        if i != n:
            modified_sentence += str[i]
    return (modified_sentence)

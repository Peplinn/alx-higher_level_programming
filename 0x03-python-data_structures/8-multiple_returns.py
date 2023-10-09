#!/usr/bin/python3

def multiple_returns(sentence):
    size = len(sentence)
    first_letter = sentence[0] if size > 0 else None
    return ((size, first_letter))

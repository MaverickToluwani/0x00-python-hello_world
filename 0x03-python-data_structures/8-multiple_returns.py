#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "" or sentence is None:
        return 0, None

    sent_len = len(sentence)
    firstChar = sentence[0]
    return sent_len, firstChar

#!/usr/bin/python3
def multiple_returns(sentence):
    sent_len = len(sentence)
    firstChar = sentence[0]

    if sentence == "" or sentence is None:
        return None, None
    else:
        return sent_len, firstChar

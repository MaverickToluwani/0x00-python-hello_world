#!/usr/bin/python3
def multiple_returns(sentence):
    sent_len = len(sentence)
    firstChar = sentence[0]

    if sentence == "":
        return (None, sent_len)
    else:
        return (sent_len, firstChar)

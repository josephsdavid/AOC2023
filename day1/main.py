from collections import deque
import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

pwd = os.path.dirname(os.path.abspath(__file__))

STRING_PAIRS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def load_data(fp):
    with open(f"{pwd}/{fp}", 'r') as f:
        data = f.read().splitlines()
        arr = [x if x != "" else "" for x in data]
        return arr


@log_time
def p1(fp):
    data = load_data(fp)
    seq = []
    for item in data:
        digits = []
        for ch in item:
            if ch.isdigit():
                digits.append((ch))
                break
        for ch in item[::-1]:
            if ch.isdigit():
                digits.append((ch))
                break
        seq.append(int("".join(digits)))
    return sum(seq)


# print(p1("t1.txt"))
# print(p1("input.txt"))


@log_time
def p2(fp):
    data = load_data(fp)
    seq = []
    for item in data:
        digits = []
        current_subsequence = deque()
        for ch in item:
            if ch.isdigit():
                digits.append((ch))
                break
            current_subsequence.append(ch)
            current_str = "".join(current_subsequence)
            matches = [x for x in STRING_PAIRS.keys() if x in current_str]
            if len(matches) > 0:
                digits.append(STRING_PAIRS[matches[0]])
                break

        current_subsequence = deque()
        for ch in item[::-1]:
            if ch.isdigit():
                digits.append((ch))
                break
            current_subsequence.appendleft(ch)
            current_str = "".join(current_subsequence)
            matches = [x for x in STRING_PAIRS.keys() if x in current_str]
            if len(matches) > 0:
                digits.append(STRING_PAIRS[matches[0]])
                break
        seq.append(int("".join(digits)))
    return sum(seq)


print(p2("t2.txt"))
print(p2("input.txt"))

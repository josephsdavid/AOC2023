import os
import sys

root_folder = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from utils.time_run import log_time

pwd = os.path.dirname(os.path.abspath(__file__))


def load_data(fp):
    with open(f"{pwd}/{fp}", 'r') as f:
        data = f.read().splitlines()
        arr = [x if x != "" else "" for x in data]
        return arr


@log_time
def run_part_A():
    data = load_data()


@log_time
def run_part_B():
    data = load_data()


print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

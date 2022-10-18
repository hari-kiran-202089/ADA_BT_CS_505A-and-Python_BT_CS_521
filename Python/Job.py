from dataclasses import dataclass


@dataclass
class Job:
    job_name: str
    profit: int
    deadline: int


if __name__ == '__main__':
    job_names = input("Enter Job names: ").split(" ")
    profits = list(map(int, input("Enter Profits: ").split(" ")))
    deadlines = list(map(int, input("Enter Deadlines: ").split(" ")))

    jobs = [Job(name, profit, deadline)
            for (name, profit, deadline) in zip(job_names, profits, deadlines)]

    for job in jobs:
        print(job)

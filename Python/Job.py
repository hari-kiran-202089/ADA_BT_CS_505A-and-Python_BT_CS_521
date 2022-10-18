from dataclasses import dataclass


# Job class with 3 required properties
@dataclass
class Job:
    job_name: str
    profit: int
    deadline: int


if __name__ == '__main__':
    # taking input from users
    job_names = input("Enter Job names: ").split(" ")
    profits = list(map(int, input("Enter Profits: ").split(" ")))
    deadlines = list(map(int, input("Enter Deadlines: ").split(" ")))

    # Storing all jobs in an list
    jobs = [Job(name, profit, deadline)
            for (name, profit, deadline) in zip(job_names, profits, deadlines)]

    print("\nAll Jobs are:")
    for job in jobs:
        print(job)

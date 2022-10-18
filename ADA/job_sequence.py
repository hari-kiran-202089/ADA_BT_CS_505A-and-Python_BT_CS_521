from dataclasses import dataclass


@dataclass
class Job:
    job_name: str
    profit: int
    deadline: int


def job_sequence(jobs):
    # Sorting jobs based on profits
    jobs = sorted(jobs, key=lambda x: x.profit, reverse=True)  # O(nlogn)

    # Finding Max deadline
    max_deadline = max(deadlines)  # O(n)

    # Creating array for sequence
    job_sequence = [None] * max_deadline

    count = 0  # For tracking num of jobs added
    max_profit = 0  # For tracking profit

    for job in jobs:
        if count >= max_deadline:
            break
        # Finding possible position before its deadline
        for i in range(job.deadline-1, -1, -1):
            if job_sequence[i] is None:
                job_sequence[i] = (job.job_name, job.profit)
                max_profit += job.profit
                count += 1
                break

    return job_sequence


if __name__ == '__main__':

    # taking inputs
    job_names = input("Enter Job names: ").split(" ")
    profits = list(map(int, input("Enter Profits: ").split(" ")))
    deadlines = list(map(int, input("Enter Deadlines: ").split(" ")))

    # Making Job objects from the inputs
    jobs = [Job(name, profit, deadline) for (name, profit, deadline)
            in zip(job_names, profits, deadlines)]  # O(n)

    print("The sequence with Maximum profit is", job_sequence(jobs))

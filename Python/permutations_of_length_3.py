from ast import main


def permutaions_of_3(word: str):
    result = set()
    for i in range(len(word)):
        for j in range(len(word)):
            if j == i:
                continue
            for k in range(len(word)):
                if j == k or i == k:
                    continue
                result.add(word[i]+word[j]+word[k])
    return list(result)


if __name__ == '__main__':
    word = input("Enter a 3 letter word: ")
    print(f"All permutations of the {word} are: ")
    print(permutaions_of_3(word))

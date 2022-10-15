def main():
    banks = []
    num_of_banks = int(input())
    names = input().split()
    sums = input().split()
    for i in range(num_of_banks):
        banks.append((names[i], i, int(sums[i])))

    route, inds, summary = [], [], 0
    for i in range(len(banks) - 1):
        if i - 1 in inds or i in inds:
            continue
        elif banks[i][2] >= banks[i + 1][2]:
            route.append(banks[i][0])
            inds.append(banks[i][1])
            summary += banks[i][2]
        else:
            route.append(banks[i + 1][0])
            inds.append(banks[i + 1][1])
            summary += banks[i + 1][2]
    if len(banks) - 1 not in inds and len(banks) - 2 not in inds:
        route.append(banks[-1][0])
        inds.append(banks[-1][1])
        summary += banks[-1][2]
    print(*route)
    print(summary)


main()
if __name__ == "__main__":
    main()

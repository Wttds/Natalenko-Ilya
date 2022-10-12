def main():
    banks = [("sber", 0, 2), ("ZXC", 1, 4), ("VTB", 2, 5), ("a", 3, 3), ("b", 4, 6)]
    summary, maximum, route, max_route, inds, max_inds = 0, 0, [], [], [], []
    for i in range(0, len(banks), 2):
        summary += banks[i][2]
        route.append(banks[i][0])
        inds.append(banks[i][1])
    if summary > maximum:
        maximum, max_route, max_inds = summary, route[:], inds
    summary, route, inds = 0, [], []
    for i in range(1, len(banks), 2):
        summary += banks[i][2]
        route.append(banks[i][0])
        inds.append(banks[i][1])
    if summary > maximum:
        maximum, max_route, max_inds = summary, route[:], inds
    print(maximum, *max_route, *max_inds, sep="\n")

main()
if __name__ == "__main__":
    main()

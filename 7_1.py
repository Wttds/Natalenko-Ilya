def main():
    banks = [("sber", 0, 2), ("ZXC", 1, 4), ("VTB", 2, 5), ("a", 3, 3), ("b", 4, 6)]
    summary, maximum, route, max_route = 0, 0, [], []
    for i in range(0, len(banks), 2):
        summary += banks[i][2]
        route.append(banks[i][0])
    if summary > maximum:
        maximum, max_route = summary, route[:]
    summary, route = 0, []
    for i in range(1, len(banks), 2):
        summary += banks[i][2]
        route.append(banks[i][0])
    if summary > maximum:
        maximum, max_route = summary, route[:]
    print(maximum, max_route)


main()
if __name__ == "__main__":
    main()

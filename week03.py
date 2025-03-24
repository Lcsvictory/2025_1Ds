def searching_duplicate(cities):
    result = []
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)

        if l1 == l2:
            result.append(city)
    result = set(result)
    return result

cities1 = ["Incheon", "Seoul", "Incheon", "Gangwondo", "Incheon", "Gawngju", "Seoul"]

result_d = searching_duplicate(cities1)
print(result_d)
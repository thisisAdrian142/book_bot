vehicles = [
        {"name": "car", "num": 7},
        {"name": "plane", "num": 10 },
        {"name": "boat", "num": 2}
]

def sort_on(dict):
    return dict["num"]

vehicles.sort(reverse=True, key=sort_on)
print(vehicles)

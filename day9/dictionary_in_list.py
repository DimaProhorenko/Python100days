def add_new_country(country, times_visited, cities):
    travel_log.append({
        "country": country,
        "visits": times_visited,
        "cities": cities
    })


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

add_new_country("Ukraine", 20, ["Odessa", "Kyiv", "Dnipro", "Lviv"])
print(travel_log)


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

def add_new_country(country_name, num_visits,cities):
    global travel_log
    new_dict = {}
    new_dict["country"] = country_name
    new_dict["visits"] = num_visits
    new_dict["cities"] = cities
    print(new_dict)
    travel_log.append(new_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
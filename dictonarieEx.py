countries = [
    {"c_name" : "Sri Lanka", "population" : "22.04 Million"},
    {"c_name" : "France", "population" : "68.29 Million"}
]

biggest_country = countries[0]

for country in countries:
    print(country["c_name"])

for country in countries:
    if country["population"] > biggest_country["population"]:
        biggest_country == country

print(f"The biggest country is {biggest_country["c_name"]}"  )
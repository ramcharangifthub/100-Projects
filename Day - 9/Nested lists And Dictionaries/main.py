capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

travel_log = {
    "France" : ["Paris","Lille","Dijon"],
    "Germany" : ["Stuttgart","Berlin"],
}


nested_lists = ["a","b",["c","d"]]
print(nested_lists[2][0])

travel_log = {
    "France" : {
        "num_times_visited" : 8,
        "cities_visited" : ["Paris","Lille","Dijion"] 
    },
    "Germany" : ["Stuttgart","Berlin"]
}

print(travel_log["Germany"][1])
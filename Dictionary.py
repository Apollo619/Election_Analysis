counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for key, values in counties_dict.items():
    message_to_candidate = (
        f"{key} county has {values:,} registered voters. "
        f"{key} county has {values:,} registered voters. "
        f"{key} county has {values:,} registered voters. ")

print(message_to_candidate)


#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
              #  {"county":"Denver", "registered_voters": 463353},
              #  {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
 #   for values in county_dict.values():
  #      print(values)

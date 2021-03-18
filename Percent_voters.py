my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
message_to_candidate = (
    f"You received {my_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {my_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

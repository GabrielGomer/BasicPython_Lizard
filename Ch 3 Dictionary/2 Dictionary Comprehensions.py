# Dictionary Comprehension
# Build a dict instance by producing
# key: value pair from any iterable

# Shows a list of pairs can be used directly w/ dict constructor
# A list of pairs can be used directly with the dict constructor
usa_team = [
    (0, 'Goulding'),
    (33, 'Gomer'),
    (53, 'Rogan'),
    (79, 'Sharapova'),
    (89, 'Juul'),
]
# Here the pairs are reversed: player is key, and jersey_number is value
jersey_number = {player: number for number,
                 player in usa_team}
print(jersey_number)
# Reversing the pairs again, values uppercased and items filtered by number
new = {number: player.upper() for player, number in jersey_number.items() if number < 66}
print(new)

time_dict = {
    "s" : 3600,
    "m" : 60,
    "h" : 1,
    "d" : 0.041
}

# get amounts and units (im sure they are valid)
amount = float(input("How much"))
from_unit = input("Starting unit")
to_unit = input("Converting to:")

# get the standard value
multiply_by = time_dict[to_unit]
standard = amount * multiply_by

# divide for desired value
divide_by = time_dict[from_unit]
answer = standard / divide_by

print(f" there are {answer} {to_unit} in {amount} {from_unit}")
mass_dict = {
    "mg" : 1000,
    "g" : 1,
    "kg" : 0.001
}

# get amounts and units (im sure they are valid)
amount = float(input("How much"))
from_unit = input("Starting unit")
to_unit = input("Converting to:")

# get the standard value
multiply_by = mass_dict[to_unit]
standard = amount * multiply_by

# divide for desired value
divide_by = mass_dict[from_unit]
answer = standard / divide_by

print(f" there are {answer} {to_unit} in {amount} {from_unit}")
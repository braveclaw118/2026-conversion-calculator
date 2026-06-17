mass_dict = {
    "mg" : 1000,
    "g" : 1,
    "kg" : 0.001
}

time_dict = {
    "s" : 86400,
    "m" : 1440,
    "h" : 24,
    "d" : 1
}

distance_dict = {
    "mm" : 1000,
    "cm" : 100,
    "m" : 1,
    "km" : 0.001
}


# Generates headings
def statement_generator(statement, decoration):
    print(f"\n {decoration * 5} {statement} {decoration * 5}")

# display instructions
def instructions():
    statement_generator("Instructions", "[]")
    print('''
Chose which unit system you want to convert in
(Distance, Time, Mass)
Choose the units you want to covert to and from
Use shortened units such as CM and MM rather than Centimeter and Millimeter
(Range for distance is from millimeter to kilometer)
(Range for time is from second to hour
(Range for mass is gram and kilogram)
Input your number and have fun!
(Use xxx to end)
    ''')

# ask user for units to convert (integer, text, image, xxx)
def get_unit_type():

    while True:
        response = input("Unit type").lower()

        #check for m or exit code
        if response == "xxx" or response == "m":
            return response

        # check for distance
        elif response in ['meter','distance','km','kilometer','cm','centimeter', 'millimeter','mm']:
            return "distance"

        # check for time
        elif response in ['time','minute','minutes','min','hour','hours','h','seconds','second','s','day','d']:
            return "time"

        #check for mass
        elif response in ['kg','g','kilogram','gram','kilo','weight','mass']:
            return "mass"

        # error message
        else:
            print("Please enter a valid measurement")

def num_check(question):

    error = "Please enter a positive Number that's above 0\n"
    while True:
        response = input(question).lower()
        if response == "xxx":
            return response
        try:
            # ask user for number
            response = float(response)
            # check number is above
            if 0 < response :
                return response
            else:(print(error))
        except ValueError:
            print (error)



def distance_calc():
    # get amounts and units (im sure they are valid)
    amount = float(input("How much"))
    from_unit = input("Starting unit")
    to_unit = input("Converting to:")

    # get the standard value
    multiply_by = distance_dict[to_unit]
    standard = amount * multiply_by

    # divide for desired value
    divide_by = distance_dict[from_unit]
    answer = standard / divide_by
    return answer

def time_calc():
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
    return answer


def mass_calc():
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
        return answer

# main routine here

# Want instructions? Get Conversion plus subscription for only $2.99 a week, or buy the yearly pass for only $199.99. Or, buy the double plus pass for $10.99 for full access to the application and 100 conversions a day!
statement_generator("Welcome to the Ultimate Conversion Calculator!", "-")
want_instructions = input("Press <Enter> to read instructions and any other key to continue")

if want_instructions == "":
    instructions()

while True:
    unit_type=get_unit_type()

    if unit_type == "xxx":
        break

    # if user says "I" check if they want img or int
    if unit_type =='m':

        want_image=input("please press <enter> for distance or any key for time")
        if want_image == "" :
            unit_type = "distance"
        else:
            unit_type = "time"

    if unit_type == "distance":
        distance_ans = distance_calc()
        print(distance_ans)
    elif unit_type == 'time':
        time_ans = time_calc()
        print(time_ans)
    else:
        mass_ans = mass_calc()
        print(mass_ans)

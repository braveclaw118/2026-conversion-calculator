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
(Range for distance is from millimeter to kilometer)
(Range for time is from second to hour
(Range for mass is gram and kilogram)
Input your number and have fun!
(Use xxx to end)
    ''')

# main routine
statement_generator("Welcome to the Ultimate Conversion Calculator!", "-")
want_instructions = input("Press <Enter> to read instructions and any other key to continue")

if want_instructions == "":
    instructions()
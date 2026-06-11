def num_check(question):

    error = "Please enter a positive Number that's above 0\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response
        try:
            # ask user for number
            response = float(response)
            # check number is between 1 and 200
            if 0 < response :
                return response
            else:(print(error))
        except ValueError:
            print (error)



# routine
while True:
    to_convert = num_check("Number to convert: ")
    if to_convert == "xxx":
        print("Thanks for using!")
        break
    else:
        print("You chose to convert", to_convert)

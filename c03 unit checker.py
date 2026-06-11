# ask user for units to convert (integer, text, image, xxx)
def get_unit_type():

    while True:
        response = input("File type").lower()

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








# main routine here
while True:
    unit_type=get_unit_type()


    # if user says "I" check if they want img or int
    if unit_type== 'm':

        want_image=input("please press <enter> for distance or any key for time")
        if want_image== "" :
            unit_type= "distance"
        else:
            unit_type= "time"

    print(f"You chose {unit_type}")

    if unit_type == "xxx":
        break
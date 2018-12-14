import csv

with open('NCHS_-_Leading_Causes_of_Death__United_States.csv', 'r') as file_reader:
    data_reader = csv.DictReader(file_reader)

    headers = data_reader.fieldnames

    print("Data of different cities")
    print("1 = City")
    print("2 = Day/Month/Year")
    n = input("For searching city-wise data enter '1' \nFor Day/Month/Year wise enter '2'\n")
    print("\n")

    if int(n) == 1:
        user_input = input("Enter the city name : ")
        fLines = file_reader.readline()
        print(fLines.rstrip())
        search = file_reader.readlines()

        for i, sLine in enumerate(search):
            if user_input.upper() in sLine.upper():
                print(sLine)
    elif int(n) == 2:
        user_input = input("Search day, month, year")
        fLines = file_reader.readline()
        print(fLines.rstrip())
        search = file_reader.readlines()

        for i, sLine in enumerate(search):
            if user_input.upper() in sLine.upper():
                print(sLine)

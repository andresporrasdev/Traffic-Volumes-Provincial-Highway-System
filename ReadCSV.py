import DTO
import csv

fileName = "Traffic_Volumes_-_Provincial_Highway_System.csv"

def readCSV(fileName):
    """
    Reads a CSV file and prints the data using a DTO object.
    Args:
        fileName (str): The path to the CSV file.
    Returns:
        None
    """
    with open(fileName) as data:
        reader = list(csv.reader(data)) #Using list to convert the reader object to a list
        for row in reader[1:2001]: #Loads the first 2000 rows ommiting the header
            DTO.set_sectionID(row[0])
            DTO.set_highway(row[1])
            DTO.set_section(row[2])
            DTO.set_sectionLength(row[3])
            DTO.set_sectionDescription(row[4])
            DTO.set_date(row[5])
            DTO.set_description(row[6])
            DTO.set_group(row[7])
            DTO.set_type(row[8])
            DTO.set_county(row[9])
            DTO.set_ptrucks(row[10])
            DTO.set_adt(row[11])
            DTO.set_direction(row[13])
            DTO.printDTO()
   
try:
    readCSV(fileName)
except FileNotFoundError as e: #Change the name or the file to test the exception
    print("File not found Error exception")
    print("The file name found is: " + str(e.filename))

print ("Program made by Andres Porras")


"""
with open("Traffic_Volumes_-_Provincial_Highway_System.csv") as data:
    reader = csv.reader(data)
    for i, row in enumerate(reader):
        if i <= 2:
            DTO.sectionIDfunc(row[0])

            print(row)
            #break
"""

"""
with open("Traffic_Volumes_-_Provincial_Highway_System.csv") as data:
    reader = csv.reader(data)
    for i, row in enumerate(reader):
        if i >= 2000:
            break
        print(row)
"""


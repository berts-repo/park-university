# Bert
# 4-25-21
# unit 6 assignment 2
#
# this program allows the user to enter search criteria of diseases and prints a formated table

# filter criteria for table. return if you want all the values of a field
def check_table(aline, check_location, check_disease, check_year):
    if check_location in aline:
        if check_disease in aline:
            if check_year in aline[-5:]:
                return True
    else:
        return False

# prints a table of filtered or nonfiltered criteria
def table(file):
    location = input('Enter state: ').upper()
    disease = input('Enter disease: ').upper()
    year = input('Enter year: ')

# table header    
    print('Location'.ljust(20), 'Disease'.ljust(15), 'Number'.ljust(10), 'Year\n'.ljust(5))

# runs each line of the table and calls inputs
    sum_total = 0
    for unformated_line in file:     
        if check_table(unformated_line, location, disease, year) == True:

# formats and totals the table, also adds commas to numbers
            line = unformated_line.strip('\n')
            aline = line.split(',')
            sum_total += int(aline[3])
            number = '{:,}'.format(int(aline[3]))

# prints the table
            print(aline[2].ljust(20), aline[0].ljust(15), number.ljust(10), aline[5].ljust(5))
    print(' '*20, 'Total:'.ljust(15), '{:,}'.format(sum_total).ljust(10))

        
# opens and closes the data file and calls the table funtion
file = open("health-no-head.csv", "r")
table(file)
file.close()

# Questions for assignment
# How many cases of Hepatitis A were reported in Utah in 2001? 59
# How many cases of polio have been reported in California? 47,743
# How many cases of all diseases were reported in 1956? 631,797

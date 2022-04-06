log_file = open("um-server-01.txt")


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


# line 1 is opening the code um-server-01.txt


# line 4 is defining the sales_reports
# line 5 is looping the code
# line 6 is cleaning the code
# line 7 is slicing information we want
# line 8 is choosing the condition
# line 9 is giving back the info
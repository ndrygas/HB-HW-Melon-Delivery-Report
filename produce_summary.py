
def daily_report(filename):
    """Takes in a file and prints the sales summary for that day"""
    the_file = open(filename)
    for line in the_file:
        words = line.rstrip().split("|")
        # words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

daily_report("um-deliveries-day-1.txt")

"""print("Day 1")
the_file = open("um-deliveries-day-1.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()

#old methods for reference
print("Day 2")
the_file = open("um-deliveries-day-2.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()"""


"""print("Day 3")
the_file = open("um-deliveries-day-3.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()"""

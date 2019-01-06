# Create some tools you want to use in other folders
import random

feet_in_mile = 5280
meter_in_kilometers = 1000
beetles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ect(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)

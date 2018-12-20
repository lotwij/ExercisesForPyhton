Indexfile = open("RankingLists.txt", "r") # open file in read mode, so you can't change/modify it after

# open("RankingLists.txt", "2") # open file in write mode, so you can change/modify it after

# open("RankingLists.txt", "r+") # open file in read+write mode, so you change/modify/read it after

# open("RankingLists.txt", "a") # open file in append mode, so you can't change/modify it after but you can add information


## Function to see if the file is readible:
print(Indexfile.readable()) # And it is, as we opended it in reading mode


print(Indexfile.read()) # Print the file

print(Indexfile.readline()) # Print the individual line
print(Indexfile.readline()) #And now it reads the second line after running it twice

print(Indexfile.readlines())
print(Indexfile.readlines()[1:2])

# Loop through line to find those specified:
for Country in Indexfile.readlines():
    print(Country)

Indexfile.close()




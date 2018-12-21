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

Indexfile = open("RankingLists.txt", "a") # open file in append mode, so you can add new data
Indexfile.write("\nBrazil	2016	94	73	95	-14.235004	-51.92528") # Add a new line to the dataset use \n
                                                                        # to add an enter

Indexfile = open("RankingLists.txt", "w") # open file in write mode, so you can overwrite
Indexfile.write("\nBrazil	2016	94	73	95	-14.235004	-51.92528") # Now the added line will replace all
                                                                        # the other data

Indexfile = open("RankingLists_copy.txt", "w") # By changing the file text name, you can make a copy of your file


## This way you can also create an HTML file:
webpage = open("Test.html", "w")
webpage.write("<p>TestPage</p>")





Indexfile.close()




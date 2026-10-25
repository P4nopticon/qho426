#nested book classification
#ask first question about the book
print("what type of cover does the book have?")
cover = input()
if cover == "soft":
    #asks second question to determin which patch to follow
    print("Is the book perfect-bound?")
    perfect = input()
    if perfect == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
#check whether book has a hard cover
elif cover == "hard":
    print("Book with hard covers can be more expensive!")
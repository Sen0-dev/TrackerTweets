#import trackerTweetClass

print("""
    Heyheyhey!! He and Welcome in THE TRACKER TWEETS PROGRAMM !!
    
    _______________________________________________________________________________
    | 1 | View all Tweets of a specific user
    -------------------------------------------------------------------------------
    | 2 | Views Tweets by key words
    -------------------------------------------------------------------------------
    | 3 | Views Tweets by "#"
    -------------------------------------------------------------------------------
    | 4 | Track an account ands receive e-mail when the author published new Tweets
    _______________________________________________________________________________
""")

choice = ""
while type(choice) != int:
    try:
        choice = int(input("    = "))
    except ValueError:
        print("Fais pas le malin et entre un nombre...")


match choice:
    case 1:
        print("View all Tweets of a specific user")

    case 2:
        print("Views Tweets by key words")

    case 3:
        print("Views Tweets by \"#")
    
    case 4:
        print("Tracker Tweets")


print("suiteee....")


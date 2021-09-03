# String Concatenation (aka how to put all strings together)
# Suppose we want to create a string that says "Subscribe to ___"
# youtuber = "Dharan" # some string variable

# # a few ways to do this
# print("Subscribe to " +youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famousPerson = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I Love to {verb1}.Stay hydrated and {verb2} like you are {famousPerson}!"

print(madlib)
print "Chapter 2"
name = raw_input ("Hi, there. What's your name?\n")
print "Hello, "+name+"!"
hours = input ("How many hours did you work this week?\n") #use input (not raw input) when expecting numbers
rate = input ("What's your hourly rate?\n") #use input (not raw input) when expecting numbers
pay = float(hours * rate)
print pay

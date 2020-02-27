#strigs and output

msg = "hello world"

print(msg)

# list

pets = ["dog", "cat", "bird"]

thepet = pets [1]

print(thepet)

# lenght & type

size = len(pets)

msg = "there are " + str(size) + " pets"

print(msg)

# loops

for animal in pets:
    print("I wish I had a " + animal)
#user input

ans = input ("what kind of pet do you have?")

print("you have a " + ans)

# booleans

known = ans in pets

print("it is "+str(known)+  " that I have seen a "+  ans)
 
#branching
if known:
    msg = "My friend has a " + ans
else:
    msg = "I don't know anyone with a " + ans
print(msg)

#dictionary

feels = {"cat":"selfish", "dog":"loyal", "bird":"feathery"}

if known: 
    pre = "e" if animal == "fish" else ""
    msg = ans + "s are very " + feels.get(ans)
else:
    msg = "I don't know anyone with a " + ans
print(msg)    
print ("welcome to my computer quiz") 

playing = input("do you want to play a game? ")
 
if playing != "yes" :
    quit ()
    
print ("okay! lets play")
score = 0

answer = input (" what does CPU stand for? ")
if answer == "central processing unit":
    print('correct')
    score += 1
else :
    print("incorrect")
    
answer = input (" what does GPU stand for? ")
if answer == "graphics processing unit":
    print('correct')
    score +=1
else :
    print("incorrect")
    
    
answer = input (" what does MS stand for? ")
if answer == "microsoft":
    print('correct')
    score += 1
else :
    print("incorrect")
    
answer = input (" what does amazon do? ")
if answer == "shopping":
    print('correct')
    score +=1
else :
    print("incorrect")

print ("you got " + str(score) + " questions correct")
print (" you got " + str((score/4) * 100) + "%")
import re
#For UBS by Adriel

#Scroll Test 1
validStrings= ["abc", "def"]
invalidStrings= ["123", "456"]
#Scroll Test 2
# validStrings= ["aaa", "abb", "acc"]
# invalidStrings= ["bbb", "bcc", "bca"]
#Scroll Test 3
# validStrings= ["abc1", "bbb1", "ccc1"]
# invalidStrings= ["abc", "bbb", "ccc"]
#Scroll Test 4
# validStrings= ["abc-1", "bbb-1", "cde-1"]
# invalidStrings= ["abc1", "bbb1", "cde1"]
#Scroll Test 5
# validStrings= ["a123", "b234"]
# invalidStrings= ["1234", "5678"]
#Scroll Test 6
# validStrings= ["foo@abc.com", "bar@def.net"]
# invalidStrings= ["baz@abc", "qux.com"]
#Custom Scroll
# validStrings = ["simpletest", "juststrings", "validinput"]
# invalidStrings = ["simple test", "just@strings", "valid.input"]

currentString = 0

#Used when current and before alphanumeric value are different   
def makePatternTwo(myContainer:str):
    #Return String
    patternCreated = ""
    #Make Logic so that each container refer to special character
    if(myContainer.isalpha()):
        #If container contains only 1 String
        if len(myContainer) == 1:
            patternCreated += "[%s]" %str(myContainer)
            
        #If container contain more than 1 String
        else: 
            patternCreated += "\D+"
    elif(myContainer.isdigit()):
        #If container contain only 1 number
        if len(myContainer) == 1:
            patternCreated += "[" + myContainer + "]"
        #If container contain more than 1 number
        else:
            patternCreated += "\d+"

    return patternCreated

#Used when current and before character type are different
def makePattern(myContainer:str):
    #Return String
    patternCreated = ""
    #Make Logic so that each container refer to special character
    if(myContainer.isalpha()):
        #If container contains only 1 String
        if len(myContainer) == 1:
            patternCreated += "\D"
        #If container contain more than 1 String
        else:
            patternCreated += "\D+"
        
    elif(myContainer.isdigit()):
        #If container contain only 1 number
        if len(myContainer) == 1:
            patternCreated += "\d"
        #If container contain more than 1 number
        else:
            patternCreated += "\d+"
        
    #If container contains character like !,@,#,$, etc
    else:
        #If container contains only 1 random character
        if len(myContainer) == 1:
            
            if(myContainer != " "):
                # Adding a backslash before myContainer
                patternCreated += "\\" + str(myContainer)
            else:
                #If myContainer contains blank space
                patternCreated += "."
                
        #If container contain more than 1 same random character
        else:
            # If myContainer contains more than 1 blank space
            if(myContainer.count(" ") > 1):
                patternCreated += "\s+"
            else:
                patternCreated += "\W+"

    return patternCreated

# matchpattern needs to have more cases considered?
def matchPattern(myPattern:str, currentString:str):
    myString = ""
    #Matches the strings
    pattern = re.compile(r'%s' %myPattern) # Put myPattern into inside '...'
    #Iterate through the whole sentence to find patterns
    matches = pattern.finditer(currentString)

    #For debugging, get the match value
    #Loop will not execute if "matches" is empty
    for match in matches:
        print("Match parent is " + match[0])
        #Set match to myString
        myString = match[0]
        # match is an object that only contains a string "match[0]" inside of it

    #If itemString match the string compiled from myPattern, this mean pattern is valid
    if(myString == currentString):
        print(myString + " match!")
        return True
    else:
        print(currentString + " doesn't match pattern")
        #Return false if myString doesn't match currentString
        #This is mostly used when myString from inValidString doesn't 
        # match any pattern
        return False
        

def checkValidity(patternTest: str):
    # patterntest is currently effectively just the final pattern
    validStringState = False
    invalidStringState = True

    #Check if patternTest contain certain pattern
    patternTest = changePattern(currentPattern= patternTest)

    #Loop and match each validString & invalidString with pattern
    #It must return true for validstring & for invalidstring
    for index in range(len(validStrings)):
        # Use range() to iterate
        # list's length to avoid index out of range error

        #Check whether pattern is correct 
        validStringState = matchPattern(myPattern= patternTest, 
                                        currentString= validStrings[index])
        
        if not validStringState:
            # This means that if validStringState is "False" then it breaks the loop so that the variable
            # won't be rewritten as true later on
            # This is done to tell us that pattern isn't right
            print("validStringState found INVALID at " + str(index))
            break
        
    # this is the same for loop but for invalidstring
    for index in range(len(invalidStrings)):
        invalidStringState = (matchPattern(myPattern= patternTest,
                                          currentString= invalidStrings[index]))
        #For debugging
        print("Current invalidStringState at index %s " %str(index) + "is " + str(invalidStringState))
        
        if invalidStringState:
            # This means that if invalidStringState is "True" then it breaks the loop so that the variable
            # won't be rewritten as false later on
            # This is done to tell us that pattern isn't right
            print("invalidString break at index = " + str(index))
            break

    #For debugging
    print("My final states are " + str(validStringState) + " and %s" %str(invalidStringState))
    #If validStringState is true and invalidStringState 
    # is false, return condition
    #This will also return patternTest
     # Return both patternTest and the validity state as a tuple
    return patternTest, validStringState and not invalidStringState

#Change pattern when pattern received are as shown below
#This is done to ensure pattern match only alphabets
def changePattern(currentPattern:str) -> str:
    if(currentPattern == "^\D+$"):
        #For debugging
        print("Pattern has been changed 1")
        currentPattern = "^[a-zA-Z]+$"

    elif(currentPattern == "^\D+\d$"):
        #For debugging
        print("Pattern has been changed 2")
        currentPattern = "^[a-zA-Z]+\d$"

    elif(currentPattern == "^\D+\d+$"):
        #For debugging
        print("Pattern has been changed 3")
        currentPattern = "^[a-zA-Z]+\d+$"

    #If currentPattern is not "^\D+$, return original version"
    return currentPattern

#Generate Gree Expression
def generate_gree_expression(valid_strings, invalid_strings):
    # if not valid_strings or not invalid_strings:
    #     return ""
    
    # Initialize the pattern
    pattern = "^"
    container= ""
    
    # Analyze character positions
    # Since length is different, but logic same for each String
    # We can find Regex Expression from the first string
    #Reference string used to make the pattern
    global currentString 
    myString = valid_strings[currentString]
    length = len(myString)

    
    for index in range(length):

        #Add to container first time
        if(index == 0):
            container += myString[index]
            print("1st type: My container is " + container + " at index: " + str(index))
            #For debugging
            print("Current return pattern is %s" %str(pattern))

        #Do function and clear container if item type 
        #current don't match the previous one
        #Check using isalpha and isdigit
        elif(index > 0 and 
             (str(myString[index]).isalpha() != str(myString[index-1]).isalpha()
              and str(myString[index]).isdigit() != str(myString[index-1]).isdigit()
              )):
            #Make new character everytime it doesn't match
            print("Before 2nd type: My container is " + container + " at index: " + str(index))
            pattern += makePattern(myContainer= container)
            #For debugging
            print("Current return pattern is %s" %str(pattern))
            #Clear container once function has been made & container cleared
            container = ""
            #Add the new different character to container
            container += myString[index]
            print("After 2nd type: My container is " + container + " at index: " + str(index))
        
        # If item type current and before is same (used when it is alphanumeric)
        elif(index > 0 and 
             (str(myString[index]).isalpha() == str(myString[index-1]).isalpha()
              and str(myString[index]).isdigit() == str(myString[index-1]).isdigit()
              )):
            #If current alphanumeric and before is same, implement differently
            #Only occur in the beginning
            if(index < 2 and (str(myString[index]) == str(myString[index-1]))):
                pattern += makePatternTwo(myContainer= container)
                #Add the current alphanumeric after makePattern has been conducted
                #on the previous container
                container += myString[index]
                
            #If content before and current is different
            else:
                container += myString[index]
                
            print("3rd type: My container is " + container + " at index: " + str(index))
            #For debugging
            print("Current return pattern is %s" %str(pattern))
        
        #If item type is not alphabetics or digit or a blank space
        else:
             #Make new character everytime doesn't match
            print("Before 4th type: My container is " + container + " at index: " + str(index))
            pattern += makePattern(myContainer= container)
            #For debugging
            print("Current return pattern is %s" %str(pattern))
            #Clear container once function has been made & container cleared
            container = ""
            #Add the new not same character to container
            container += myString[index]
            print("After 4th type: My container is " + container + " at index: " + str(index))

    #If pattern hasn't been made
    if(len(container) != 0):
        print("Container not made yet is " + container)
        inPattern = makePattern(myContainer= container)
        pattern += inPattern
        #For debugging
        print("Current return pattern is %s" %str(pattern))

    #Clear container once pattern 
    container = ""
    #Lastly add $ in the end
    pattern += "$"
    
    #Check pattern with pattern, valid strings and invalid strings
    #checkValidity function will return 2 values
    currentPattern, conditionValue = checkValidity(patternTest= pattern)
    if(conditionValue):
        #Clean pattern if there is a lot of \D+
        # print("Before clean pattern: " + pattern)
        return currentPattern
    else:
        pattern = "This pattern " +  str(pattern) + " is completely wrong"
        print(pattern)
        #Perhaps we can use recursion everytime the pattern is wrong
        #We need to make new pattern again by changing the reference validString
        # Do recursion
        currentString += 1
        print("CurrentString is " + str(currentString))
        if(currentString < len(valid_strings)):
            generate_gree_expression(validStrings, invalidStrings)

#Print Gree Expression
result = generate_gree_expression(validStrings, invalidStrings)
print("Final Gree Expression: " + str(result))

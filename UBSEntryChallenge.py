import re
#For UBS by Adriel

#Scroll Test 1
# validStrings= ["abc", "def"]
# invalidStrings= ["123", "456"]
#Scroll Test 2
# validStrings= ["aaa", "abb", "acc"]
# invalidStrings= ["bbb", "bcc", "bca"]
#Scroll Test 3
# validStrings= ["abc1", "bbb1", "ccc1"]
# invalidStrings= ["abc", "bbb", "ccc"]
#Scroll Test 4


#Scroll Test 5

def makePattern(myContainer:str):
    #Return String
    patternCreated = ""
    #Make Logic so that each container refer to special character
    if(myContainer.isalpha()):
        #If container contain 1 String
        if len(myContainer) == 1:
            patternCreated += "."
        #If container contain more than 1 String
        else:
            patternCreated += "\D+"
        
    elif(myContainer.isdigit()):
        #If container contain 1 Number
        if len(myContainer) == 1:
            patternCreated += "[" + myContainer + "]"
        #If container contain more than 1 Number
        else:
            patternCreated += "\d+"
        
    #If container contains character like !,@,#,$, etc
    else:
        #If container contain a random character
        if len(myContainer) == 1:
            patternCreated += str(myContainer)
        #If container contain more than 1 same random char
        else:
            patternCreated += "\W+"

    return patternCreated

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
    myString = valid_strings[0]
    length = len(myString)
    
    for index in range(length):

        #Add to container first time
        if(index == 0):
            container += myString[index]
            print("1st type: My container is " + container + " at index: " + str(index))

        #Do function and clear container if item type 
        #current don't match the previous one
        #Check using isalpha and isdigit
        elif(index > 0 and 
             (str(myString[index]).isalpha() != str(myString[index-1]).isalpha()
              and str(myString[index]).isdigit() != str(myString[index-1]).isdigit()
              )):
            #Make new character everytime doesn't match
            print("Before 2nd type: My container is " + container + " at index: " + str(index))
            pattern += makePattern(myContainer= container)
            #Clear container once function has been made & container cleared
            container = ""
            #Add the new not same character to container
            container += myString[index]
            print("After 2nd type: My container is " + container + " at index: " + str(index))
        

        # If item type current and before is same
        elif(index > 0 and 
             (str(myString[index]).isalpha() == str(myString[index-1]).isalpha()
              and str(myString[index]).isdigit() == str(myString[index-1]).isdigit()
              )):
            container += myString[index]
            print("3rd type: My container is " + container + " at index: " + str(index))

        
    
    #If pattern hasn't been made
    if(len(container) != 0):
        print("Container not made yet is " + container)
        inPattern = makePattern(myContainer= container)
        pattern += inPattern

    #Clear container once patern 
    container = ""
    #Lastly add $ in the end
    pattern += "$"
    
    # Validate against invalid strings
    # for invalid in invalid_strings:
    #     if re.fullmatch(pattern, invalid):
    #         return ""  # Return empty if an invalid string matches

    return pattern

#Print Gree Expression
result = generate_gree_expression(validStrings, invalidStrings)
print(result)
# items = "1333"
# print(items.__add__("444"))
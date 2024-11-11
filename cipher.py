# add your code here

# Solution #1- I wrote this one out relaying mostly on what I understood from what we have studied so far, it works, kinda, and felt very clunky. 
#I wasn't very sastified with it so I kept going.


text= input("Enter your secret message without spaces")
lowercase= text.lower()

letters= { "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}


message= []
for char in lowercase:
    message.append(letters.get(char))
coded_message =[]
for char in message:
    coded_message.append(char+5)
final_message = []
for char in coded_message:    
    final_message.append([k for k, v in letters.items() if v == char])

print(final_message)
    




# Solution #2- was found after much frustrated searching on the interwebs, I didn't want to just use someone else's solution, I wanted to 
#Understand how the code worked. And after stumbling upon some W3 python lessons, and another search to understand Ascii values, I present
#the more streamlined solution!


alpha = {97:118, 98:119, 99:120, 100:121, 101:122, 102:97, 103:98, 104:99, 105:100, 106:101, 107:102, 108:103, 109:104, 110:105, 111:106, 112:107, 113:108, 114:109, 115:110, 116:111, 117:112, 118:113, 119:114, 120:115, 121:116, 122:117, }
phrase= input("What is your secret message?")
lowercase= phrase.lower()


print(lowercase.translate(alpha))
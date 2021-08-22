m = float(input("Import your Math marks: "))
s = float(input("Import your Science marks: "))
e = float(input("Import your English marks: "))
t = float(input("Import your total marks: "))

if m>60 or m<0 : print("Maths marks must be within [0, 60]")
elif s>40 or s<0 : print("Science marks must be within [0, 40]")
elif e>60 or e<0 : print("English marks must be within [0, 60]")
elif t>280 or t<0 : print("Total marks must be within [0, 280]")

elif t>=266 and m==60 and s==40 : print("You are allowed to register in Egypt STEM Schools")
elif t>=266 and m==60 and e==60 : print("You are allowed to register in Egypt STEM Schools")
elif t>=266 and e==60 and s==40 : print("You are allowed to register in Egypt STEM Schools")
elif t>=274.5 and m==60 : print("You are allowed to register in Egypt STEM Schools")
elif t>=274.5 and e==60 : print("You are allowed to register in Egypt STEM Schools")
elif t>=274.5 and s==60 : print("You are allowed to register in Egypt STEM Schools")

else : print ("You are not allowed to register in Egypt STEM Schools")

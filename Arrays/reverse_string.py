# Reverse a string
# input = poly
# output = ylop

s = "poly"
out = ""

for i in range(len(s)-1,-1,-1):
    out+=s[i]
    
print(out)
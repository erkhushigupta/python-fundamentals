#Use of continue in for loops
#this can be used when one operation is required to be skipped and the next operation continues

for i in range(5):
    if i==3:
        continue
    print (i)

#Output: Expected output is:
#0
#1
#2
#4
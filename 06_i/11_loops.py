# while and for loops

#01 while loop eg we make baby until he growth

# x = 0
# while (x<=5):
#     print(x)
#     x = x+1 # increament is for avoiding the infinite loop

#02 for loop
# for x in range(5, 10):
#     print(x)
    
    # make an array
days = ["mon", "tue", "wed", "thur"]
for d in days:
    #if d == "wed": break # loop stops
    if d== "wed": continue # for skiping some thing
    print(d)

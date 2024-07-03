# Solution 1 (Using | operator)
dic1= {"Ali": 90, "Abubakar": 98}
dic2 ={ "Abubakar":99,  "Sheza":89}
print(dic1 | dic2)

# So;ution 2 (Using ** operator)
dic1= {"Ali": 90, "Abubakar": 98}
dic2 ={ "Abubakar":99,  "Sheza":89}
print({**dic1,**dic2})

# Solution 3 (Using copy() and update() method)
dic1= {"Ali": 90, "Abubakar": 98}
dic2 ={ "Abubakar":99,  "Sheza":89}
dic3 = dic2.copy()
dic3.update(dic1)
print(dic3)

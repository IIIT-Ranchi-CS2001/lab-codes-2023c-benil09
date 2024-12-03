"""
1. If the given string S1= “Maha Bharat” , generate the following strings by manipulating S1.
       a. “mAHA bHARAT”
       b. “Bharat”
       c. “BharatBharatBharat”
       d.  “Mera Bharat”
       e. “Mera Bharat Mahan”

"""

S1="Maha Bharat"

a=S1.swapcase()
print(a)

b=S1[5:]
print(b)

c=S1[5:]*3
print(c)

d=S1.replace("Maha","Mera")
print(d)

e=S1.replace("Maha","Mera")+ " " + "Mahan"
print(e)
# Jab hume pehle se pata ho ki loop kitni baar chalega, tab hum for loop use karte hain.

# for variable in sequence:
#     code


# For Loop Kab Use Karte Hain?

# Jab hume pehle se pata ho loop kitni baar chalega.


for i in range(5):
    print(i)



# range() Function

# range() numbers ki sequence generate karta hai.

for i in range(5):  #
    print(i)


for i in range(1, 6): #Stop value include nahi hoti.
    print(i)

# range(start, stop, step)
for i in range(1, 11, 2):   #Yahan step = 2 hai, matlab 2-2 ka jump.
    print(i)

# Reverse Loop
for i in range(10, 0, -1):  # -1 ka matlab reverse direction.
    print(i)


# Strings ko iterate karna
for char in "Python":    #String is a sequence of characters.
    print(char)


# List Par Loop

#List ke har item ko access karne ke liye loop use karte hain.

fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)
# Set Python ka ek collection data type hai jo unique values store karta hai.

# Duplicate values automatically remove ho jati hain.
# Indexing nahi hoti.
# Unordered collection hai (items ka order fixed nahi hota).
# Mutable hai (add/remove kar sakte hain).

numbers = {10, 20, 30, 20, 10}

# print(numbers)  # 20 10 30 (order change ho sakta hai) Duplicate Values Allowed Nahi Hai
# numbers.add(40)
# print(numbers)  # 20 10 30 40 (add karta hai)Mutable Hai
# print(numbers[0])  #index nahi hota




# Empty Set Banana
s = {}  #dictionary hai ❌
s = set()  #set hai ✅


print(type(s))



# Set Mein Item Add Karna
# add()
fruits = {"Apple", "Mango"}

# fruits.add("Banana")
# fruits.update(["Mango", "Banana"])
# fruits.remove("Mango")
# fruits.discard("Orange") #remove (Error Nahi Deta)
# fruits.pop() #remove last item
# fruits.clear() #remove all items

print(fruits)




# Loop in Set
fruits = {"Apple", "Mango", "Banana"}

for fruit in fruits:
    print(fruit)
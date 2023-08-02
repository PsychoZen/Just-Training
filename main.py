# Type conversion practice
tennis_balls = 10
print(str(tennis_balls))
print(type(tennis_balls))
print(type(str(tennis_balls)))

# Arithmetic Operator practice


num_lives = 10
print(num_lives)
new_num_lives = (10 * 2)
print(new_num_lives)

health = 100
print(health)
new_health = (100 // 2)
print(new_health)

num_enemies = 300
new_num_enemies = (300 // 34)
print(new_num_enemies)

weapons = 8
new_weaopns = (8 % 3)
print(new_weaopns)
# % is equal to the remainder left in the division whereas // is equal to the solution to the division problem without a remainder


# Practice with string concatination
player_name = "Sinister"
player_pet = "Alan"
player_data = (player_name + " & " + player_pet)
print(player_data)


# More operator combinations
health = 300
health -= 25    
#               (-= will subtract the number after equal sign to the original variable)
print (health)
health += 55    
#               (+= will add the number after equal sign to the original variable)
print(health)

#               (+= will work with strings however -= will not (for obvious reasons))
name = "Psycho"
name += " Zen"
print(name)


#logical and conditional operators practice (< , <= , > , >= , == , !=)     (will always return true or false)

result = 10 < 110
print(result)
print(type(result))
result = 10 != 20
print(result)
result = 10 == 20
print(result)
result = 10 <= 23
print(result)
result = 10 >= 32
print(result)

# also works with other defined variables

result = 100 != health
print(result)
result = 300 >= health
print(result)

# will also compare other defined variables
random = weapons <= num_lives
print(random)

# when comparing strings or single letters, the letters' place in the alphabet determines its' value (a=0 , b=1 , c=2, etc)

a = "a"
b = "b"
print(a > b)
# will return false, 0 is not greater than 1 

a = "abc"
b = "b"
print(a <= b)

# takes the first letters position

a = "z"
b = "b"
print(a <= b)

# will return false

print(5 > True)

# True takes the value of 1 if not defined

print(1 > True)

# will return false

# logical operators practice (and, not, or)

# not , will reverse the boolean value, i.e true to false and false to true

name = True
name = not name
print(name)

# will return false

health = 0
lives = 0
print(health <= 0 and lives <= 0)

# using and , if one or both variables are false it will return false

health = 10
lives = 5
print(health <= 0 and lives <= 0)

# will return false

# using or , if one or both value are true it will return true

health = 0
lives = 25
print(health <= 0 or lives <= 0)

# will return true

# collections practice (lists, tuples, ranges, dictionaries)

# lists ["each item will be an 'element'", "The first element will have the index position of 0", "items in a list are mutable"]

inventory = ['Iron Sword', 'Iron Helm', 'Iron Shield']
print(inventory) 
inventory[1] = 'Apples'
print(inventory)
inventory[2] = 'Potion'
print(inventory)
print(len(inventory))
print(max(inventory))
# will return the element with the highest alphatbetical value (a=0 , b=1, etc)
print(min(inventory))
# will return element with the lowest alphabetic value

# Append will add an element to the end of the list
inventory.append('Leather')
print(inventory)

# Insert will allow you to place an element at a specific index point (first parameter is the index point , second is the desired element)
inventory.insert(2, 'Hide')
print(inventory)

# Pop removes the last element on the list
inventory.pop()
print(inventory)

# Remove will specify a specific str to remove from the list
inventory.remove('Hide')
print(inventory)

# Clear will delete all items in the list, (example = [] also works)
inventory.clear()
print(inventory)

# Multi-dimensional lists (lists within lists) , they do not have to be the same length
inventory = [[1, 2, 3], 
             [1, 2, 3, 4],
             [1, 2],
             [1, 2, 3],
             [1, 2, 3]]
ruby_pouch = inventory[4][1]
print(ruby_pouch)
leather_bag = inventory[1][3]
print(leather_bag)

# append will also worth with multidimensional lists
inventory.append([1, 2, 3, 4, 5])
print(inventory)

# Each list will also have an index position as a whole
inventory[0].pop()
print(inventory)
inventory[2].pop()
print(inventory)

# Using the Slicing method we can add a list into a specific index point in our multidimensional lists
new_inventory = [1, 2, 3, 4, 5, 6]
index_to_insert = 3
inventory[index_to_insert:index_to_insert] = [new_inventory]
print(inventory)

# Tuples are immutable and only used to store data that won't change, format with key and value pairs ex. = ("example", 3)

item = ("Potions", 5)
name = item[0]
amount = item[1]
print(name)
print(amount)
print(item.count("Potions"))
print(item.index(5))

# Dictionaries use {} with key value pairs , searching requires key position on the list, not the index position

inventory = {'Sword': 1, 'Shield': 1, 'Healthkit': 10, 'Berries': 5}
print(inventory['Berries'])
print(inventory['Healthkit'])

inventory['gold'] = 100
print(inventory)

# Dictionaries can add more elements to their lists by giving a new element a value

inventory['Rations'] = 5
print(inventory)

# Modification of Dictionaries also requires the use of the key, and not the index position

inventory['Sword'] = 2
print(inventory)

inventory['gold'] += 1
print(inventory)

inventory['Rats'] = 32
print(inventory)
inventory['Rats'] -= 14
print(inventory)


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


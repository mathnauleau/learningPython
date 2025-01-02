## primitives data
number: int = 10
decimal: float = 2.5
text: str = 'Hello, world!'
active: bool = False

## strings of characters
names: list = ['Bob', 'Anna', 'Luigi'] ## list can be modified
coordinates: tuple = (1.5, 2.5) ## tuple cannot be modified
unique: set = {1, 4, 2, 9}
data: dict = {f'name': 'Bob', 'age': 203}

## List
social_platforms = ["Facebook", "Instagram", "Snapchat", "Twitter"]

print(number, unique)
print(number*decimal)
print(active)
print(social_platforms[1])

## Modify a list field
social_platforms[-1]= "X"
print(social_platforms[-1])

social_platforms.append("XYZ")
## .remove("item") to remove an item from the list
## del my_list[3] to remove an index from the list
## .sort() to sort alphabetically

print(social_platforms)

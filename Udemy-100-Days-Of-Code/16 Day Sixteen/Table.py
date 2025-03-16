from prettytable import PrettyTable

table = PrettyTable() #* created obj from prettytable

table.add_column("Pokemon Name",
["Pikachu","Charmander", "Squirtle"])

table.add_column("Pokemon Type",
["Electric","Fire", "Water"])

table.align = "l" #* accessing attrabute 

print(table)


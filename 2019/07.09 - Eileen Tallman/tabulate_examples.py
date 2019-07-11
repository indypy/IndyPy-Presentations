from tabulate import tabulate

###### Example 8. Tabulate Table 1 ######
print("\n" + "----------Tabulate Table 1--------------")
data = [[1, 'Arizona Aardvarks', 24, 12], 
        [2, 'New York Nightingales', 19, 14], 
        [3, 'Indiana Iguanas', 15, 19], 
        [4,'Pennsylvania Piglets', 10, 20]]
print (tabulate(data, headers=["Pos", "Team", "Win", "Lose"]))

###### Example 9. Tabulate Table 2 ######
print("\n" + "----------Tabulate Table 2--------------")
print(tabulate([["bacon", 3.5], ["eggs", 24]],
               ["Breakfast Food", "Quantity"], "fancy_grid"))
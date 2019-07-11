from texttable import Texttable

###### Example 6. Texttable 1 ######
table = Texttable()
table.set_cols_align(["l", "r", "c"])
table.set_cols_valign(["t", "m", "b"])
table.add_rows([["Name", "Age", "Nickname"],
                        ["Mr. George Bluth", 52, "George"],
                        ["Mr. George Oscar Bluth", 32, "Gob"],
                        ["Mrs. Lucille Bluth", "Not Reported", "Lucille"],
                        ["Mr. Michael George Bluth", 37, "Michael"],
                        ["Mrs. Lyndsey Funke", 37, "Lyndsey"]])

print("\n" + "---------- Texttable 1 ----------" + "\n")
print(table.draw() + "\n")


###### Example 7. Texttable 2 ######
table = Texttable()
table.set_deco(Texttable.HEADER)
table.set_cols_dtype(['t',  # text
                              'f',  # float (decimal)
                              'f',  # float (decimal)
                              'f']) # float (decimal)
table.set_cols_align(["l", "c", "c", "c"])
table.add_rows([["Name",    "Age(years)", "Time at Company(years)", "Sales"],
                        ["Jim Halpert",    26,    3,   310],
                        ["Pam Beasley", 26, 2,  0  ],
                        ["Michael Scott",    41,   10, 4],
                        ["Dwight Schrute", 31,   9, 270.6]])

print("\n" + "---------- Texttable 2 ----------" + "\n")
print(table.draw())
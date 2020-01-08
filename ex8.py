formatter = "%r %r %r %r"
print(formatter %(1,2,3,4))
print(formatter %("one", "two", "three", "four"))
print(formatter % (True, False, True, False))
print(formatter % (
    "I had this thing.",
    "That you could type up right",
    "that you didn't sing.",
    "so I said goodnight."
))
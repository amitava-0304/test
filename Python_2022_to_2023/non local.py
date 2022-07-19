def outer_function():
    a = 5
    def inner_function():
        global a
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)

outer_function()
print("Outer function: ",a)

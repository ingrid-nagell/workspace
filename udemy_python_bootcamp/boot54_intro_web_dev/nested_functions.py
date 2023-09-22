def outer():
    print("outer")

    def nested():
        print("inner")
    
    return nested


inner = outer()

inner() # activate with parenthesis
inner()
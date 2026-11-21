def make_greeting(language):
    def greet(name):
        if language == "Hindi":
            print("Namaste ,",name)
        else:
            print("Hello ,",name)
            
    return greet

g1=make_greeting("Hindi")
g1("Amit")

g2=make_greeting("english")
g2("Rahul")
 
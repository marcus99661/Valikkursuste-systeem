'''
with open("log.txt", "w") as file:
    file.write("")
    file.write("tere1\n")
    file.write("tere2")
'''
with open("log.txt", "w") as file:
    file.write("")
    def test(asd):
        print("----")
        print(asd)
        file.write(asd + "\n")
    
test("tere")
test("tere1")
test("tere2")

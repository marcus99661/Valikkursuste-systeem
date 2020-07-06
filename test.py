'''
ainedList = []
korral = 0
ained = {}
with open('ained.txt', 'r', encoding="utf-8") as ainedfail:
        for i in ainedfail: #### {Python 2 : {"kohad" : 40, "vajalikud" = "Python 1", "lisad" : ""}}
            temp1 = {}
            ainedList = i.replace("\n", "").split(";")
            #ained[ainedList[0]]["kohad"] = ainedList[1]
            #ained[ainedList[0]]["kohad"] = 40
            temp1["kohad"] = ainedList[1]
            temp1["kohtiVõetud"] = 0
            temp1["vajalikud"] = ainedList[2]
            temp1["lisad"] = ainedList[3]
            temp1["vastuVõetud"] = []
            ained[ainedList[0]] = temp1
            korral += 1
            print(ained)
        #print(ained)
'''
a = "tere,tere2,tere1".split()
b = "tere1".split()
#if test1.split(",").sort() in test.split(",").sort():
#    print("jah")

any_in = any(i in b for i in a)
print(any_in)
any_in = lambda a, b: bool(set(a).intersection(b))
print(any_in)
'''
if test1 in test.split():
    print("jah")
print(test.split())
'''
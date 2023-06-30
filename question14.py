# print your name 10 times without loop and manually print

counter=1
def printer(name):
    global counter
    if counter<=10:
        print(name)
        counter+=1
        printer(name)

printer("Rahul")
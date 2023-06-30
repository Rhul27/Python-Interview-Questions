# Count number of items having list as values

data={
    'jay':['male',23,20000],
    'raj':25,
    'ram':['male',28,25500],
    'vijay':['male',25]
}
counter=0
for i in data:
    if isinstance(data[i],list):
        counter+=1
print(counter)
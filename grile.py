a={2,5,3,5,4,1,2}
doubled=len(a)*2
print(doubled)

#2
var_1=[x for x in range(20) if x/2==0]
print(var_1)

#4
var=1
while var<4:
    for var in range(4):
        if var==1:
            var+=1
            break
        print('var=4')
    var+=1
print(var+=1)

# input list
input = [1,[3,35,2,5] ,2, [3, 47, [5, 6]], 7, 89, [9, [10]]]
#output list
output = []

def makeflatten(input):
    for i in input:
        if type(i) == list:
            makeflatten(i)
        else:
            output.append(i)

print('The original list: ',input)
makeflatten(input)
print('The Flatten List ', output)
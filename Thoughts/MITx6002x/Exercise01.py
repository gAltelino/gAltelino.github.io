maxWeight = 14

class Items(object):
    name = ''
    weight = 0
    value = 0

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def metric1(self):
    return self.value / self.weight

def metric2(self):
    return -self.weight

def metric3(self):
    return self.value

def printList(list):
    weight = 0
    totalValue = 0
    for item in list:
        if((item.weight + weight) < maxWeight):
            print(item.name)
            weight = weight + item.weight
            totalValue = totalValue + item.value

    print('Total items value: ', end="" )
    print(totalValue)
    print('\n')

dirt = Items('dirt', 4, 0)
computer = Items('computer', 10, 30)
fork = Items('fork', 5,1)
problemSet = Items('problemSet', 0, -10)

a = [dirt, computer, fork, problemSet]

#error due to the 0 division
# a.sort(key = metric1, reverse=True)
# print('Using the best overral method')
# printList(a)

a.sort(key = metric2, reverse=True)
print('Getting the light items first')
printList(a)

a.sort(key = metric3, reverse=True)
print('Getting the items with the biggest value first')
printList(a)


   

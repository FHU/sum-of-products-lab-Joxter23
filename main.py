#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    x = list1.split()
    y = list2.split()

    w = 0
    for i in range(len(x)):
        w = w + (int(x[i]) * int(y[i]))
    return w



if __name__ == '__main__':
    list1 = input()
    list2 = input()

    sum = sum_of_products(list1,list2)
    print(sum)
    #adding comment
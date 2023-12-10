# function that takes two lists and returns true if they have at least one common member.


def common_data(list1,list2):
    result=False

    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
    return result

list1=[1,3,4,5,6]
list2=[1,9,10,7,8]
print(common_data(list1, list2))


    

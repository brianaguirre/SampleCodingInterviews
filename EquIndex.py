__author__ = 'BrianAguirre'



def solutions(A):
    l = len(A)

    #ADD UP AND DOWN LISTS:
    addUp = [None] * l
    addUp[0] = 0
    addDown = [None] * l
    addDown[l-1] = 0


    if l == 0:
        return -1
    elif l == 1:
        return 0
    elif l > 1:
        for i in range(1, l):
            addUp[i] = addUp[i-1] + A[i-1]
        for i in range(l-2, -1, -1):

            addDown[i] = addDown[i+1] + A.get[i+1]

        for i in range(0, l):
            if addUp[i] == addDown[i]:
                return i

    else:
        #NO INDICES FOUND:
        return -1


#SAMPLE TESTS:
print(solutions([1,1,1,7,1,1,1]))
print(solutions([1]))
print(solutions([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
print(solutions([1,1,1,7,1,1,1]))
print(solutions([1000,1000,1000,1000,1000, 1000, 1000, 1000, 3000]))
print(solutions([1,1]))
print(solutions([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]))



__author__ = 'BrianAguirre'
__twitter__ = 'bnap48'


'''
REQUIREMENTS:
Given three int numbers, calculate which is the most late valid time you can write out of them.
EX: (1, 2, 3, 4) -> 23:41
It has to be valid. If no valid time can be made with the four numbers, return 'NO SOLUTION'
Print should be in format AB:CD, where AB and CD are both string numbers.

Assume numbers are positive integers.
Thus A, B, C, D >=0

NOTE: Don't worry about time or memory complexity, concentrate on correctness.

'''

#Consider the following brute force combination:
'''
AB CD
AB DC
AC BD
AC DB
AD BC
AD CB

BA CD
BA DC
BC AD
BC DA
BD AC
BD CA

CA BD
CA DB
CB AD
CB DA
CD AB
CD BA

DA BC
DA CB
DB AC
DB CA
DC AB
DC BA

'''
def lateTimeCalculator(A, B, C, D):

    #Create a Dictionary that has all the combinations above: Hours:Minutes
    hrsMins = []
    choose = [A, B, C, D]

    #CHOICES
    choseAB = [C, D]
    choseAC = [B, D]
    choseAD = [B, C]

    choseBA = [C, D]
    choseBC = [A, D]
    choseBD = [A, C]

    choseCA = [B, D]
    choseCB = [A, D]
    choseCD = [A, B]

    choseDA = [B, C]
    choseDB = [A, C]
    choseDC = [A, B]

    #HOURS AND MINUTES LISTS:
    hours = []
    mins = []

    #CREATING LISTS:
    for i in choose:
        #FOR A as leading hour
        if i == A:
            for j in choseAB:
                if j == C:
                    hours.append(i*10 + B)
                    mins.append(j*10 + D)
                else:
                    hours.append(i*10 + B)
                    mins.append(j*10 + C)

            for j in choseAC:
                if j == B:
                    hours.append(i*10 + C)
                    mins.append(j*10 + D)
                else:
                    hours.append(i*10 + C)
                    mins.append(j*10 + B)

            for j in choseAD:
                if j == C:
                    hours.append(i*10 + D)
                    mins.append(j*10 + B)
                else:
                    hours.append(i*10 + D)
                    mins.append(j*10 + C)

        #FOR B as leading hour
        if i == B:
            for j in choseBA:
                if j == C:
                    hours.append(i*10 + A)
                    mins.append(j*10 + D)
                else:
                    hours.append(i*10 + A)
                    mins.append(j*10 + C)

            for j in choseBC:
                if j == A:
                    hours.append(i*10 + C)
                    mins.append(j*10 + D)
                else:
                    hours.append(i*10 + C)
                    mins.append(j*10 + A)

            for j in choseBD:
                if j == A:
                    hours.append(i*10 + D)
                    mins.append(j*10 + C)
                else:
                    hours.append(i*10 + D)
                    mins.append(j*10 + A)

        #For C as leading hour:
        if i == C:
            for j in choseCA:
                if j == B:
                    hours.append(i*10 + A)
                    mins.append(j*10 + D)
                else:
                    hours.append(i*10 + A)
                    mins.append(j*10 + B)

            for j in choseCB:
                if j == A:
                    hours.append(i*10 + B)
                    mins.append(j*10 + D)
                else:
                    hours.append(i*10 + B)
                    mins.append(j*10 + A)

            for j in choseCD:
                if j == A:
                    hours.append(i*10 + D)
                    mins.append(j*10 + B)
                else:
                    hours.append(i*10 + D)
                    mins.append(j*10 + A)

        #For D as leading hour:
        if i == D:
            for j in choseDA:
                if j == B:
                    hours.append(i*10 + A)
                    mins.append(j*10 + C)
                else:
                    hours.append(i*10 + A)
                    mins.append(j*10 + B)

            for j in choseDB:
                if j == A:
                    hours.append(i*10 + B)
                    mins.append(j*10 + C)
                else:
                    hours.append(i*10 + B)
                    mins.append(j*10 + A)

            for j in choseDC:
                if j == A:
                    hours.append(i*10 + C)
                    mins.append(j*10 + B)
                else:
                    hours.append(i*10 + C)
                    mins.append(j*10 + A)


    ''' TEST IF HRS AND MINS ARE GOING IN AS COORDINATES:
    #Add all possibilities to coordianates:
    for i in range(0, len(hours)):
        hrsMins.append((hours[i],mins[i]))
    '''



    #Find largest one:
    for i in range(0, len(hours)):
        if hours[i] < 24 and (mins[i] < 60):
            hrsMins.append((hours[i],mins[i]))

    hrsMins.sort()
    hrsMins.reverse()

    solution = ""

    if len(hrsMins)<=0:
        solution = "NO SOLUTION."
    else:
        solution = str(hrsMins[0][0]) + ":" + str(hrsMins[0][1])


    return solution



print(lateTimeCalculator(2,2,3,5))
print(lateTimeCalculator(1,1,2,4))
print(lateTimeCalculator(1,1,1,1))
print(lateTimeCalculator(9,9,5,4))
print(lateTimeCalculator(0,0,0,0))
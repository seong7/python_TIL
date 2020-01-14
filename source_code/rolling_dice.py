print ("ROLLING DICE !")

while True :
    x = input ('Do you want to start? (Y/N)   ')
    if x == 'N' :
        print ('Bye bye !')
        break

    elif x == 'Y' :
        # dictionary 생성하여 결과 값 도출 (histogram)
        rslt = dict()
        while True :
# 횟수 지정하여 연속으로 굴리기 (for loop, list 사용)
#            numx = input ('How many times in a row? :  (only 1 available now) ')
#            try :
#                if numx == 'done':
#                    break
#                inumx = int(numx)
#            except :
#                print ('Only numbers.')
#                continue

            # random 기능으로 주사위 굴리기
            import random
            dice = random.randrange(1,7)
            print (dice)
            rslt[dice] = rslt.get(dice, 0) +1

            # 다시 굴릴 것인지 뭇기 (continue)
            while True :
                again = input ('Do you want to play more? (Y/N)')
                y = ['Y', 'N']
                if again in y :
                    break
                else :
                    print ('You can only choose one of "Y" or "N".')
                    continue

            if again == 'Y' :
                continue
            elif again == 'N' :
                break

    else :
        print ('You can only choose one of "Y" or "N".')
        continue

    if again == 'N':
        break

print ('Caculating the result....')
print (rslt)
# value로 내림차순하기

inp = input ('Enter a testscore between 0 and 1: ')
testscore = inp

def computegrade(testscore):

    try:

        testscore = float(inp)
        if testscore > 1 or testscore < 0 :
            print ('Please enter a number between 0 and 1')
        elif testscore >= 0.9:
            print ('Grade: A')
        elif testscore >= 0.8 :
            print ('Grade: B')
        elif testscore >= 0.7:
            print ('Grade: C')
        elif testscore >= 0.6:
            print ('Grade: D')
        elif testscore < 0.6:
            print ('Grade: F')

    except:
        print('Please enter a number between 0 and 1')

computegrade(testscore)

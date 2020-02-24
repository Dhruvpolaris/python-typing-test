import matplotlib.pyplot as plt
import time as t

print('---------- Typing Test ----------')
print('')
print("Submit a Word/Sentence that you would like to test (Ex: Roses are Red)")
word = input('Enter a word or a phrase to practice:').lower()
print('')
print('You will get 5 attempts to test yourself. Press enter after each input')
print("Once you start the Test, Type '",word,"' 5 times as fast as you can. All the best")
print('')
confirm = input("Press 'S' to start the test: ").lower()
if confirm == 's':
    timer = 3
    print('Get ready Test Starting in..')
    while timer != 0:
        t.sleep(1)
        print(timer)
        timer -=1
    time_arr = []
    time_attempt = [1,2,3,4,5]
    is_correct = []
    attempt = 1
    count =0
    while attempt <= 5:
        print('Attempt number',attempt)
        now_time = t.time()
        ip = input("Type -> ").lower()
        if ip == word:
            count +=1
            is_correct.append('Correct')
        else:    
            is_correct.append('Incorrect')
        type_time = t.time()
        time_taken = type_time - now_time
        time_arr.append(round(time_taken,3))
        attempt +=1
    print('***** TEST RESULT *****')
    print('You got',count,' /5 Correct!')
    print('')
    show_res = input("Press 'A' to view detailed analysis of your test: ").lower()
    if show_res == 'a':
        plt.bar(time_attempt,time_arr)
        plt.title('Typing Test Analysis')
        plt.ylabel('Time Taken in seconds ->')
        plt.xlabel('Attempts ->')
        plt.xticks(time_attempt,is_correct)
        plt.show()
        print('Thank You for attempting the test!') 
    else:
        print('Thank You for taking the typing test!')    
else:
    print('Run the program whenever you are ready..')


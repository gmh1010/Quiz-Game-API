import requests
import json
import pprint
import random
import html
correctAnswers=0
wrongAnswers=0
input("this is a quiz game,do you want to play? Press enter to start or quit to stop ")
endgame=" "
x=True
url=0
while x==True:
    i=1
    categorys=["Geography","History","Sports","Animals"]
    for category in categorys:
        print(str(i) + "- " + category)
        i+=1

    choise=input("Choose a category: ")
    while choise!="1" and choise!="2" and choise!="3" and choise!="4":
        choise = input("Choose a category by typing a number from 1 to 4 : ")
    urlChoise=choise
    choise = category[int(choise) - 1]
    if urlChoise=='1':
        url="https://opentdb.com/api.php?amount=1&category=22"
    elif urlChoise=='2':
        url="https://opentdb.com/api.php?amount=1&category=23"
    elif urlChoise=='3':
        url="https://opentdb.com/api.php?amount=1&category=21&type=multiple"
    elif urlChoise=='4':
        url="https://opentdb.com/api.php?amount=1&category=27"
    x = False

while (endgame.lower()!="quit"):
    r= requests.get(url)
    question=json.loads(r.text)
    if (r.status_code!=200):
        endgame=input("Sorry we run to a problem please try again or type quit ")
    else:
        data = json.loads(r.text)
        print(html.unescape(question['results'][0]['question']))
        print("---------------------------------")
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        answer_number=1
        random.shuffle(answers)

        for answer in answers:
            print(str(answer_number) + "- " + html.unescape(answer))
            answer_number += 1



        useranswer=input("give your answer only with numbers: ")
        while useranswer!="1" and useranswer!="2" and useranswer!="3" and useranswer!="4" and useranswer!="5":
            useranswer=input("give a correct number, from 1 to "+str(len(answers))+": ")


        useranswer = answers[int(useranswer) - 1]

        if (useranswer== correct_answer):
            print("---------------------------------")

            print("you are right")
            print("---------------------------------")
            correctAnswers+=1
            print("Correct Answers: ", correctAnswers, "\n Wrong Answers: ", wrongAnswers)
            endgame=input("if you want to continue press enter else write quit if you want to change category write ok: ")
        else:
            print("---------------------------------")
            wrongAnswers+=1
            print("wrong answer the correct one is "+correct_answer)
            print("---------------------------------")
            print("Correct Answers: ",correctAnswers,"\n Wrong Answers: ",wrongAnswers)
            endgame=input("if you want to continue press enter else write quit if you want to change category write ok: ")
    if endgame.lower()=="ok":
        x=True
        while x == True:
            i = 1
            categorys = ["Geography", "History", "Sports", "Animals"]
            for category in categorys:
                print(str(i) + "- " + category)
                i += 1
            choise = input("Choose a category: ")
            while choise != "1" and choise != "2" and choise != "3" and choise != "4":
                choise = input("Choose a category by typing a number from 1 to 4: ")
            urlChoise = choise
            choise = category[int(choise) - 1]
            if urlChoise == '1':
                url = "https://opentdb.com/api.php?amount=1&category=22"
            elif urlChoise == '2':
                url = "https://opentdb.com/api.php?amount=1&category=23"
            elif urlChoise == '3':
                url = "https://opentdb.com/api.php?amount=1&category=21&type=multiple"
            elif urlChoise == '4':
                url = "https://opentdb.com/api.php?amount=1&category=27"
            x = False



from requests import get
from sys import exit
from json import loads
from colorama import Fore, init

init(True)

gameID = "" # Enter game ID here; if not entered, you will be prompted
colors = ""
colorsList = []
coloramaColor = ""

def setColor(color):
    if color == "Red":
        return Fore.RED
    elif color == "Blue":
        return Fore.BLUE
    elif color == "Yellow":
        return Fore.YELLOW
    elif color == "Green":
        return Fore.GREEN

if gameID == "":
    gameID = input("\nEnter the quiz ID:\n\n")

r = get("https://play.kahoot.it/rest/kahoots/" + gameID)

if r.status_code == 200:
    try:
        question = loads(r.text)
        try:
            print("\nQuiz Title: " + question["title"] + "\n")
            for index, slide in enumerate(question["questions"]):
                if slide["type"] == "quiz" or slide["type"] == "multiple_select_quiz":
                    for i in range (len(slide["choices"])):
                        if slide["choices"][i]["correct"] == True:
                            if slide["type"] == "quiz":
                                colors = ["Red", "Blue", "Yellow", "Green"][i]   
                                coloramaColor = setColor(colors)
                                break
                            else:
                                colorsList.append(["Red", "Blue", "Yellow", "Green"][i])
                                coloramaColor = setColor(colorsList[0])
                        elif slide["choices"][i]["correct"] == False and slide["type"] == "quiz":
                            colors = "Unknown"
                    if len(colorsList) > 0:
                        print(" [" + Fore.MAGENTA + "Multiple Answers" + Fore.RESET + "] " + slide["question"] + " | [Answers] " + coloramaColor + "[" + ", ".join(colorsList) + "]")
                        colorsList.clear()
                    else:
                        print(" [" + Fore.CYAN + "Single Answer" + Fore.RESET + "] " + slide["question"] + " | [Answer] " + coloramaColor + "[" + colors + "]")
                elif slide["type"] == "content":
                    pass
                else:
                    print("[" + Fore.RED + "Error" + Fore.RESET + "] Unable to parse question type [" + Fore.MAGENTA + slide["type"] + Fore.RESET + "] but will come in a future update...")
            print("")
        except Exception as ex:
            print("\nQuiz throwing error:\n")
            print(str(ex) + "\n")
    except Exception as ex:
        print("\nQuiz throwing error:\n")
        print(str(ex) + "\n")
else:
    print("\nCan't find quiz.\n")
    print(r.status_code)

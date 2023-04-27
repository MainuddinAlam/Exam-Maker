# Author: Mainuddin Alam Irteja
# Date edited: 27/04/2023

# Importing important modules for the program
import sys
import string
import roman
import random

# Global variables for the program
questionDetails = []
alphabet = list(string.ascii_lowercase)
total_marks = 0


def Introduce_Program() -> None:
    """ 
    Function to introduce the program to the user
    """
    intro = """
        Welcome to the exam maker.
        This python program helps to create exams or quizzes.

        Program will prompt user to keep asking questions until he is done preparing
        the question paper. The question paper and sample answers will be be given as
        output files.
        """
    print(intro)


def select_question_type() -> None:
    """ 
    Function to make user select the type of question he wants
    """
    add_question = None

    # Menu for the user
    question_type = """ 
        Select the number to the appropriate question type

        1) Multiple Choice Question 
        2) Multi Select Question
        3) True False
        4) Short Answer Questions
        5) Fill in the blanks
        6) Matching
        """

    # Prompting user to add questions or end program
    add_question = input(
        "\nDo you want to add a question or finish making the paper ?\nEnter yes or no: ")
    if add_question != ('yes' or 'Yes' or 'No' or 'no'):
        print("\nIllegal input. We are exitting the program.")
        sys.exit()

    # Prompting user to select his desired question type
    # The corresponding function of the question type will be called to ask for
    # further details
    while (add_question != 'no'):
        print(question_type)
        option = int(
            input("Select the number according to the question type: "))
        if option == 1:
            add_mcq(option)
        elif option == 2:
            add_multi_select(option)
        elif option == 3:
            add_true_false(option)
        elif option == 4:
            add_short_answer(option)
        elif option == 5:
            add_fill_in_blanks(option)
        elif option == 6:
            add_matching(option)
        else:
            print("\nIllegal input. We are exitting the program.")
            sys.exit()  # exitting the program due to illegal input

        add_question = input(
            "\nDo you want to add a question or finish making the paper ?\nEnter yes or no: ")


def details() -> tuple:
    """
    Helper function for adding multiple choice questions and multi-select questions

    Returns:
        tuple: returns the question and the options list for multiple choice and
        multi-select questions
    """
    # Function will ask user his question and the number of options he would like.
    # The function will append each option to the local list, optionsList.
    optionsList = []
    question = input("\nEnter your question: ")
    n = int(input("\nHow many options would you like? "))
    for i in range(n):
        option = input("Enter option {0}: ".format(i + 1))
        optionsList.append(option)
    return question, optionsList


def add_mcq(option: int) -> None:
    """
    Function to add multiple-choice questions.

    Args:
        option (int): this variable is used to signify that a multiple-choice question is chosen
    """
    # The details() method will ask for the question and options list.
    # Marks will be set to 1. Then function will ask for the answer. These information
    # will be appended to the local list, quentionInfo. The local list will be then
    # appended to the global list, questionDetails.
    questionInfo = []
    q, optList = details()
    marks = 1
    ans = input("\nEnter the correct answer: ")
    questionInfo.extend([option, q, len(optList), optList, ans, marks])
    questionDetails.append(questionInfo)


def add_multi_select(option: int) -> None:
    """
    Function to add multi-select question.

    Args:
        option (int): this variable is used to signify that a multiple-select question is chosen
    """
    # The details() method will ask for the question and options list.
    # Marks will be set to 3. Then function will ask for the number of correct answers.
    # Each answer will be asked to be given from the user. All these information
    # will be appended to the local list, quentionInfo. The local list will be then
    # appended to the global list, questionDetails.
    questionInfo = []
    q, optList = details()
    howMany = int(input("\nHow many correct answers are there ?: "))
    ansList = []
    marks = 3
    for i in range(1, howMany + 1):
        ans = input("\nEnter answer {0} : ".format(i))
        ansList.append(ans)
    questionInfo.extend([option, q, len(optList), optList, ansList, marks])
    questionDetails.append(questionInfo)


def genericQuestion(option: int, marks: int, prompt: str, ansInfo: str) -> None:
    """
    Helper function made to add questions of some type.

    Args:
        option (int): this variable is used to signify which question type is chosen
        marks (int): the marks of that question
        prompt (str): the question set by the particular question type
        ansInfo (str): Prompting for answer
    """
    # The function will ask for the question and answer from the user.
    # The question, answer alongside information from the caller function will be
    # appended to the local list, quentionInfo. The local list will be then
    # appended to the global list, questionDetails
    questionInfo = []
    question = input("\n{0}: ".format(prompt))
    answer = input("\n{0}: ".format(ansInfo))
    questionInfo.extend([option, question, answer, marks])
    questionDetails.append(questionInfo)


def add_true_false(option: int) -> None:
    """
    Function to add a true false question

    Args:
        option (int): this variable is used to signify that a true-false question is chosen
    """
    # Setting statements and marks and passing it to the genericQuestion function
    # genericQuestion function will add the true false question
    info = "Enter your statement"
    ansInfo = "Enter your answer (Either true of false)"
    marks = 1
    genericQuestion(option, marks, info, ansInfo)


def add_short_answer(option: int) -> None:
    """
    Function to add a short answer question

    Args:
        option (int): this variable is used to signify that a short answer question is chosen
    """
    # Setting statements and marks and passing it to the genericQuestion function
    # genericQuestion function will add the short answer question
    info = "Enter your question"
    ansInfo = "Enter your answer"
    marks = 5
    genericQuestion(option, marks, info, ansInfo)


def add_fill_in_blanks(option: int) -> None:
    """
    Function to add a fill in the blanks question

    Args:
        option (int): this variable is used to signify that a fill in the blanks question is chosen
    """
    # Setting statements and marks and passing it to the genericQuestion function
    # genericQuestion function will add the fill in the blanks question
    info = "Enter your statement and include ..... for the blank"
    ansInfo = "Enter your answer"
    marks = 1
    genericQuestion(option, marks, info, ansInfo)


def add_matching(option: int) -> None:
    """
    Function to add matching questions

    Args:
        option (int): this variable is used to signify that a matching question is chosen
    """
    # This function prompts user to enter the amount of options he needs for the
    # matching question. The left sided options will be added to the lList and the
    # right sided options will be added to the rList. This info will be appended to
    # the local list, questionInfo. The questionInfo list will be added to the
    # global list, questionDetails
    questionInfo = []
    rList = []
    lList = []
    n = int(input("\nEnter the amount of options: "))
    marks = n
    for i in range(1, n + 1):
        left = input("\nEnter statement {0} (will be on the left): ".format(i))
        right = input("\nEnter answer {0} (Will be on right): ".format(i))
        rList.append(right)
        lList.append(left)
    questionInfo.extend([option, n, rList, lList, marks])
    questionDetails.append(questionInfo)


def display_mcq(qInfo: list, underLine_Amount: int, qNum: int, qFile, aFile) -> None:
    """
    Function to display the multiple choice question to the Questions.txt file and
    its answer to the Answer.txt file

    Args:
        qInfo (list): the list that has all the information about a certain mcq
        underLine_Amount (int): the amount of underlines one line will have
        qNum (int): the question number
        qFile (_type_): the output file, Questions.txt
        aFile (_type_): the output file, Answers.txt
    """
    # This function will format how to display the multiple choice question
    # to the Questions.txt file. Marks for this question will be shown at
    # the end of this file. The answer will be written to the output file,
    # Answers.txt
    global alphabet, total_marks
    qFile.write("\n{0}. {1}\n".format(qNum, qInfo[1]))
    for i in range(0, qInfo[2]):
        qFile.write("\t{0}) {1}\n".format(alphabet[i], qInfo[3][i]))
        if qInfo[3][i] == qInfo[4]:
            aFile.write("\n{0}. {1}) {2}\n".format(
                qNum, alphabet[i], qInfo[4]))
    qFile.write("\nMarks for this question = {0}\n".format(qInfo[5]))
    total_marks += qInfo[5]
    qFile.write("-" * underLine_Amount + "\n")
    aFile.write("-" * underLine_Amount + "\n")


def display_multi_select(qInfo: list, underLine_Amount: int, qNum: int, qFile, aFile) -> None:
    """
    Function to display the multiple select question to the Questions.txt file and
    its answers to the Answer.txt file

    Args:
        qInfo (list): the list that has all the information about a certain multi select question
        underLine_Amount (int): the amount of underlines one line will have
        qNum (int): the question number
        qFile (_type_): the output file, Questions.txt
        aFile (_type_): the output file, Answers.txt
    """
    # This function will format how to display the multiple select question
    # to the Questions.txt file. Marks for this question will be shown at
    # the end of this file. The answers will be written to the output file,
    # Answers.txt
    global alphabet, total_marks
    qFile.write("\n{0}. {1}\n".format(qNum, qInfo[1]))
    aFile.write("{0}".format(qNum))
    for i in range(0, qInfo[2]):
        qFile.write("\t{0}) {1}\n".format(alphabet[i], qInfo[3][i]))
        if qInfo[3][i] in qInfo[4]:
            aFile.write("\t{0}) {1}\n".format(alphabet[i], qInfo[3][i]))
    qFile.write("\nMarks for this question = {0}\n".format(qInfo[5]))
    total_marks += qInfo[5]
    qFile.write("-" * underLine_Amount + "\n")
    aFile.write("-" * underLine_Amount + "\n")


def generic_Display(qInfo: list, underLine_Amount: int, qNum: int, qFile, aFile) -> None:
    """
    Function to display a generic question to the Questions.txt file and
    its answer to the Answer.txt file

    Args:
        qInfo (list): the list that has all the information about a question
        underLine_Amount (int): the amount of underlines one line will have
        qNum (int): the question number
        qFile (_type_): the output file, Questions.txt
        aFile (_type_): the output file, Answers.txt
    """
    # This function will format how to display questions of some question type
    # to the Questions.txt file. Marks for this question will be shown at
    # the end of this file. The answers will be written to the output file,
    # Answers.txt . This function is used to format true false and fill in the
    # blanks questions
    global total_marks
    qFile.write("\n{0}. {1}\n".format(qNum, qInfo[1]))
    qFile.write("\nMarks for this question = {0}\n".format(qInfo[3]))
    total_marks += qInfo[3]
    aFile.write("\n{0}. {1}\n".format(qNum, qInfo[2]))
    qFile.write("-" * underLine_Amount + "\n")
    aFile.write("-" * underLine_Amount + "\n")


def display_short_answer(qInfo: list, underLine_Amount: int, qNum: int, qFile, aFile) -> None:
    """
    Function to display the short answer question to the Questions.txt file and
    its answer to the Answer.txt file

    Args:
        qInfo (list): the list that has all the information about a certain short answer question
        underLine_Amount (int): the amount of underlines one line will have
        qNum (int): the question number
        qFile (_type_): the output file, Questions.txt
        aFile (_type_): the output file, Answers.txt
    """
    # This function will format how to display the short answer question
    # to the Questions.txt file. Marks for this question will be shown at
    # the end of this file. The answer will be written to the output file,
    # Answers.txt
    global total_marks
    qFile.write("\n{0}. {1}\n".format(qNum, qInfo[1]))
    marks = qInfo[3]
    for i in range(1, marks + 3):
        qFile.write("\n" + ("." * 60) + "\n")
    qFile.write("\nMarks for this question = {0}\n".format(marks))
    total_marks += marks
    aFile.write("\n{0}. {1}\n".format(qNum, qInfo[2]))
    qFile.write("-" * underLine_Amount + "\n")
    aFile.write("-" * underLine_Amount + "\n")


def get_The_Index(searchStr: str, lList: list, rList: list, rightList: list) -> int:
    """
    Helper function for the display_matching function.

    Args:
        searchStr (str): the statement on the left side
        lList (list): the left list containing statements on the left side
        rList (list): the right list containing statements on the right side
        rightList (list): this list contains the statements alongside roman numbers

    Returns:
        int: the index of the right statement in the rightList
    """
    # This function uses searchStr(Left statement) and finds its index. This index
    # is used to find the right statement on rList. For loop is used to find
    # [right_Statement, romanNum] in the rightList. The index is found through
    # that code and returned to the function that called
    iDex = lList.index(searchStr)
    right_Statement = rList[iDex]
    returning_Index = 0
    for i in range(0, len(rList)):
        romanNum = roman.toRoman(i + 1)
        search_List = [right_Statement, romanNum]
        if search_List in rightList:
            returning_Index = rightList.index(search_List)
    return returning_Index


def display_matching(qInfo: list, underLine_Amount: int, qNum: int, qFile, aFile) -> None:
    """
    Function to display the matching questions to the Questions.txt file and
    its answers to the Answer.txt file

    Args:
        qInfo (list): the list that has all the information about the matching question
        underLine_Amount (int): the amount of underlines one line will have
        qNum (int): the question number
        qFile (_type_): the output file, Questions.txt
        aFile (_type_): the output file, Answers.txt
    """
    # This function will format how to display the matching question
    # to the Questions.txt file. Marks for this question will be shown at
    # the end of this file. The answer will be written to the output file,
    # Answers.txt . The helper function get_The_Index is needed for correct
    # formatting of the answers
    global total_marks, alphabet

    # original lists
    rList = qInfo[2]
    lList = qInfo[3]

    rightList = []
    qFile.write("\n{0}. Match the following: \n".format(qNum))

    # randomizing list positions for matching questions
    random.shuffle(qInfo[2])
    random.shuffle(qInfo[3])

    aFile.write("{0}. : \n".format(qNum))
    for i in range(0, qInfo[1]):
        localList = []
        qFile.write("\n{0}) {1:<20} \t\t {2:>10}) {3}\n".format(
            alphabet[i], qInfo[3][i], roman.toRoman(i + 1), qInfo[2][i]))

        # appending to local lists
        localList.append(qInfo[2][i])
        localList.append(roman.toRoman(i + 1))
        rightList.append(localList)

    # Display the matching answers to the Answers.txt file
    for i in range(0, qInfo[1]):
        iDex = get_The_Index(qInfo[3][i], lList, rList, rightList)
        aFile.write("\n{0}) {1:<20} \t\t {2:>10}) {3}\n".format(
            alphabet[i], qInfo[3][i], rightList[iDex][1], rightList[iDex][0]))
    qFile.write("\nMarks for this question = {0}\n".format(qInfo[4]))
    total_marks += qInfo[4]
    qFile.write("-" * underLine_Amount + "\n")
    aFile.write("-" * underLine_Amount + "\n")


def write_To_File() -> None:
    """
    Function to write the information to the output files
    """
    # The name of the output files are Questions.txt and Answers.txt
    # This functions formats the output files. Each question type calls another
    # function which describes how the question will be represented in the question
    # paper. Those function also distinguishes how the answers of each question type
    # will be represented
    global total_marks
    with open("Questions.txt", "w") as qFile, open("Answers.txt", "w") as aFile:
        underLine_Amount = 80
        exam_header = "\t" * 9 + "Exam Paper"
        ans_header = "\t" * 9 + "Answers"
        qFile.write("-" * underLine_Amount + "\n")
        qFile.write(exam_header + "\n" + ("-" * underLine_Amount) + "\n\n")
        aFile.write("-" * underLine_Amount + "\n")
        aFile.write(ans_header + "\n" + ("-" * underLine_Amount) + "\n\n")
        for i in range(0, len(questionDetails)):
            qInfo = questionDetails[i]
            option = questionDetails[i][0]
            if option == 1:
                display_mcq(qInfo, underLine_Amount, i + 1, qFile, aFile)
            elif option == 2:
                display_multi_select(
                    qInfo, underLine_Amount, i + 1, qFile, aFile)
            elif option == 3:
                generic_Display(qInfo, underLine_Amount, i + 1, qFile, aFile)
            elif option == 4:
                display_short_answer(
                    qInfo, underLine_Amount, i + 1, qFile, aFile)
            elif option == 5:
                generic_Display(qInfo, underLine_Amount, i + 1, qFile, aFile)
            else:
                display_matching(qInfo, underLine_Amount, i + 1, qFile, aFile)
        qFile.write("\nMarks for the Paper: {0}.\n".format(total_marks))
        qFile.write("-" * underLine_Amount + "\n")


# Try the following or catch exceptions if they arise
try:
    Introduce_Program()  # Introduce the program
    select_question_type()  # Select the question type
    write_To_File()  # Write to the file
    print("\nThe question paper and answer paper have been created to the output files.")
except:
    print("\nPlease try again because there are bugs.")

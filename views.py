import Controllers
from Controllers import CommandController, Input, is_number
from TextMessages import MenuMessage, ChooseMatrixSizeMessage, ViewBorderText, ExitMessage, InputCommandErrorMessege, \
    InputNumberErrorMessage, MatrixInputMessage, InputIs_Messege, MatrixCheck, ShowDeterminantMessage, \
    ShowSetTriangleMessage


def Menu():
    ViewBorderText()
    while (True):

        MenuMessage(Controllers.Matrix)
        command = Input()
        MenuCommandController(command)


def MenuCommandController(input):
    Controllers.ChangeView()
    InputIs_Messege(input)
    if input == "РАЗМЕР":
        # print("вы ввели РАЗМЕР")
        ChooseMatrixSize()
    elif input == "ВВОД":
        # print("вы ввели ВВОД")
        MatrixInput()
    elif input == "ОПР":
        ShowDeterminant()
        #print("вы ввели ОПР")  # я это оставил в качестве заглушки, иначе начинает материться, мол, поч пусто
    elif input == "СВО":
        print("вы ввели СВО")
        print(Controllers.Matrix) #ПЕРВУЮ СТРОКУ КОРЁЖИТ НЕЗАВИСИМО ОТ  СПОСОБА ВЫВОДА НА ЭКРАН. ЕЁ КОРЁЖИТ ПО-НАСТОЯЩЕМУ
        # ОСТАЛЬНЫЕ СТРОКИ СОХРАНЯЮТ НЕЙТРАЛИТЕТ
    elif input == "ДИАГ":
        print("вы ввели ДИАГ")
    elif input == "ТРЕУГ":
        ShowTriangleView()
    elif input == "НАЗАД":
        print("вы ввели НАЗАД")  # под вопросом для Menu
    elif input == "ВЫХОД":
        print("вы ввели ВЫХОД")
        Exit()
        return True
    else:
        InputCommandErrorMessege(input)
    return False
    # elif input=="":
    #     print("")


def Exit():  # выход из программы
    ExitMessage()  # "пока-пока"
    exit()


def ChooseMatrixSize():  # выбор размера матрицы
    Controllers.ChangeView()
    while (True):
        ChooseMatrixSizeMessage()
        command = Input()
        if ChooseMatrixSizeCommandController(command):
            break


def ChooseMatrixSizeCommandController(input):  # ну а нафига?
    Controllers.ChangeView()
    if is_number(input):
        # global MatrixSize  # ну а чё мне ещё делать?
        # таскать за собой список в качестве чемодана????????
        correct_number=int(float(input)) # напрямую почему-то низзя
        if correct_number<1:
            InputNumberErrorMessage(input) # мне лень переправлять отрицательные в положительные, пусть  вводит правильно
        else:
            Controllers.MatrixSize = correct_number
            Controllers.Matrix= Controllers.CreateNewSquareMatrix(correct_number) #пересоздаём матрицу под новый размер
            return True
    elif input == "ВЫХОД":
        InputIs_Messege(input)
        Exit()
    elif input == "НАЗАД":
        InputIs_Messege(input)
        return True
    else:
        InputNumberErrorMessage(input)
    return False


def MatrixInput():  # в разработке
    Controllers.ChangeView()
    # newMatrix = [ [0]*Controllers.MatrixSize for i in range(Controllers.MatrixSize)]
    #newMatrix = Controllers.CreateNewSquareMatrix(Controllers.MatrixSize)
    newMatrix=Controllers.Matrix #ВРЕМЕННЫЙ КОСТЫЛЬ. Не помог. Дефолтная матрица всё так же сбоит ДА ******* РОТ
    #значит дело не в способе создания матрицы?
    for i in range(Controllers.MatrixSize):
        for j in range(Controllers.MatrixSize):
            while (True):
                MatrixInputMessage(newMatrix,i,j)
                #MatrixCheck(newMatrix)
                input = Input()
                Controllers.ChangeView()  #  каждый раз "перелистывать"
                InputIs_Messege(input)
                if input == "СЛЕД":
                    break
                elif input == "ПРЕД": #ЭТА ШТУКА НА АРМАГЕДОН ПЕРВОЙ СТРОКИ НЕ ВЛИЯЕТ. Изымали- не помогло
                    if j == 0:  # если в первом столбце
                        if i == 0:  # и в первой строке
                            print("Ты в начале матрицы, куда ещё раньше то??????")
                        else:  # и не в первой строке
                            i = i - 1
                            j = Controllers.MatrixSize - 1
                    else:  # если не в первом столбце
                        j = j - 1

                elif input == "НАЗАД":
                    return True  # выйти из функции счастливым и не сохранившимся
                elif input == "СОХР":
                    Controllers.Matrix = newMatrix
                    return True  # выйти из функции счастливым # мб не выходить а просто сейвиться
                elif input == "ВЫХОД":
                    Exit()  # завершение работы всей программы
                # elif input == "СТР":
                #     Exit()  # завершение работы всей программы
                elif is_number(input):  # если не подошла ни одна команда, проверим, является ли введённая штука числом
                    newMatrix[i][j] = input
                    #MatrixCheck(newMatrix)
                    break
                else:
                    InputNumberErrorMessage(input)  # вы ввели полную фигню
    print(" МАТРИЦА СОХРАНЕНА")
    Controllers.Matrix = newMatrix

def ShowDeterminant():
    ViewBorderText()
    while (True):
        ShowDeterminantMessage(  Controllers.Matrix, Controllers.Detarminant(Controllers.Matrix)   )
        command = Input()
        if ShowDeterminantCommandController(command):
            break

def ShowDeterminantCommandController(input):
    Controllers.ChangeView()
    InputIs_Messege(input)
    if input == "ВЫХОД":
        Exit()
    elif input == "НАЗАД":
        return True
    else:
        InputNumberErrorMessage(input)
    return False

def ShowTriangleView():
    ViewBorderText()
    newMatrix = Controllers.SetMatrixTriangle(Controllers.Matrix)
    while (True):
        ShowSetTriangleMessage(  Controllers.Matrix, newMatrix   )
        command = Input()
        if ShowTriangleViewCommandController(command,newMatrix):
            break

def ShowTriangleViewCommandController(input, newMatrix):
    Controllers.ChangeView()
    InputIs_Messege(input)
    if input == "ВЫХОД":
        Exit()
    elif input == "НАЗАД":
        return True
    elif input=='ДА':
        Controllers.Matrix=newMatrix
        return True
    else:
        InputNumberErrorMessage(input)
    return False
# def MatrixInputCommandController(input): #под вопросом, из этой штуки ****** как запарно возвращать значения кроме true/false
#     # а ведь надо ещё и значение элемента возвращать...
#     # return списком == костыль, т.к. его нужно будет точно также расшифровывать при помощи 99999 elif
#     if input=="СЛЕД":
#         InputIs_Messege(input) #а может эту штуку просто в начало перенести?????
#     elif input=="ПРЕД":
#         InputIs_Messege(input) # нафига я её дублирую...
#     elif input=="НАЗАД":
#         InputIs_Messege(input)
#         return True #выйти из цикла
#     elif input=="ВЫХОД":
#         InputIs_Messege(input)
#         Exit() #завершение работы
#     elif is_number(input): #если не подошла ни одна команда, проверим, является ли введённая штука числом
#         InputIs_Messege(input)
#     return False #не выходить из цикла


Menu()  # эта штука должна быть в самом конце, она запускает программу

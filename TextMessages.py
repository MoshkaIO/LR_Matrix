import Controllers


def ViewBorderText(): #типо текстовый разделитель чтобы 999999 текста не сливалось в 1
    print("---------------------------------------------")
    for i in range(10):
        print(" ")
    print("---------------------------------------------")
def MenuMessage(matrix): # текст для главного меню
    print("Главное меню")
    print("Ваша матрица: ")
    PrintMatrix(matrix)
    print("Текущий размер матрицы: "+str(Controllers.MatrixSize)+" на " +str(Controllers.MatrixSize))
    #здесь как-нибудь вывести
    print("Введите РАЗМЕР чтобы указать новый размер матрицы")
    print("Введите ВВОД чтобы ввести матрицу")
    print("Введите ОПР чтобы посчитать определитель матрицы")
    print("Введите СВО чтобы получить информацию о СВОйствах матрицы")#хаха СВО
    print("Введите ДИАГ чтобы получить информацию о главной и побочной диагонали матрицы")
    print("Введите ТРЕУГ привести текущую матрицу к треугольному виду")
    ToExitMessage()
def ToExitMessage():
    print("Введите ВЫХОД чтобы выйти из программы")
def ExitMessage():
    print("Вы вышли из программы")
def ToBackMessage():
    print("Введите НАЗАД чтобы отменить ввод и перейти в предыдущее меню")
def BachMessage():
    print("Вы перешли назад")

def InputIs_Messege(input): #ну да а чё такого
    print("Вы ввели "+str(input))
def ChooseMatrixSizeMessage():
    print("ВНИМАНИЕ! При изменении размера старая матрица будет утрачена!")
    print("*в планах обрезка/дополнение нулями старой матрицы при изменении рамзера*")
    print("Введите размер квадратной матрицы (одно число):")
    ToBackMessage()
    ToExitMessage()
def MatrixInputMessage(matrix,x,y):
    print("Ввод матрицы")
    print("Сейчас твоя матрица выглядит так:")
    PrintChosenElementMatrix(matrix,x,y)
    print("*Редактируемый элемент: "+str(x)+" "+str(y))
    print("Введите новое значение редактируемого элемента чтобы изменить его")
    print("Введите СЛЕД чтобы оставить его неизменным и перейти к следующему")
    print("Введите ПРЕД чтобы оставить его неизменным и перейти к предыдущему")
    print("Введите СОХР чтобы сохранить изменения и перейти в предыдущее меню")
    ToBackMessage()
    ToExitMessage()
#def MatrixInputMessage():
def ShowDeterminantMessage(matrix, det):
    print("Ваша матрица: ")
    PrintMatrix(matrix)
    print(" Её определитель: "+str(det))
    ToBackMessage()
    ToExitMessage()

def ShowSetTriangleMessage(matrix, newMatrix):
    print ("Текущий вид вашей матрицы:")
    PrintMatrix(matrix)
    print("Ваша матрица в треугольном виде: ")
    PrintMatrix(newMatrix)
    print("Чтобы сохранить изменения нажмите ДА ")
    ToBackMessage()
    ToExitMessage()
def InputCommandErrorMessege(wrong_input):
    print("Вы ввели какую-то фигню: \""+str(wrong_input)+"\"")
    print("Пожалуйста, введите команду ещё раз")
def InputNumberErrorMessage(wrong_input): #я не понял в чём их отличие ...
    print("Вы ввели какую-то фигню: \""+str(wrong_input)+"\" вместо числа")
    print("Пожалуйста, введите число/команду ещё раз")

def PrintMatrix(matrix): #отпечатать всю матрицу. Используется почти везде
    #MatrixCheck(matrix)
    MaxInColumn= Controllers.MaxInMatrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if float(matrix[i][j])<0:
                print("  " + TextAlinger(str(matrix[i][j]), len(str(MaxInColumn[j]))) + "  ", end="") #типо минус подвинуть
            else: print("  " + TextAlinger(str(matrix[i][j]), len(str(MaxInColumn[j]))) + "  ", end="")

            #print(str(j)+" ",end="") #надо реализовать определение нужной ширины столбца
        print("")
def PrintChosenElementMatrix(matrix,x,y): # отпечатать матрицу и выделить конкретный элемент
    MaxInColumn = Controllers.MaxInMatrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i==x) and (j==y):
                print(" >" + TextAlinger(str(matrix[i][j]), len(str(MaxInColumn[j]))) + "< ", end="") #выделяем нужный элемент
            else:
                print("  " +TextAlinger(str(matrix[i][j]), len(str(MaxInColumn[j]))) + "  ", end="")
            # print(str(j)+" ",end="") #надо реализовать определение нужной ширины столбца
        print("")

def TextAlinger(text,count_of_ch): #выравниватель 777
    # return text
    if len(text)>=count_of_ch: #если больше то так-то пипец
        if len(text)>count_of_ch:
            T=1
             #print("СЛИШКОМ МАЛО МЕСТА! ГДЕ-ТО СЛУЧИЛАСЬ ОШИБКА")
        return text
    return text+' '*(count_of_ch-len(text)) #оставшееся место добиваем пробелами


def MatrixCheck(matrix): #случилась поломка и пришлось написать эту фигню
    print("---------------")
    print("Отладка. Содержимое матрицы:")
    print(matrix)
    print("---------------")
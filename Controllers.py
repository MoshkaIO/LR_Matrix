import TextMessages
from TextMessages import ViewBorderText, InputCommandErrorMessege, InputNumberErrorMessage, PrintMatrix, MatrixCheck

MatrixSize=3
Matrix=[[1,-2,3],[4,0.77,6],[-777,8,9]]
def CommandController(command_list, input): #этой штуке я назначения пока не придумал
    for i in command_list:
        if input==i:
            return True
    return False
def Input(): #ну а вдруг ещё какой-нибудь будет!!!!!!!!!!!!!!!!!!!!
    return input()

def is_number(s):
    s=s.replace(',','.') #все запятые заменить на точки, иначе подумает что не число
    try:
        float(s)
        print("вроде норм число: "+s)
        return True
    except ValueError:
        print("вроде НЕ норм число")
        return False

def ChangeView():
    ViewBorderText() #типо текстовый разделитель чтобы 999999 текста не сливалось в 1

# def MatrixInput(size):
#     arr = [ [0]*size for i in range(size)]
#     print("Текущая матрица:")
#     PrintMatrix(Matrix)
def CreateNewSquareMatrix(size):
    #newMatrix = [[0] * size for i in range(size)]
    newMatrix=[]
    for i in range(size):
        newLine=[]
        for j in range(size):
            newLine.append('0')
        newMatrix.append(newLine)
    newMatrix2 = [[0 for _ in range(size)] for _ in range(size)]
    return newMatrix2

def MaxInMatrix(matrix):
    #Max=matrix[0][0]
    #MaxInColumn=[len(matrix)]
    MaxInColumn=matrix[0].copy() #ПИДОРАС НАЙДЕН ПИДОРАС НАЙДЕН ПИДОРАС НАЙДЕН ПИДОРАС НАЙДЕН ПИДОРАС НАЙДЕН ПИДОРАС НАЙДЕН
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # if matrix[i][j]>Max:
            #     Max=matrix[i][j]
            if len(str(matrix[i][j]))>len(str(MaxInColumn[j])): #ЧЕЕЕЕЕЕ НАХРЕНА Я ИХ ПО МОДУЛЮ СРАВНИВАЮ!
                MaxInColumn[j]=matrix[i][j]
    return MaxInColumn


def Detarminant(matrix):#matrix[i][0]
    if len(matrix)==1:
        return float(matrix[0][0])
    if len(matrix)==2:
        print("Вы подали матрицу шириной 2")
        det=float(matrix[0][0])*float(matrix[1][1])-float(matrix[0][1])*float(matrix[1][0])
        print(" Её определитель "+ str(det))
        return det
    summ=0
    for i in range(len(matrix[0])): #ну типо первую строку перебираем эээ не пмню зачем
        print(" этот ваш индекс "+str(i))
        print(" элемент в строке 0 с ним: "+str(float(matrix[0][i])))
        summ=summ+((-1)**(1+i+1))*float(matrix[0][i])*Detarminant(CutMatrix(matrix.copy(),0,i))
        print("Промежуточное значение суммы: "+str(summ)+" (множитель):"+str(float(matrix[0][i])))
    return summ

def CutMatrix(matrix1,x,y): #удаляет строку x и стобец y (да, это неправильные координаты >:(  )
    matrix=matrix1.copy() # страховка
    for i in range (len(matrix)):
        matrix[i]=matrix1[i].copy() #гиперстрахование И ЧТО БЫ ВЫ ДУМАЛИ? ИМЕННО ЭТО И ПОЧИНИЛО ПРОГРАММУ!!1!!!!!!!
    print(" Обрезалка матрицы запущена ")
    print(" До удаления строки: ")
    PrintMatrix(matrix)
    matrix.pop(x) #удаляем строку (вроде как)
    print(" После : ")
    PrintMatrix(matrix)
    for i in range (len(matrix)):
        matrix[i].pop(y) #удаляем столбик
    print(" Стобик y был уничтожен :")
    PrintMatrix(matrix)
    return matrix

def SetMatrixTriangle(matrix):
    newMatrix=matrix.copy()
    print("Проверка корректного копирования перед обрезанием:")
    TextMessages.PrintMatrix(newMatrix)
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            newMatrix[i][j]=0
    print("Промежуточный результат:")
    TextMessages.PrintMatrix(newMatrix)
    return newMatrix



# def MenuCommandController(input): #вся идея пошла через жопу из-за циклического импорта
#     if input=="РАЗМЕР":
#         print("вы ввели РАЗМЕР")
#         ChooseMatrixSize()
#     elif input=="ВВОД":
#         print("вы ввели ВВОД")
#         MatrixInput()
#     elif input=="ОПР":
#         print("вы ввели ОПР")
#     elif input=="СВО":
#         print("вы ввели СВО")
#     elif input=="ДИАГ":
#         print("вы ввели ДИАГ")
#     elif input=="НАЗАД":
#         print("вы ввели НАЗАД") #под вопросом для Menu
#     elif input == "ВЫХОД":
#         print("вы ввели ВЫХОД")
#         return False
#     else:
#         InputCommandErrorMessege()
#     return True
#     # elif input=="":
#     #     print("")


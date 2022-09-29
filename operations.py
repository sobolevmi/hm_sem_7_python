import logger

def addition():
    size = str(input("Сколько чисел вы хотите сложить? "))
    while size.isdigit() == False:
        size = input("Необходимо ввести число. Попробуйте снова: ")
        logger.log_message("critical")
    while True:
        if int(size) > 1:
            temp_list = list()
            for i in range(0, int(size)):
                number = str(input("Введите число: "))
                while number.isdigit() == False:
                    number = input("Необходимо ввести число. Попробуйте снова: ")
                    logger.log_message("critical")
                temp_list.append(float(number))
            result = 0
            for item in temp_list:
                result = result + float(item)
            print(f"Введенные числа: {temp_list}\n"
                    f"Результат сложения введенных чисел: {round(result, 5)}")
            break
        elif int(size) <= 1:
            size = str(input("Необходимо ввести число, больше или равное двум. Попробуйте снова: "))
            logger.log_message("warning")
            while size.isdigit() == False:
                size = str(input("Необходимо ввести число. Попробуйте снова: "))
                logger.log_message("critical")

def subtraction():
    size = str(input("Введите количество чисел, участвующих в вычитании: "))
    while size.isdigit() == False:
        size = input("Необходимо ввести число. Попробуйте снова: ")
        logger.log_message("critical")
    while True:
        if int(size) > 1:
            temp_list = list()
            for i in range(0, int(size)):
                number = str(input("Введите число: "))
                while number.isdigit() == False:
                    number = input("Необходимо ввести число. Попробуйте снова: ")
                    logger.log_message("critical")
                temp_list.append(float(number))
            result = temp_list[0]
            for index in range(1, int(size)):
                result = result - temp_list[index]
            print(f"Введенные числа: {temp_list}\n"
                    f"Результат вычитания введенных чисел: {round(result, 5)}")
            break
        elif int(size) <= 1:
            size = str(input("Необходимо ввести число, больше или равное двум. Попробуйте снова: "))
            logger.log_message("warning")
            while size.isdigit() == False:
                size = str("Необходимо ввести число. Попробуйте снова: ")
                logger.log_message("critical")

def mult():
    size = str(input("Сколько чисел вы хотите умножить? "))
    while size.isdigit() == False:
        size = input("Необходимо ввести число. Попробуйте снова: ")
        logger.log_message("critical")
    while True:
        if int(size) > 1:
            temp_list = list()
            for i in range(0, int(size)):
                number = str(input("Введите число: "))
                while number.isdigit() == False:
                    number = input("Необходимо ввести число. Попробуйте снова: ")
                    logger.log_message("critical")
                temp_list.append(float(number))
            result = temp_list[0]
            for index in range(1, int(size)):
                result = result * temp_list[index]
            print(f"Введенные числа: {temp_list}\n"
                    f"Результат умножения введенных чисел: {round(result, 5)}")
            break
        elif int(size) <= 1:
            size = str(input("Необходимо ввести число, больше или равное двум. Попробуйте снова: "))
            logger.log_message("warning")
            while size.isdigit() == False:
                size = str("Необходимо ввести число. Попробуйте снова: ")
                logger.log_message("critical")

def div():
    size = str(input("Сколько чисел вы хотите разделить? "))
    while size.isdigit() == False:
        size = input("Необходимо ввести число. Попробуйте снова: ")
        logger.log_message("critical")
    while True:
        if int(size) > 1:
            temp_list = list()
            for i in range(0, int(size)):
                number = str(input("Введите число: "))
                while number.isdigit() == False:
                    number = input("Необходимо ввести число. Попробуйте снова: ")
                    logger.log_message("critical")
                temp_list.append(float(number))
            result = temp_list[0]
            for index in range(1, int(size)):
                result = result / temp_list[index]
            print(f"Введенные числа: {temp_list}\n"
                    f"Результат деления введенных чисел: {round(result, 5)}")
            break
        elif int(size) <= 1:
            size = str(input("Необходимо ввести число, больше или равное двум. Попробуйте снова: "))
            logger.log_message("warning")
            while size.isdigit() == False:
                size = str("Необходимо ввести число. Попробуйте снова: ")
                logger.log_message("critical")
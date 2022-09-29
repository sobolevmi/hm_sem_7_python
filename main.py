import operations
import logger

choice_menu = " "
while choice_menu != "q":
    choice_menu = str(input("Калькулятор\n"
                        "Если вы хотите выполнить сложение, нажмите '+'\n"
                        "Если вы хотите выполнить вычитание, нажмите '-'\n"
                        "Если вы хотите выполнить умножение, нажмите '*'\n"
                        "Если вы хотите выполнить деление, нажмите '/'\n"
                        "Если вы просмотреть журнал логов, нажмите 'v'\n"
                        "Если вы хотите выйти из программы, нажмите 'q'\n"))
    with open("log_magazine.txt", "a"):
        if choice_menu == "+":
            operations.addition()
            logger.log_time()
            print(choice_menu)
        elif choice_menu == "-":
            operations.subtraction()
            logger.log_time()
            print(choice_menu)
        elif choice_menu == "*":
            operations.mult()
            logger.log_time()
            print(choice_menu)
        elif choice_menu == "/":
            operations.div()
            logger.log_time()
        elif choice_menu == "v":
            logger.log_view()
        elif choice_menu == "q":
            break
        else:
            print("Вы ввели неверный символ. Попробуйте снова")
            print(choice_menu)
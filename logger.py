from datetime import datetime

def log_time():
    with open("log_magazine.txt", "a", encoding="utf8") as file:
        operation_time = datetime.now()
        file.write("Время выполнения операции: " + str(operation_time) + "\n")

def log_message(message):
    with open("log_magazine.txt", "a", encoding="utf8") as file:
        operation_time = datetime.now()
        if message == "warning":
            file.write(f"WARNING: пользователь ввел число, выходящее за пределы диапазона\n")
        if message == "critical":
            file.write(f"CRITICAL: пользователем введено не число\n")

def log_view():
    with open("log_magazine.txt", "r", encoding="utf8") as file:
        for line in file:
            print(line)
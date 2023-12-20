import random
import matplotlib.pyplot as plt
RUS_ALPHABET= "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def generation(length):
    password = ""
    for i in range(length): password += random.choice(RUS_ALPHABET)
    return password

def distribution_visualization(password):
    char_dict = dict.fromkeys(password, 0)
    for character in password:
        char_dict[character] += 1
    visualizer = ""
    for character in char_dict:
        periodicity = char_dict[character]
        visualizer += character + " " + ("_" * periodicity) + "\n"
    print(visualizer)

def average_time_by_length(length):
    return pow(len(RUS_ALPHABET), length) / 2000000.0

def plotting(n):
    fig, ax = plt.subplots()
    plt.title("Зависимость времени взлома пароля от его длины при скорости подбора 2 000 000 п/с", fontsize=9)
    ax.set_ylabel("Время взлома, c")
    ax. set_xlabel("Длина пароля")
    x = [i for i in range(n+1)]
    y = [average_time_by_length(j) for j in x]
    ax.scatter(x,y, c= 'red', )
    ax.grid()
    plt.show()

def main():
    pass_len = int(input("Введите длину пароля: "))
    password = generation(pass_len)
    print("Сгенерированный пароль: ", password)
    distribution_visualization(password)
    print("При скорости подбора 2 000 000 п/с: ", average_time_by_length(pass_len), "с")
    plotting(int(input("График зависимости скорости подбора пароля, длина которого находится в пределах от 0 до n символов. \nВведите n: ")))

main()
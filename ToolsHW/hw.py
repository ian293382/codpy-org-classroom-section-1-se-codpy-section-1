import sys
import webbrowser

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def input_math():
    global B1, ERROR_COUNT, UndefinedVar
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == "1":
                opEn_vIdeo()
                break
            elif user_input.lower() == "exit":
                print("let me out! now!!")
                break
            else:
                print("Wrong! Try again.")

    except Exception as e:
        print(f"Error: {e}")


def opEn_vIdeo():
    webbrowser.open(X1)
    print("Rickroll incoming...")


if __name__ == "__main__":
    input_math()

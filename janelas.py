import pygetwindow as gw
import pyautogui
import pyperclip
import time

# for w in gw.getWindowsWithTitle(''):
#     print(w.title)

if __name__ == "__main__":
    ldb = ':: NEW LDB ::'
    try:
        newjanela = gw.getWindowsWithTitle(ldb)[0]
        newjanela.restore()
        time.sleep(0.1)
        newjanela.activate()
        time.sleep(0.1)
        print("ldb aberto")
    except IndexError:        
        print("❌ Janela do CPlus ou LDB não encontrada.")

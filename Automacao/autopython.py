import pyautogui, time
import pandas as pd

time.sleep(5)
pyautogui.click(x=141, y=1068)
time.sleep(2)
pyautogui.write('chrome')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://lista-de-produtos-pdf.vercel.app/')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('tab')
tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    # time.sleep(2)
    pyautogui.write(str(tabela.loc[linha, "nome"]))
    pyautogui.press('tab')
    # time.sleep(2)
    pyautogui.write(str(tabela.loc[linha, "preco"]))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.click(x=538, y=215)

pyautogui.scroll(-600)
pyautogui.click(x=496, y=1011)
time.sleep(2)
pyautogui.press('enter')
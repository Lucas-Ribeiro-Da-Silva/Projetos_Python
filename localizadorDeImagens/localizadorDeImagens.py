import pyautogui
import time

"""
Obrigatório a instalação das seguintes bibliotecas
pip install pyautogui
pip install PyScreeze
pip install opencv-python
pip install Pillow
"""

"""
Este código recebe um print de exemplo
e busca na sua tela uma imagem parecida
ao encontrar na sua tela, realiza as ações programadas.
"""
while True:
    try:
        #a linha a seguir usa a url de referência para fazer a comparação
        #ou seja, sua url deve ser um print de exemplo da imagem desejada
        #o confidence é um ajuste que permite pequenas diferenças entre ex e o real
        img = pyautogui.locateCenterOnScreen('caminho_completo_aqui', confidence=0.7)
        time.sleep(1)
        #nas linhas a seguir pode-se realizar a ação desejada
        #como exemplo, clicamos na imagem e dizemos "achei"
        pyautogui.click(img.x, img.y)
        time.sleep(1)
        print("achei")
    except:
        time.sleep(1)
        print("Não encontrei")
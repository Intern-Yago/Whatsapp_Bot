import pywhatkit, keyboard, time
from datetime import datetime

contatos["+<DDI><DDD><NUMBER>"]#Coloque as respectivas informações aqui                                                                                             
while len(contatos) >= 1:                                                                                                                                           
    pywhatkit.sendwhatmsg(teste[0], 'Começando os estudos de GIT', datetime.now().hour, datetime.now().second + 2)                                 
    del contatos[0]
    time.sleep(25)
    keyboard.press_and_release('ctrl + w')

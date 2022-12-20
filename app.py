import time
from playsound import playsound

def cont_regressiva(t):
    print("Contagem regressiva:\r")
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        playsound("bip.mp3")
        print(timer, end="\r")
        time.sleep(0.65)
        t -= 1        

    print('Fim do tempo!')
    playsound("bip_final.mp3")    

t = input('Digite o tempo desejado(em segundos): ')

cont_regressiva(int(t))
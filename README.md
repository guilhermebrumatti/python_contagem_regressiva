# Contagem Regressiva com Python

Esta aplicação pede ao usuário, que digite o tempo desejado(em segundos).<br>
Após digitado e confirmado com ENTER, a contagem regressiva começa.

Um bip é emitido a cada segundo e um bip final é emitido quando a contagem
se encerra.

<b>*Obs: O correto seria definir o time.sleep() com 1, porém, por conta do 
delay gerado pela execução do bip.mp3, precisei ajustar o sleep para <u>0.65</u><b>

Necessário:<br>
- pip install playsound

# pitcher.py
Este programa recebe input audio através de um microfone e processa-o para indicar a altura do som, ou seja, que nota musical representa.

![Exemplo com flauta](https://github.com/guizado/pitcher.py/blob/main/media/flauta.gif?raw=true)

## Como funciona?
Utilizando a biblioteca pyaudio, o input sonoro é transformado em sinais de tempo discreto. Ao aplicarmos o algoritmo FFT a estes dados obtem-se o espetro sonoro, e com este, a frequência fundamental. Pyaudio faz com que o input seja contínuo e não em blocos, por isso o cálculo da nota musical é realizado em tempo real.
A interface do programa é feita em Tkinter.

![Plot](https://github.com/guizado/pitcher.py/blob/main/media/plot.png?raw=true)

## Limitações
###### Microfone
A eficácia depende do microfone utilizado. Para os exemplos dados, usei o microfone do meu portátil. Dado a má qualidade do mesmo, as notas nas oitavas mais baixas são muito difíceis de detetar, visto que as suas frequências correspondentes encontram-se muito próximas, logo o menor desvio de frequência gera resultados errados. Sendo que nas oitavas mais altas as notas têm frequências fundamentais distantes uma das outras, a sua deteção tem mais acurácia. [Comparação entre baixas e altas frequências fundamentais.](https://github.com/guizado/pitcher.py/blob/main/media/comparacao.png?raw=true)
###### Sons complexos
Tendo em conta que o input é contínuo e em tempo real, sons complexos geram resultados variados. A eficácia do programa encontra-se em reconhecer sons mais simples como ondas harmónicas.
###### Ruído
Sabendo que o programa está feito para sons simples, é óbvio que ruído de background influencia os resultados negativamente. 

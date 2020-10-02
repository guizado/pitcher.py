# pitcher.py
Este programa recebe input audio através de um microfone e processa-o para indicar a altura do som, ou seja, que nota musical representa.

[GIF DO ECRÃ A USAR O PROGRAMA]
[VIDEO/GIF DE EU A TOCAR FLAUTA COM O PROGRAMA LIGADO]

## Como funciona?
Utilizando a biblioteca pyaudio, o input sonoro é transformado em sinais de tempo discreto. Ao aplicarmos o algoritmo FFT a estes dados conseguimos obter o espetro sonoro, e com este, a frequência fundamental. Pyaudio faz com que o input seja contínuo e não em blocos, por isso o cálculo da nota musical é realizado em tempo real. A interface do programa é feita com o Tkinter.
![plot](https://github.com/guizado/pitcher.py/blob/main/media/plot.png?raw=true)

## Limitações
###### Microfone
A eficácia depende do microfone utilizado. Para os exemplos dados, usei o microfone do meu portátil. Dado a má qualidade do mesmo, as notas nas oitavas mais baixas são muito dificéis de detectar, visto que as suas [frequências conrespondentes encontram-se muito próximas](https://github.com/guizado/pitcher.py/blob/main/media/lowfreqs.png?raw=true), logo o menor desvio de frequência lida a resultados errados. Sendo que nas oitavas mais altas as notas têm frequências fundamentais distantes uma das outras, a sua detecção tem mais acurácia. 
[TABELA DE FREQUÊNCIAS]
###### Sons complexos
Tendo em conta que o input é contínuo e em tempo real, sons complexos geram resultados variados. A eficácia do programa encontra-se em detetar sons mais simples como ondas harmónicas.
###### Ruído
Sabendo que o programa está feito para sons simples, é óbvio que ruído de background influencia os resultados negativamente. Também de notar que em sons com muita reverberação, o programa consegue identificar a altura do mesmo, mas devido à reverberação, os resultados desviam-se do pretendido. É de notar que estes desvios apresentavam propriedades musicas constantes, por exemplo, serem sempre o mesmo intervalo musical a partir da nota original.

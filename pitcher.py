import pyaudio
import time
from pitcher_aux import *
import tkinter as tk
from tkinter.font import Font


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
DELTA_TIME = 0.1
P = pyaudio.PyAudio()
stream = 0


# GUI Setup
rt = tk.Tk()
rt.title('Pitcher')
rt.iconbitmap('icon.ico')
rt.geometry('300x200')


def on_click():
    ''' Chamado quando o botão que controla a Stream é clicado '''
    global b
    global l
    global stream
    if b['text'] == 'Start':
        # Stream setup
        stream = P.open(format=FORMAT, 
                channels=CHANNELS, 
                rate=RATE, 
                input=True, 
                frames_per_buffer=CHUNK,
                stream_callback=callback)
        b['text'] = 'Pause'
    elif b['text'] == 'Pause':
        stream.stop_stream()
        l['text'] = '...'
        b['text'] = 'Resume'
    else:
        stream.start_stream()
        b['text'] = 'Pause'


# Butão que controla a stream
b = tk.Button(rt, text='Start', height=2, width=8, bd=4, command=on_click)
b.place(relx=0.5, rely=0.7, anchor='center')
# Label da nota
l = tk.Label(rt, text='Pitcher.py', font=Font(family="Lucida Grande", size=40))
l.place(relx=0.5, rely=0.3, anchor='center')


def process_in_data(in_data):
    ''' Processar dados sonoros para obter frequência, amplitude e nota musical '''
    signal = np.fromstring(in_data, "Int16")
    freqs, fft = signalfft(signal, RATE)
    f, amp = dom_freq(freqs, fft)
    nota = freq2note(f, amp)
    return nota, f, amp


def callback(in_data, frame_count, time_info, status):
    ''' 
    Streaming será feito em callback mode, 
    necessitando de uma função destas que é repetidamente chamada
    '''
    global l
    nota, f, amp = process_in_data(in_data)
    l['text'] = nota
    time.sleep(DELTA_TIME)
    return in_data, pyaudio.paContinue


rt.mainloop()


# Término
if stream:
    stream.close()
P.terminate()



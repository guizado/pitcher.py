import numpy as np
import scipy
import scipy.fftpack as fftpk


RATE = 44100
AMPLITUDE_MINIMA = 0.5 * (10**6)


# Notas musicais e as suas conrespondentes frequências em Hz
musical_freqs = {
    (0,253.9):{'C3':130.81, 'D3':146.83, 'E3':164.81, 'F3':174.61, 'G3':196.00, 'A3':220.00, 'B3':246.94},
    (254.0,508.9):{'C4':261.63, 'D4':293.66, 'E4':329.63, 'F4':349.23, 'G4':392.00, 'A4':440.00, 'B4':493.88},
    (509.0,1016.9):{'C5':523.25, 'D5':587.33, 'E5':659.25, 'F5':698.46, 'G5':783.99, 'A5':880.00, 'B5':987.77},
    (1017,2034.9):{'C6':1046.50, 'D6':1174.66, 'E6':1318.51, 'F6':1396.91, 'G6':1567.98, 'A6':1760.00, 'B6':1975.53},
    (2035,9999.9):{'C7':2093.00, 'D7':2349.32, 'E7':2637.02, 'F7':2793.83, 'G7':3135.96, 'A7':3520.00, 'B7':3951.07}
    }


def signalfft(signal, sampling_rate):
    ''' Aplica o FFT ao sinal sonoro '''

    fft = np.abs(scipy.fft(signal))
    freqs = fftpk.fftfreq(len(fft), (1.0/sampling_rate))
    half = len(fft)//2
    return freqs[:half], fft[:half]



def dom_freq(freqs, fft):
    ''' Devolve a frequência predominante, no fundo, a nota do som '''

    z = zip(freqs, fft)
    max = 0
    freq_res = 0
    for a, b in z:
        if a > 8000:
            break
        if b > max:
            max = b
            freq_res = a
    return freq_res, max


def freq2note(freq, amp):
    ''' 
    Recebe uma frequência e devolve uma string conrespondente à nota mais próxima,
    segundo o dicionário musical_freqs
    '''

    dif = -1
    nota = '--'
    if amp < AMPLITUDE_MINIMA:
        return '--'
    for intervalo, oitava in musical_freqs.items():
        if intervalo[0] < freq < intervalo[1]:
            for n, f in oitava.items():
                d = abs(freq - f)
                if d < dif or dif == -1:
                    dif = d
                    nota = n
            break
    return nota


def process_in_data(in_data):
    ''' Processar dados sonoros para obter frequência, amplitude e nota musical '''
    signal = np.fromstring(in_data, "Int16")
    freqs, fft = signalfft(signal, RATE)
    f, amp = dom_freq(freqs, fft)
    nota = freq2note(f, amp)
    return nota, f, amp


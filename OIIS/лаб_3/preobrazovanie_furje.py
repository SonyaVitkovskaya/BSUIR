import numpy as np
import math
import matplotlib.pyplot as plt


def DFT_slow(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def FFT(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:int(N/2)] * X_odd,
                               X_even + factor[int(N/2):] * X_odd])


def iFFT(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    x = np.conjugate(x)
    x = FFT(x)
    x = np.conjugate(x)

    x /= N

    return x


def genSine(f0, fs, dur):
    t = np.arange(dur)
    wave = np.sin(2*np.pi*t*(f0/fs))
    wave = normalise(wave)
    return wave


def getCosine(f0, fs, dur):
    t = np.arange(dur)
    wave = np.cos(2*np.pi*t*(f0/fs))
    wave = normalise(wave)
    return wave


def normalise(x, MAX_INT16=32767):
    maxamp = max(x)
    amp = math.floor(MAX_INT16/maxamp)
    norm = np.zeros(len(x))
    for i in range(len(x)):
        norm[i] = amp*x[i]
    return norm


if __name__ == '__main__':
    f0 = 440
    fs = 16000
    dur = 2**10

    sine = genSine(f0, fs, dur)
    cosine = getCosine(f0, fs, dur)

    plt.plot(np.arange(dur), sine, cosine)
    plt.title('Plot of sin and cos')
    plt.xlabel('x values from 0 to {}'.format(dur))
    plt.ylabel('sin(x) and cos(x)')
    plt.legend(['sin(x)', 'cos(x)'])  
    plt.show()

    plt.plot(np.arange(dur), np.abs(FFT(sine)), np.abs(FFT(cosine)))
    plt.title('Double Sided FFT')
    plt.xlabel('x values from 0 to {}'.format(dur))
    plt.ylabel('DFT values')
    plt.legend(['FFT(sine)', 'FFT(cosine)'])  
    plt.show()


from scipy.signal import cheby1, cheb1ord
from math import pi, log10

BW=4000
Fs=10*BW
nbits=12
Rp=0.3

Wp=2*pi*BW
Ws=2*pi*(Fs-BW)
Rs=nbits*20*log10(2)

(N,wn)=cheb1ord(Wp, Ws, Rp, Rs, analog=True)
sos_proto=cheby1(N,Rp,1,analog=True,output='sos')

print("{0}-th order Chebyshev Type I".format(N))
print(sos_proto)

from scipy.signal import cheby1, cheb1ord
from math import pi, log10


def antialias_proto(bw,fs,nbits,rp):

  Wp=2*pi*bw
  Ws=2*pi*(fs-bw)
  Rs=nbits*20*log10(2)

  (N,wn)=cheb1ord(Wp, Ws, rp, Rs, analog=True)
  sos_proto=cheby1(N,rp,1,analog=True,output='sos')
  return (N,wn,sos_proto)


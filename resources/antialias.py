from antialias_proto import antialias_proto

if __name__=='__main__':

  BW=4000
  Fs=10*BW
  nbits=12
  Rp=0.3
  (N,sos_proto)=antialias_proto(BW,Fs,nbits,Rp)

  print("{0}-th order Chebyshev Type I".format(N))
  print(sos_proto)

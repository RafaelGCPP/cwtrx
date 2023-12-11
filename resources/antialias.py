from antialias_proto import antialias_proto
from numpy import pi, sqrt

#if __name__=='__main__':

BW=4000
Fs=40000
nbits=12
Rp=0.3
(N,wn,sos_proto)=antialias_proto(BW,Fs,nbits,Rp)

print("{0}-th order Chebyshev Type I".format(N))


for f in sos_proto: # All sections are LP...

    den=f[3:6]
    num=f[0:3]

    cBase=47e-9

    if den[0]==0: # first order
        w0=den[2]*wn
        C=cBase
        R=1/(w0*C)
        print("  First order RC at {:.3f} Hz:".format(w0/(2*pi)))
        print("    R={:.2e} ohm".format(R))
        print("    C={:.2e} farad".format(C))
    
    else: 
        # second order -> Sallen-Key EPF case B (eq 5-74b of Schaumann, Ghausi and Laker)
        # eta=beta4=0
        

        w0=sqrt(den[2])
        Q=den[2]/den[1]
        w0=w0*wn
        gain=num[2] 
        
        #minimize 3g - sqrt(g)/Q - 2 =0
        Q2=Q**2
        g = (sqrt(24*Q2 + 1)/Q2 + 1/Q2 + 12)/18 # R2=R3/g

        K=g+2-(sqrt(g)/Q) # This is the optimal K, such that sensitivity is minimized
        
        # There is a catch: if K is less than 1, the circuit is not realizable
        # (negative resistor values). In this case, we have to set it to 1 and evaluate
        # g and beta2 accordingly, based on Q.

        if K<1:
            K=1
            g = (2 * Q2 + sqrt(4 * Q2 + 1) + 1)/(2 * Q2)
            

        beta2=gain/K # we can adjust the overall gain by changing beta2

        C1=cBase
        C4=cBase
        R3=sqrt(g)/(w0*cBase)
        R2=R3/g
        Rg=1000
        Rf=Rg*(K-1)

        print("  Sallen-Key EPF at {:.3f} Hz, Q={:.3f}:".format(w0/(2*pi), Q))
        print("    K=    {:15.4f}".format(K))
        print("    beta2={:15.4f}".format(beta2))
        print("    g=    {:15.4f}".format(g))
        print("    C1=   {:15.4e} farad".format(C1))
        if beta2!=1:
            print("    R2a=  {:15.4e} ohm".format(R2/beta2))
            print("    R2b=  {:15.4e} ohm".format(R2/(1-beta2)))
        else:
            print("    R2=   {:15.4e} ohm".format(R2))
        print("    R3=   {:15.4e} ohm".format(R3))
        print("    C4=   {:15.4e} farad".format(C4))
        if K!=1:
            print("    Rg=   {:15.4e} ohm".format(Rg))
        print("    Rf=   {:15.4e} ohm".format(Rf))
        


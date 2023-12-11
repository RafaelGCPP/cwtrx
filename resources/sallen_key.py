

class SallenKeyCascade:
    def __init__(self,sos,wn):
        self.cascade=[]
        for f in sos:
            if f[3]==0:
                self.cascade.append(SallenKeySection(f[0:2],f[3:5],wn))

class SallenKeySection:
    def __init__(self,num,den,wn):
        self.num=num
        self.den=den
        self.wn=wn

        #TODO check for zeros in numerator and choose filter type

        if num[0]==0:  # either a1 s+ a0 or a0
            if num[1]==0: # a0
                pass
            else:
                pass
        elif num[1]==0: # either a2 s^2 + a0 or a2 s^2
            if num[2]==0: # a2 s^2
                pass
            else:
                pass
        else: # general case a2 s^2 + a1 s + a0
            pass
            
        
        #TODO check filter order (denominator)   

        



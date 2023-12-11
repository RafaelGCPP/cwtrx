

class SallenKeyCascade:
    """
    Given the SOS (second-order section) output of an analog filter prototype design
    by scipy.signal, creates a cascade of Sallen and Key biquads.
    """
    def __init__(self,sos,wn):
        self.cascade=[]
        for f in sos:
            if f[3]==0:
                self.cascade.append(SallenKeySection(f[0:2],f[3:5],wn))

class SallenKeySection:
    """
    Parent class of the many different SK filters.
    On the constructor, it chooses the best configuration based
    on the filter type, poles and zeros.
    """
    def __init__(self,num,den,wn):
        self.num=num
        self.den=den
        self.wn=wn

        #TODO check for zeros in numerator and choose filter type

        
        if den[0]==0: # first order
            #TODO implement first order filter
            if num[1]==0: #LP
                pass
            elif num[0]==0: #HP
                pass
            else:
                raise "First order section not realizable with RC"

            

        # second order
        if num[0]==0:  # either a1 s+ a0 or a0
            if num[1]==0: # a0
                #TODO implement all pole low pass
                # EPF LP 
                pass
                return
            else:
                pass
        elif num[1]==0: # either a2 s^2 + a0 or a2 s^2
            if num[2]==0: # a2 s^2
                #TODO implement high pass (zeros at the origin)
                pass
            else:
                pass
        else: # general case a2 s^2 + a1 s + a0
            pass

        raise "Not implemented yet" #TODO implement remaining cases
            




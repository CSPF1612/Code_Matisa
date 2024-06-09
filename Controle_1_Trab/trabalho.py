from system import System
import control as ct

s=ct.tf('s')
num=4*(s*s+s+9.25)
den=s*(s+4)*(s+1.5)
ftma=num/den
sys=System(FTMA=ftma)

sys.letraA()
sys.letraB()
sys.letraC()
sys.letraD()
sys.letraE()
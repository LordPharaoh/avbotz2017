v=int(float(open("coins.in", "r").readline().strip())*100)
q=v%25
open("coins.out","w").write(str((v//25)+(q//10)+((q%10)//5)+v%5))

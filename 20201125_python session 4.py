

def operation_noob (p, l):
    "test operation dasar"
    print("hasil perkalian:", p * l)
    print("hasil pembagian:",p/l)
    print("hasil penambahan:",p+l)
   ## return;
    print("hasil pengurangan:",p-l)
    
##operation_noob(5,4)


def printme(str):
    "prints string me to this function"
    print(str)
    
##printme("Giri smol guy")

def printinfo(age=24,name="msblablvuye"):
    print('nama:',name)
   
    print('umur:', age)
##printinfo()
##printinfo('Giri',28)


##VARIABLE-LENGTH ARGUMENTS

def varArg(param1, *param2):
    "variable length params"
    print('output adalah:')
    print(param1)
    for var in param2:
        print(var)
    return
##varArg(4,2,4)


##ANONYMOUS FUNCTION
def sum11(arg1,arg2):
    "test return"
    ##total= arg1*arg2
    total1= arg1 + arg2
    total2= total1 + arg2
   ## print('ini totalnya',total1)
    return total2
    
total =sum11(10,20) 
##print('totalnya adalah:', total)


import mod
import pkg.mod1, pkg.mod2
print('test mod cuy',mod.a)
##print(pkg.mod1())
print('hello world')

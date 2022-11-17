import sys
sys.path.append("/")

# import PythonBasic.Chapter06.myCalcPackage.calcModule
from PythonBasic.Chapter06.myCalcPackage.calcModule import *

if __name__ == "__main__" :
    x = 10
    y = 5
    print(f"x = 10; y = 5 일때")
    print(f"Add= {Add(x,y)}")
    print(f"Sub= {Sub(x,y)}")
    print(f"Mul= {Mul(x,y)}")
    print(f"Div= {Div(x,y)}")

    # add = PythonBasic.Chapter06.myCalcPackage.calcModule.Add(x,y)
    # print(f"Add= {add}")
    # sub = PythonBasic.Chapter06.myCalcPackage.calcModule.Sub(x,y)
    # print(f"Add= {sub}")
    # mul = PythonBasic.Chapter06.myCalcPackage.calcModule.Mul(x,y)
    # print(f"Add= {mul}")
    # div = PythonBasic.Chapter06.myCalcPackage.calcModule.Div(x,y)
    # print(f"Add= {div}")

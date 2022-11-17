import sys
sys.path.append("D:/Pywork/NewDataScience/pkg_test")

from game.sound import echo
def print_hello():
    print("hello")

#컨트롤러 혹은 드라이버 역할
if __name__ == "__main__":
    print_hello()
    echo.echo_test()

# sys 모듈을 현재 이름 공간으로 읽어들인다.
import sys

# datetime모듈에서 date 클래스를 읽어들인다.
from datetime import date

print(sys.argv)

print(date.today())


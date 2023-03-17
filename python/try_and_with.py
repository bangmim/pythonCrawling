#예외처리

d={'a':1, 'b':2}
try:
    print(d['a'])
except KeyError:
    #try절 내부에서 except 절에 작성된 예외(현재 KeyError)가 발생하면 except절이 실행된다.
    print('x is not found')

# open()함수
# open() 함수의 반환값은 변수 f에 할당되며 with 블록 내부에서 사용한다.
# 이렇게 사용하면 블록을 벗어날 때 f.close()가 자동으로 호출된다.
with open ('index.html') as f:  
    print(f.read())
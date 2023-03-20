# vsCode 터미널로 출력 (우측 상단에 실행 단추를 눌러 실행한다.)

for x in [1,2,3]:
    print(x)

# 횟수를 지정하여 반복 >> range
for i in range(10):
    print(i)

#for 구문으로 dict를 지정하면 키를 기반으로 순회한다.
d={'a':1, 'b':2}
for key in d:
    value=d[key]
    print(key, value)

#dict의 items()메서드로 dict 키와 값을 순회한다.
for key, value in d.items():
    print(key,value)
    
#while 구분으로 식이 참일 때 반복 처리
s=1;
while s<1000:
    print(s)
    s=s*2
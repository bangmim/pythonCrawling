'''
eng_dict={
    'sun' : '태양',
    'moon' : '달',
    'star' : '별',
    'space' : '우주',
}

for word in eng_dict:
    print('{}의 뜻:{}'.format(word, eng_dict.get(word)))
    
print('p.129---------------------------------------------------');

#(1) range (초기, 종료, 증감값)
for n in range(5,0,-1):
    print(n)

#(2) 출력 변수를 미리 선언한다.
sum=0
num=int(input('임의의 양수를 입력하세요>>>>')) ;    #int로 형변환
for n in range(0,num+1):
    sum+=n

print('1부터 {}사이 모든 정수의 합계는 {}입니다'.format(n, sum))

#(3) 
count= int(input('몇 개의 과일을 보관할까요?>>>'))
fruits=[];

for n in range(0, count):
    fruit=input('{}번째 과일을 입력하세요>>>'.format(n+1))
    fruits.append(fruit)

print('입력받은 과일들은 {}입니다'.format(fruits))


# (4) 100점을 받은 학생의 점수를 제외한 나머지 학생들의 점수를 5점씩 증가시킨 'score' 리스트를 생성하고 출력하는 프로그램 구현. 단, 증가된 점수가 100을 초과하지 않음
exam=[99,98,81,85,54,100,71,50]

score=[min (n + 5,100) for n in exam]   # min(a,b) 인수 중 가장 작은 값을 찾는다.
print(score)
'''

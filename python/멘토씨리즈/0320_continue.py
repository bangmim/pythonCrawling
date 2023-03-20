''' # (1)
fruits=['사과','감귤']
count=3

while count>0:
    fruit = input('어떤 과일을 저장할까요?>>>')
    if fruit in fruits:
        print('동일한 과일이 있습니다')
        continue
    fruits.append(fruit)
    count-=1
    print('입력이 {}번 남았습니다'.format(count))

print('5개 과일은 {}입니다'.format(fruits))
''' # (2)

count =0
total=0
while count<5:
    n=int(input('{}번째 정수를 입력하세요>>>'.format(count+1)))
    if n<=0:
        print('0 이하의 정수는 처리할 수 없습니다')
        continue
    total += n
    count +=1
    
print('입력된 5개 양수의 총 합은 {}입니다'.format(total))
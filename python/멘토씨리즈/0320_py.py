print('재미있는','파이썬')
print('Python','Java','C', sep='/')

print()

fos=open('smaple.py',mode=
         'wt')
print('print("Hello World~!!")',file=fos)      #print("Hello World")가 작성된 sample.py 파일이 생성된다
fos.close()
class Rect:
    def _init_(self, width, height):
        self.width=width    
        self.height=height
    
    # 사각형의 넓이를 계산하는 메서드
    def area(self):
        return self.width*self.height;

# TypeError: Rect() takes no arguments
r= Rect(100,20)
print(r.width, r.height,r.area())   #100 20 200이 출력되야하는데 안나온다..

# Rect를 상속받아 Square 클래스를 정의한다
class Square(Rect):
    def _init_(self, width):
    #   부모 클래스의 메서드를 호출
      super()._int_(width,width)
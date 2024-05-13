class Mobile:
      def __init__(self,os):
            self.os=os
class Brand:
      def __init__(self,name):
            self.name=name
class Battery(Mobile,Brand):
      def __init__(self,os,name):
            self.os = os
            self.name=name
c=Battery("linux","Samsung")
print(c.os)
print(c.name)
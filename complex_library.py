class complex:
  def __init__(self,real,imaginery):
    self.real = real
    self.imaginery = imaginery

  def reportNum(self):
    if self.imaginery<0:
      print(str(self.real)+str(self.imaginery)+"i")
    else:
      print(str(self.real)+"+"+str(self.imaginery)+"i")
  def add(self,c):
    self.real+= c.real
    self.imaginery += c.imaginery
  def subtract(self,c):
    self.real-= c.real
    self.imaginery -= c.imaginery
  def multiply(self,c):
    zR = self.real*c.real - self.imaginery*c.imaginery
    zI = self.real*c.imaginery + self.imaginery*c.real
    self.imaginery = zI
    self.real = zR
  def mag(self):
    return math.sqrt((self.real**2)+(self.imaginery**2))
  def conjugate(self):
    return complex(self.real,-self.imaginery)
  def divide(self,c):
    self.multiply(c.conjugate())
    deno = c.mag()**2
    self.real /= deno
    self.imaginery /= deno

class evaluate :
    def __init__(self , equation):
        self.prob=equation
        self.eq = self.prob.split('=')
        self.multiply()
        self.divide()
        self.addd()
        self.minus()
        self.equal()
        self.evall_str()
        self.evall()
    def is_number(self,var):
        try:
           if var == int(var):
               return True
        except Exception:
            return False
    def multiply(self):
        mult = self.eq[0].split('*')
        z =mult[0]
        return z
    def addd(self):
        add = self.eq[0].split('+')
        z =add[0]
        if self.is_number(z) == True:
            return z
        else:
            try:
                z= (add[1])
                return z
            except:
                return ''
    def minus(self):
        minus = self.eq[0].split('-')
        z = minus[0]
        if self.is_number(z) == True:
            return z
        else:
            try:
                z= minus[1]
                return z
            except:
                return ''
    def divide(self):
        divides = self.eq[0].split('/')
        z = divides[0]
        if self.is_number(z) == True:
            return z
        else:
            try:
                z= (divides[1])
                return z
            except:
                return ''
    def equal(self):
        equal = self.prob.split('=')
        z =(equal[0])
        if self.is_number(z) == True:
            return z
        else:
            try:
                z= (equal[1])
                return z
            except:
                return ''
    def evall_str(self):
        listt = []
        if self.addd()!='':
            listt.append("-"+self.addd()+')')
        else:
            listt.append(" ")
        if self.minus()!='':
            listt.append("+"+self.minus()+')')
        else:
            listt.append(" ")
        if self.multiply()!='':
            listt.append("/"+self.multiply())
        else:
            listt.append(" ")
        if self.divide()!='':
            listt.append("*"+self.divide())
        else:
            listt.append(" ")
        return listt
    def evall(self):
        y = "" + self.equal() + self.addd()+self.minus()+self.divide() +self.multiply() + ""
        solved = '('+self.eq[1] + self.evall_str()[0] + self.evall_str()[1] + self.evall_str()[2] + self.evall_str()[3]
        o = eval(solved)
        print('x = '+str(o))
x = evaluate(input('enter an equation in the form y*x+z=o: '))

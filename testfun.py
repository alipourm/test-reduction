
class F:
    def foo(self, c):
        print(c)

    funname = None
    funargs = None

    def bar(self):
        self.funname = self.foo
        self.funargs = 100

    def zee(self):
        self.funname(self.funargs)

if __name__ == '__main__':
    f = F()
    f.bar()
    f.zee()

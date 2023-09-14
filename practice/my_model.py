__all__ = ['test_A'] #通过*导入时，只有all变量列表里的函数可以使用

def test_A(a,b):
    return a+b

def test_B(a,b):
    return a-b

#导入的时候，以下的代码不运行
if __name__ == '__main__':
    test_A(1,2)
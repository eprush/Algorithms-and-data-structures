class Singleton:
    instance = None

    def __new__(cls, x: int):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, x: int):
        self.data = x
        return

    def do_work(self):
        """do something hard"""
        self.data = 101
        return


if __name__ == "__main__":
    s = Singleton(10)
    print(s.data)
    s.do_work()
    print(s.data)

    another_s = Singleton(1)
    print(another_s is s)

class MyClass:
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self):
        return f"{self.message}"

a = MyClass("This is my test")

class CustomError(Exception):
    pass

print(a)

try:
    raise CustomError()
except CustomError as e:
    print(e)
# Trying to use 'e' out here raises a NameError!
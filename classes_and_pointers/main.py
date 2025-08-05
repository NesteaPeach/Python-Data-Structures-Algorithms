class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color
        

cookie = Cookie('blue')
print(cookie.get_color())  # Output: blue

cookie.set_color('red')
print(cookie.get_color())  # Output: red


num1 = 10
num2 = num1
print(id(num1), id(num2))  # Same ID

num2 = 22
print(id(num1), id(num2))  # Different IDs


dict1 = {"value": 1}
dict2 = dict1
dict2["value"] = 22

print(dict1["value"])  # Output: 22 – both point to the same dictionary

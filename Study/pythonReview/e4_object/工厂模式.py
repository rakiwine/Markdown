#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/27
# file: 工厂模式.py
# Email:
# Author: TSZ

class Button(object):
    html = ""

    def get_html(self):
        return self.html

class Image(Button):
    html = "<img></img>"

class Input(Button):
    html = "<input></input>"

class Flash(Button):
    html = "<obj></obj>"

class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print(button_obj.create_button(b).get_html())

######################################################
def apple_function():
    """Return an Apple class, built using the
    class keyword"""

    class Apple(object):
        def __init__(self, color):
            self.color = color

        def getColor(self):
            return self.color

    return Apple

# invoking class factory function
Apple = apple_function()
appleObj = Apple('red')
print(appleObj.getColor())

######################################################
def init(self, color):
    self.color = color

def getColor(self):
    return self.color

Apple = type('Apple', (object,), {
    '__init__': init,
    'getColor': getColor,
})

appleRed = Apple(color='red')
print(appleRed.getColor())

############################################################
def create_apple_class():
    def init(self, color):
        self.color = color

    def getColor(self):
        return self.color

    return type('Apple', (object,), {
        '__init__': init,
        'getColor': getColor,
    })

Apple = create_apple_class()
appleObj = Apple('red')
print(appleObj.getColor())

###################################
# 组件化思维
# init 和 getColor 等函数会使命名空间变得杂乱无章 无法重复使用
# 通过使用类工厂，你可以最大限度地减少杂乱，并在需要时可以重用这些功能

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import os
class MyApp(App):
    def delite(self,instance):
        if self.d.text != '':
            try:
                txt=''
                stroca=0
                with open("do.txt","r") as file:
                    for line in file:
                        stroca+=1
                        if int(self.d.text) != stroca:
                            txt=txt+line
                with open("do.txt","w") as file:
                    file.write(txt)
                with open("do.txt","r") as file:
                    txt=' '+str(file.readlines())
                    self.b.text=txt.replace(',','''
        ''').replace('[','').replace(']','').replace('\'','').replace('\\n','')
            except FileNotFoundError:
                pass
            if self.b.text == ' ':
                os.remove('do.txt')
                self.b.text='создайте задачу!'
    def do(self,instance):
        with open("do.txt","a") as file:
            file.write('\n'+self.create_do.text)
        with open("do.txt","r") as file:
            txt=' '+str(file.readlines())
            self.b.text=txt.replace(',','''
''').replace('[','').replace(']','').replace('\'','').replace('\\n','')
    def build(self):
        layout=FloatLayout()
        self.create_do=TextInput(
            text="",
            pos_hint=({"x":0.4,"y":0.15}),
            size_hint=(0.2,0.1)
        )
        self.a=Button(
            text="создать задачу",
            pos_hint=({'x':0.45,'y':0.05}),
            size_hint=(0.1,0.1)
        )
        self.b=Label(
            text="создайте задачу!",
            pos_hint=({'x':0.45,'y':0.6}),
            size_hint=(0.1,0.1)
        )
        self.c=Button(
            text="удалить задачу",
            pos_hint=({'x':0.2,'y':0.05}),
            size_hint=(0.1,0.1)
        )
        self.d=TextInput(
            text="",
            pos_hint=({"x":0.2,"y":0.15}),
            size_hint=(0.1,0.1)
        )
        try:
            with open("do.txt","r") as file:
                txt=' '+str(file.readlines())
                self.b.text=txt.replace(',','''
    ''').replace('[','').replace(']','').replace('\'','').replace('\\n','')
        except FileNotFoundError:
            pass
        self.c.bind(on_press=self.delite)
        self.a.bind(on_press=self.do)
        layout.add_widget(self.create_do)
        layout.add_widget(self.a)
        layout.add_widget(self.b)
        layout.add_widget(self.c)
        layout.add_widget(self.d)
        print(self.b.text+"|")
        return layout

if __name__ == '__main__':
    MyApp().run()
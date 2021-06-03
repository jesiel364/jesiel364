from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from translate import Translator

kv  = Builder.load_string('''
FloatLayout:
	pos_hint: {'top': .999, 'right': .999}
	size_hint: .999,.999

	FloatLayout:
		pos_hint: {'center_x': .5, 'center_y': .5}
		size_hint: .8,.8

		canvas:
			Color:
				rgba: (152/255, 214/255, 208/255,0.3 )
			RoundedRectangle:
				radius: [40]
				size: self.size
				pos: self.pos

		FloatLayout:		
			
			CheckBox:
				id: ptbr
				group: 'a'
				pos_hint: {'center_x': .25, 'y': .999}
				size_hint: .3,.1
			Label:
				text: 'Português para o Inglês'
				pos_hint: {'center_x': .40, 'y': .999}
				size_hint: .3,.1

			CheckBox:
				id: ptbr
				group: 'a'
				pos_hint: {'center_x': .70, 'y': .999}
				size_hint: .3,.1
			Label:
				text: 'Inglês para o Português'
				pos_hint: {'center_x': .85, 'y': .999}
				size_hint: .3,.1

			TextInput:
				pos_hint: {'center_x': .6, 'y': .75}
				size_hint: .6,.2
				background_color: (128/255, 27/255, 157/255, 1/5)
				

			Button:
				text: 'Traduzir'
				pos_hint: {'center_x': .6, 'y': .6}
				size_hint: .2,.08
				background_color: (1/155,1/144,1/111,1/4)
				background_normal: ('1/155,1/144,1/111,1/666')

			FloatLayout:
				pos_hint: {'center_x': .6, 'center_y': .36}
				size_hint: .6,.4
				canvas:
					Color:
						rgba: (1/155,1/155,1/155,.122)
					Rectangle:
						size: self.size
						pos: self.pos




		


	''')

class Tradutor(App):
	def build(self):
		return kv 

Tradutor().run()
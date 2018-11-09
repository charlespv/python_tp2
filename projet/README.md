# How to set up a simple project in Python with your own package
 

  

1. Prepare your folders and files :

	   /project/
		   app.py
		   /form
			   __init__.py
			   render.py

2. Write in `render.py` :
		
		def render_select():
		# Display static example of a html select tag 
		couleurs = {
			'#ff9900': 'orange',
			'#00ff00': 'vert',
			'#ff0000': 'rouge',
			'#ff00ff': 'violet',
			'#0000ff': 'bleu',
			'#000000': 'noir',
			'#ffffff': 'blanc',
			'#ffff00': 'jaune'
		}
		s=''
		first = '\t<select name="couleurs">\n'
		for cnt in couleurs:
			s += ('\t\t<option value="{}" {} />{}</option>\n'.
					format(cnt, 
						"selected" if couleurs[cnt] == 'rouge' else "", 
						couleurs[cnt]))
		second = '\t</select>\n'

		return first + s + second


		def render_button():
			# Display static example of a html input used as button   
			s = '\t<input type="submit" value="Envoyer">\n'
			return s


		def render_form(code):
			# code : str : 
			# Display static example of a html form tag   
			first_part = '<form>\n'
			second_part = '</form>'
			s = first_part + str(code) + second_part
			return str(s)
			
5. Run `app.py` :
		
		$ python3 app.py

6. Your terminal will show you :
		
		<form>  
			<select name="couleurs">  
				<option value="#ff9900" />orange</option>  
				<option value="#00ff00" />vert</option>  
				<option value="#ff0000" selected />rouge</option>  
				<option value="#ff00ff" />violet</option>  
				<option value="#0000ff" />bleu</option>  
				<option value="#000000" />noir</option>  
				<option value="#ffffff" />blanc</option>  
				<option value="#ffff00" />jaune</option>  
			</select>  
			<input type="submit" value="Envoyer">  
		</form>



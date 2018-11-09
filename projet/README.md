# How to set up a simple project in Python with your own package
 

  

1. Prepare your folders and files :

	   /project/
		   app.py
		   /form
			   __init__.py
			   render.py

2. Write in `render.py` :
		
		def  render_select():
		#Display static example of a html select tag
			s = '<select name="couleurs\">\n\
					\t<option value="#ff9900" />orange</option>\n
					\t<option value="#00ff00" />vert</option>\n\
					\t<option value="#ff0000" selected />rouge</option> \n\
					\t<option value="#ff00ff" />violet</option>\n\
					\t<option value="#0000ff" />bleu</option>\n\
					\t<option value="#000000" />noir</option>\n\
					\t<option value="#ffffff" />blanc</option>\n\
					\t<option value="#ffff00" />jaune</option>\n\
				</select>\n\t'
			return s

		def  render_button():
			# Display static example of a html input used as button
			s =  '<input type="submit" value="Envoyer">\n'
			return s

		def  render_form(code):
			# code : str :
			# Display static example of a html form tag
			first_part =  '<form>\n\t  '
			second_part =  '</form>'
			s = first_part +  str(code)  + second_part
			return  str(s)

3. Import `render.py` in `__init__.py` :

		from . import  render

4. Import package `form` in `app.py` :

		import form.render as f
		
		if __name__ ==  "__main__":

			select = f.render_select()
			button = f.render_button()
			s = f.render_form(select+button)
			
			print(s)
			
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



def render_select():
    # Display static example of a html select tag    
    s = '<select name="couleurs\">\n\
            \t<option value="#ff9900" />orange</option>\n\
            \t<option value="#00ff00" />vert</option>\n\
            \t<option value="#ff0000" selected />rouge</option> \n\
            \t<option value="#ff00ff" />violet</option>\n\
            \t<option value="#0000ff" />bleu</option>\n\
            \t<option value="#000000" />noir</option>\n\
            \t<option value="#ffffff" />blanc</option>\n\
            \t<option value="#ffff00" />jaune</option>\n\
        </select>\n\t'
    return s

def render_button():
    # Display static example of a html input used as button   
    s = '<input type="submit" value="Envoyer">\n'
    return s

def render_form(code):
    # code : str : 
    # Display static example of a html form tag   
    first_part = '<form>\n\t '
    second_part = '</form>'
    s = first_part + str(code) + second_part
    return str(s)
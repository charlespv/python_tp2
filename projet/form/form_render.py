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
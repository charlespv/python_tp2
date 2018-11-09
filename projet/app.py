import form.render as f

if __name__ == "__main__":
    select = f.render_select()
    button = f.render_button()
    s = f.render_form(select + button)
    print(s)


 
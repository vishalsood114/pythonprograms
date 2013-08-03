def render_template(_filename, **kwargs):
    t = open(_filename).read()
    return t % kwargs

print render_template("hello.tmpl", name="python")



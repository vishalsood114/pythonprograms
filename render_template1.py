def render_template1(_filename, *args):
    t = open(_filename).read()
    return t % args

print render_template1("a.tmpl", "hello", "world")
print render_template1("b.tmpl", "hello", "world","geeks")

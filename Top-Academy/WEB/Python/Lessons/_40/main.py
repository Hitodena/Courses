from jinja2 import Environment, FileSystemLoader

subs = ['Culture', 'Science', 'Politics', 'Sport']

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(list_table=subs)

print(msg)

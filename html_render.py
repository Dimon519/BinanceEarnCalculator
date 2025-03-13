from jinja2 import Environment, FileSystemLoader

def ninja2_render(pages):   
    env = Environment(loader=FileSystemLoader('web/templates'))
    for page in pages:
        template = env.get_template(f'{page}.html')
        rendered_html = template.render({'title' : f'{page}'})
        with open(f'web/{page}.html', 'w', encoding='utf-8') as f:
            f.write(rendered_html)
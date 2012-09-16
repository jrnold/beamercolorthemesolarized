##' Create templates tex
import re
import subprocess as sp
import os

# os.putenv('TEXINPUTS', '..')

import jinja2

params = [{'color':'yellow', 'dark':'light'},
          {'color':'blue', 'dark':'light'},
          {'color':'yellow', 'dark':'dark'}]

def change_ext(x, ext):
    re.sub(r'\..*?$', ext, x)

## patterns from http://e6h.de/post/11/
env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%-',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader('.')
)

template = env.get_template('beamerthemeexamplebase.tex')

def main():
    for param in params:
        filename = 'example_{color}_{dark}.tex'.\
                   format(**param)
        with open(filename, 'w') as f:
            f.write(template.render(param))
            # rc = sp.call('pdflatex %s' % filename, shell=True)
            # if rc == 0:
            #     for ext in ['.aux', '.log', '.nav', '.snm', '.toc']:
            #          os.remove(change_ext(filename, ext))
            # else:
            #     continue
        # sp.call(['pdftoppm', '-png', change_ext(filename, '.pdf')])

if __name__ == '__main__':
    main()
        

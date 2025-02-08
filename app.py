import json 
import requests 
from pywebio.input import *
from pywebio.output import *
from pywebio.session import * 


def get_fun_facts(_):
    clear()
    put_html('<div style="width:200px; hight:200px; mx-auto">'
            '<h2>Fun Fact Generator App</h2>'
            '</div>')
    
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')

    response = json.loads(response.text)

    fact = response['text']

    style(put_text(fact), 'color:black; font-size:24px')

    put_buttons([dict(label='click me', value='outline-success', color='outline-success')],
               onclick=get_fun_facts)
    



if __name__ == '__main__':

    put_html('<div style="width:200px; hight:200px; mx-auto">'
            '<h2>Fun Fact Generator App</h2>'
            '</div>')
    
    put_buttons([dict(label='click me', value='outline-success', color='outline-success')],
               onclick=get_fun_facts)
    
    hold()
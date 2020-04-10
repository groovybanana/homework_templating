import glob
import os
from jinja2 import Template
import datetime
import re

pages = [] # creating an empty pages list to fill dynamically fill from the contents of the content folder


def year(): # get current year for copyright
    now = datetime.datetime.now()
    return str(now.year)

def new_page(): # function for creating a new page via the command line
    page_name = input('What is the name of your page? ') # asks what the new page should be called
    clean_name = re.sub('[^0-9a-zA-Z]+', '_', page_name) # cleans given name of page to replace non alphanumeric characters with an underscore
    content = '<h1>New Content!</h1>\n\n<p>New content...</p>' # defines dummy content for new pages
    open('content/'+clean_name+'.html', "w+").write(content) # opens up new page and writes dummy content to it



def my_pages(): #this function creates a dynamically generated list of pages contained in the content folder
    all_html_files = glob.glob('content/*.html') # list of all files inside the content folder
    for item in all_html_files:
        file_path = os.path.basename(item) #prints the filepath, or in this case, the filename since all files are inside the same folder
        name_only, extension = os.path.splitext(file_path) #this splits the value of file_path, which is something like index.html into two parts, name_only, which returns index and extenstion which returns .html
        pages.append({ # this appeads the following key/value pairs to my currently empty pages list
            "filename": item, 
            "output": 'docs/' + file_path,
            "active": 'active',
            "title": name_only,
            "link": file_path,
        })

my_pages()

def create_pages():
    for page in pages: # for loop using the pages list that was dynamically generated above
        page_html = open(page['filename']).read() # defining the content of the page, what will replace {{ contnet }} in the template
        template_html = open("templates/base.html").read() # defining our template html, basically this is simply saying that template_html is the same as base.html in the templates folder
        template = Template(template_html) # defining Jinja template... I think...
        result = template.render({  # rendering the jinja template and assigning the result to the result variable
            'title': page['title'], # the key title is given the value of title key from the pages list
            'content': page_html, # the key content is given the value of page_html 
            'link': page['link'], # the key link is given the value of the link key from the pages list
            'active': page['active'], # the key active is given the value of the active key from the pages list
            "year": year(), # grabs current year for copyright
            'pages':pages,
        })

        open(page['output'], "w+").write(result) # opens the individual html pages and writes the value of result to the individual pages


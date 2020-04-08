import glob
import os

pages = []

def page_list():
    all_html_files = glob.glob('content/*.html')
    for item in all_html_files:
        file_path = os.path.basename(item)
        name_only, extension = os.path.splitext(file_path)
        pages.append({
            "filename": item,
            "output": 'docs/' + file_path,
            "active": "{{active_" + name_only + "}}",
            "title": name_only,
            "link": file_path,
        })


page_list()
print('-----------------------------------')

from pprint import pprint
pprint(pages)

# print(pages)

def year():
    import datetime
    now = datetime.datetime.now()
    return str(now.year)

def read_in_page(page):
    template = open("./templates/base.html").read()
    filename = page['filename']
    output = page['output']
    title = page['title']
    active = page['active']
    contents = open(filename).read()
    return template, filename, output, title, contents, active

def add_title_content(template,filename,output,title,active,year):
        the_title_added = template.replace("{{title}}", title) 
        filename_in = filename[9:]
        nav_text = '<a class="nav-link" data-toggle="tab" href=".'+filename_in+'">'
        year = year()
        highlighted_nav = the_title_added.replace(nav_text, active).replace("{{year}}", year)
        if nav_text in template:
            open(output, "w+").write(highlighted_nav)
        else:
            pass
        contents = open(filename).read()
        finished_combined_page = highlighted_nav.replace("{{content}}", contents)
        open(output, "w+").write(finished_combined_page)
        return finished_combined_page
  

def main():
    print('rebuilding pages')
    for page in pages:
        template, filename, output, title, contents, active = read_in_page(page)
        add_title_content(template,filename,output,title,active,year)
        print(output)
    print('rebuild complete')
main()


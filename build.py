pages = [ {
    "filename": "./content/index.html", 
    "output": "./docs/index.html", 
    "title": "Chris Moe's Spring 2020 bootcamp project",
    "active": '<a class="nav-link active" data-toggle="tab" href="./index.html">', 
},
{
    "filename": "./content/blog.html", 
    "output": "./docs/blog.html", 
    "title": "My personal blog",
    "active": '<a class="nav-link active" data-toggle="tab" href="./blog.html">', 
},
{
    "filename": "./content/about.html", 
    "output": "./docs/about.html", 
    "title": "Learn all about Me",
    "active": '<a class="nav-link active" data-toggle="tab" href="./about.html">', 
},
{
    "filename": "./content/contact.html", 
    "output": "./docs/contact.html", 
    "title": "Reach out and get in touch with me",
    "active": '<a class="nav-link active" data-toggle="tab" href="./contact.html">', 
},
{
    "filename": "./content/portfolio.html", 
    "output": "./docs/portfolio.html", 
    "title": "Chris Moe: Portfolio",
    "active": '<a class="nav-link active" data-toggle="tab" href="./portfolio.html">', 
},
]

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


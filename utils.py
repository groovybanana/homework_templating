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
print(pages)
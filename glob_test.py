import glob
import os

all_html_files = glob.glob("content/*.html")
print('-----------VALUE OF ALL_HTML_FILES------------')
print(all_html_files)


file_path = "content/blog.html"
file_name = os.path.basename(file_path)
print('-----------FILE_NAME------------')
print(file_name)
name_only, extension = os.path.splitext(file_name)
print('-----------VALUE OF NAME_ONLY------------')
print(name_only)
print('-----------VALUE EXTENSTION------------')
print(extension)
print('-----------VALUE NAME ONLY AND EXTENSTION------------')
print(name_only+extension)


pages = []
pages.append({
    "filename": "content/index.html",
    "title": "Index",
    "output": "docs/index.html",
    })
print('-----------VALUE OF PAGES------------')
print(pages)

pages = []
pages.append({
    'filename': all_html_files[0],
    "title": "Index",
    # "output": "docs/index.html",
})
print('-----------VALUE OF MY STUPID ATTEMPT AT PAGES------------')
print(pages)
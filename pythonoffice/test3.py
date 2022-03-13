import pdfkit
from pydocx import PyDocX

# pdfkit.from_url()
# pdfkit.from_string()

html = PyDocX.to_html('简历1.docx')
f = open('简历1.html', 'w')
f.write(html)
f.close()

pdfkit.from_file('简历1.html', 'test3.pdf')
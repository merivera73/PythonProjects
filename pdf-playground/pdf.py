import pypdf
 
# template = pypdf.PdfReader(open('superduper.pdf', 'rb'))
# watermark = pypdf.PdfReader(open('dummy.pdf', 'rb'))
# output = pypdf.PdfWriter()
 
# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)
 
with open('dummy.pdf', 'rb') as outputFile:
    reader = pypdf.PdfReader(outputFile)
    page = reader.get_page(0)
    print(page.rotate(90))
    writer = pypdf.PdfWriter()
    with open('tilt.pdf', 'wb') as new_outputFile:
        writer.write(new_outputFile)
        
        
        
    
# output.write
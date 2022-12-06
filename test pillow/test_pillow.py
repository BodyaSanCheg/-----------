from PIL import Image, ImageDraw
import img2pdf
from PyPDF2 import PdfFileWriter, PdfFileReader

a4_height = 1755
a4_width = 1241
img_degrees = 99
a4_paper_size = (a4_width, a4_height)
img_a4_paper = Image.new('RGBA', a4_paper_size)
image_resize = Image.open('test pillow/img/img.jpg').convert("RGBA")


# Функция изменения прозрачности
# datas = image_resize.getdata()
# newData = []

# for item in datas: # Изменение прозрачности
#     newData.append((item[0], item[1], item[2], int(255/100*80)))

# image_resize.putdata(newData)

image_resize = image_resize.rotate(img_degrees, expand=True, fillcolor = True).resize((279, 999)) # Поворот на угол и изменение размеров
x, y = image_resize.size

print(f"{x=}, {y=}")

# coordinates = (0, 0) # Слева вверху
# coordinates = (0, (a4_height - y)//2) # Слева по центру
# coordinates = (0, a4_height - y) # Слева внизу
# coordinates = ((a4_width - x)//2, 0) # Центр сверху
# coordinates = ((a4_width - x)//2, (a4_height - y)//2) # Центр по центру
# coordinates = ((a4_width - x)//2, a4_height - y) # Центр внизу
# coordinates = (a4_width - x, 0) # Справа сверху
# coordinates = (a4_width - x, (a4_height - y)//2) # Справа по центру
coordinates = (a4_width - x, a4_height - y) # Справа внизу

img_a4_paper.paste(image_resize, coordinates, image_resize)
img_a4_paper.save('test pillow/img/img_a4_paper.png')
# img_a4_paper.show()

# specify paper size (A4)
a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(a4inpt)

with open("test pillow/img/name.pdf","wb") as f:
	f.write(img2pdf.convert('test pillow/img/img_a4_paper.png', layout_fun=layout_fun))

input_file = 'test pillow/img/test-pdf-2pdf.pdf'
wotermark_pdf = "test pillow/img/name.pdf"
out_put_file = 'test pillow/img/wotermart.pdf'

watermark_obj = PdfFileReader(wotermark_pdf)
watermark_page = watermark_obj.getPage(0)

pdf_reader = PdfFileReader(input_file, strict=False)
pdf_writer = PdfFileWriter()

for page in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page)
    page.mergePage(watermark_page)
    pdf_writer.addPage(page)

with open(out_put_file, 'wb') as out:
    pdf_writer.write(out)

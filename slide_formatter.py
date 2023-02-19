from PyPDF2 import PdfReader, PdfWriter

input_file_name = str(input("Input file name: "))
reader = PdfReader(input_file_name, 'r')
readerBinary = PdfReader(input_file_name, 'rb')
writer = PdfWriter()


# Loop through pages and find the last page with the given page number at the bottom.
prevLastLine = reader.pages[0].extract_text().split("\n").pop()
indexesToKeep = []
for i in range(1, len(reader.pages)):
    page = reader.pages[i]
    # Last line always contains the 'actual' page number
    lastLine = page.extract_text().split("\n").pop()
    # Keep the previous page since is the 'most complete'
    if (lastLine != prevLastLine):
        prevLastLine = lastLine
        indexesToKeep.append(i-1)
# Keep the final page
indexesToKeep.append(len(reader.pages) - 1)

for i in range(0, len(reader.pages)):
    if i in indexesToKeep:
        p = readerBinary.pages[i]
        writer.add_page(p)

output_file_name = input_file_name.removesuffix(".pdf") + "_edited.pdf"
with open(output_file_name, 'wb') as f:
    writer.write(f)

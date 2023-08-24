from PyPDF2 import PdfReader, PdfWriter
import os
# Get file name
input_file_name = str(input("Input file name: ")).strip()

# Check if file exists
if (not os.path.isfile(input_file_name)):
    print("File does not exist")
    exit()

# Open file
try:
    reader = PdfReader(input_file_name, 'r')
    readerBinary = PdfReader(input_file_name, 'rb')
    writer = PdfWriter()
except:
    print("Error opening file")
    exit()

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

# Add pages to writer
for i in range(0, len(reader.pages)):
    if i in indexesToKeep:
        p = readerBinary.pages[i]
        writer.add_page(p)

# Write to file
output_file_name = input_file_name.removesuffix(".pdf") + "_edited.pdf"
with open(output_file_name, 'wb') as f:
    writer.write(f)
    f.close()
print("Done! File written to " + output_file_name)

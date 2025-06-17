import fitz  # PyMuPDF
import sys

source_pdf = sys.argv[1]
target_pdf = sys.argv[2]

# Load the source PDF with the bookmarks
src_doc = fitz.open(source_pdf)

# Extract bookmarks (outline)
bookmarks = src_doc.get_toc(simple=True)  # [level, title, page]
src_doc.close()

# Example output:
#for item in bookmarks:
#    print(item)

name, ext = target_pdf.rsplit('.', 1)

print(name)

# Path to the PDF to which you want to add the bookmarks
output_pdf = f"{name} with ToC.pdf"

# Open target and write bookmarks
target_doc = fitz.open(target_pdf)

# Insert bookmarks
target_doc.set_toc(bookmarks)

# Save updated PDF
target_doc.save(output_pdf)
target_doc.close()

print("Bookmarks added successfully.")


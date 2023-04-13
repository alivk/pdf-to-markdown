import os
import re
import subprocess
from pdf2image import convert_from_path

pdf_file = "example.pdf"
output_dir = "markdown_output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Convert PDF to images
pages = convert_from_path(pdf_file)

for i, page in enumerate(pages):
    # Extract slide title from page using pdftotext command
    title_command = f"pdftotext -f {i+1} -l {i+1} -layout '{pdf_file}' -"
    title = subprocess.check_output(title_command, shell=True).decode("utf-8")
    title = f'page-{i+1}-' + re.sub(r'\W+', '-', title.lower().strip()[:20])
    
    # Save image to disk
    image_folder = os.path.join(output_dir, f"{title}.assets")
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    image_file = os.path.join(image_folder, f"page-{i+1}.png")
    page.save(image_file, "PNG")



    # Generate markdown file content
    markdown_content = f"""# {title}
### PPT Slide
<img src="{title}.assets/page-{i+1}.png" alt="" style="float:left;width:600px;" />

### Speaker Notes
This is the speaker notes for slide {i+1}.
<!-- NextPage -->
"""

    # Save markdown to disk
    markdown_file = os.path.join(output_dir, f"{title}.md")
    with open(markdown_file, "w") as f:
        f.write(markdown_content)

print("Conversion complete.")

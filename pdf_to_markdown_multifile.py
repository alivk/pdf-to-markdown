import os
import re
import subprocess
from pdf2image import convert_from_path

pdf_dir = "pdf_for_all_modules"
pdf_dir = input('What is your pdf file folder name?\n') 
output_dir = pdf_dir + "_output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, pdf_file)

        # Create subdirectory with same name as PDF file
        pdf_name = os.path.splitext(pdf_file)[0]
        pdf_output_dir = os.path.join(output_dir, pdf_name)
        if not os.path.exists(pdf_output_dir):
            os.makedirs(pdf_output_dir)

        # Convert PDF to images
        pages = convert_from_path(pdf_path)

        for i, page in enumerate(pages):
            # Extract slide title from page using pdftotext command
            title_command = f"pdftotext -f {i+1} -l {i+1} -layout '{pdf_path}' -"
            content = subprocess.check_output(title_command, shell=True).decode("utf-8")
            title = f'pg-{i+1}-' + re.sub(r'\W+', '-', content.lower().strip()[:30])

            # Save image to disk
            image_folder = os.path.join(pdf_output_dir, f"{title}.assets")
            if not os.path.exists(image_folder):
                os.makedirs(image_folder)
            image_file = os.path.join(image_folder, f"pg-{i+1}.png")
            page.save(image_file, "PNG")

            # Generate markdown file content
            markdown_content = f"""# {title}
### PPT Slide
<img src="{title}.assets/pg-{i+1}.png" alt="" style="float:left;width:600px;" />

### Speaker Notes
This is the speaker notes for slide {i+1}.
{content}
<!-- NextPage -->
"""

            # Save markdown to disk
            markdown_file = os.path.join(pdf_output_dir, f"{title}.md")
            with open(markdown_file, "w") as f:
                f.write(markdown_content)
                
# Add README.md in output folder
                
readme_file = os.path.join(output_dir, "README.md")
with open(readme_file, "w") as f:
    f.write("# " + output_dir + "\n\n")
    f.write("This directory contains the output of my PDF conversion process.\n\n")
    f.write("## Directory Structure\n\n")
    f.write("- `pdf_for_all_modules/`\n")
    f.write("  - Directory containing input PDF files.\n")
    f.write("- `pdf_for_all_modules_output/`\n")
    f.write("  - Directory containing output files.\n")

print("Conversion complete.")

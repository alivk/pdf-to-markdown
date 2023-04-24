### Cloud9 Amazon Linux 2 Convertion from pdf to markdown notes

Steps to set up and run the code in a new Cloud9 environment using Amazon Linux 2:

1. Install required packages:
```
sudo yum install -y poppler-utils
sudo pip3 install pdf2image
```

2. Clone the repository and navigate to the project directory:
```
git clone https://github.com/alivk/pdf-to-markdown.git
```

3. Run the script:
```
python3 pdf_to_markdown.py
```
The generated markdown files will be saved in the markdown_output folder.

 - pdf_to_markdown_singlefile.py
   for single file, you need to provide single pdf document which might exported from ppt
   
 - pdf_to_markdown_multifile.py
   for multi file, you need to place all those pdf document in a folder and provide folder name to the script to process

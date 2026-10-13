import subprocess
import os
import sys

def textContent(fileName: str) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", os.path.join(dir_path, fileName), "-"],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout



if len(sys.argv) != 3:
    print("Provide a folder and and output file\nExample:\n     ./program [./pdfs_folder] [output_file_path.txt]")
    sys.exit(1)

dir_path = sys.argv[1]
out_file_path = sys.argv[2]

if not out_file_path.lower().endswith(".txt"):
    out_file_path += ".txt"




# Get only PDF files, excluding folders
files = [
    f for f in os.listdir(dir_path)
    if os.path.isfile(os.path.join(dir_path, f))
    and f.lower().endswith(".pdf")
]

if not files:
    print("The Provided folder does not contain any .pdf files")
    sys.exit(1)

with open(out_file_path, "w") as out_file:
    for f in files:
        out_file.write(textContent(f) + " \n")
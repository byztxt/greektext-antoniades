import beta_code
import re
import os 

# Define the path to the folder containing the files
folder_path = "../textonly"

# Create a subfolder named "unicode" if it doesn't already exist
if not os.path.exists(os.path.join(folder_path, "unicode")):
    os.makedirs(os.path.join(folder_path, "unicode"))

# List of file names
book_list = [
    "1CO",
    "1JO",
    "1PE",
    "1TH",
    "1TI",
    "2CO",
    "2JO",
    "2PE",
    "2TH",
    "2TI",
    "3JO",
    "AC",
    "COL",
    "EPH",
    "GA",
    "HEB",
    "JAS",
    "JOH",
    "JUDE",
    "LU",
    "MR",
    "MT",
    "PHM",
    "PHP",
    "RE",
    "RO",
    "TIT",
]

# Loop through the file names
for book in book_list:
    # Get the full file path by joining the folder path and file name
    file_path = os.path.join(folder_path, book + '.ANT')

    # Get the filename from the path
    filename = os.path.basename(file_path)
    
    # Read the file
    with open(file_path, "r") as inputfile:
        clean = inputfile.read()
        # Substitute letters to ensure that beta_code properly converts to Unicode
        clean = clean.replace('v', 's')
        clean = clean.replace('c', 'j')               # 1. replacing c with x (using j as a placeholder)
        clean = clean.replace('x', 'c')               # 2. 
        clean = clean.replace('j', 'x')               # 3.
        
        clean = clean.replace('y', 'j')               # 1. replacing y with q (using j as a placeholder)
        clean = clean.replace('q', 'y')               # 2. 
        clean = clean.replace('j', 'q')               # 3. 
                
        # Convert from betacode to unicode using https://github.com/perseids-tools/beta-code-py
        clean = beta_code.beta_code_to_greek(clean)       # convert to unicode Greek letters
        
        # Final cleanup 
        clean = re.sub(r'σ\b', 'ς', clean)                # Fix final sigmas
        clean = re.sub(' --', '\u2014', clean)            # Convert dashes to em dashes
        
        clean = re.sub('\n\n', '\n\u00B6', clean)         # Indicate original paragraphing with a 'pilcrow' (¶)
        clean = re.sub('\n', '', clean)                   # Remove all line breaks
        clean = re.sub('(?<=[0-9])·', ':', clean)         # Fix references that were mangled by beta_code 
        clean = re.sub('(\d+:\d+ )', '\n\\1', clean)      # find all verse beginnings and add a line break before them
        clean = re.sub('(?m)^\n', '', clean)              # Remove extra line break at beginning of file
        clean = re.sub('\u00B6', '\n', clean)             # Restore original paragraphing

    # Save the Unicode text to a file in the "unicode" subfolder
    with open(os.path.join(folder_path, "unicode", book + '.txt'), "w", encoding="utf-8") as outputfile:
        outputfile.write(clean)

# PDF_search

First we put the script in the SAME folder as the PDF files we want to sort, search and create a list of them.

Script then searches the folder only for files that have .pdf extension and then it sorts it by asc order in a list (pdfFiles).
After that I just get the length of a longest PDF name so that the script can set the width of the columns in excel to automatically fit. 
row and column are set to 0 because that's how the script recognizes ABC... rows and columns in excel, after that the excel file is created and a worksheet is also created.

The loop goes through the list of stored PDF files and writes them as a apsolute path to the file in excel, then row is incremented by one -> meaning that every PDF in a list will be writted in a new row(A1, A2,...)

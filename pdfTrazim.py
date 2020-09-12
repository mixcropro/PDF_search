import os, xlsxwriter
#skripta mora biti unutar istog direktorija kao i pdf-ovi
pdfFiles = []
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)
    pdfFiles.sort(key=str.lower)

longestPDFName = len(max(pdfFiles, key=len))

row = 0
column = 0
workbook = xlsxwriter.Workbook('popisPDF.xlsx')
worksheet = workbook.add_worksheet()

for line in pdfFiles:
    worksheet.write_url(row, column, line, worksheet.set_column(column, column, longestPDFName))
#line je ime pdfa i ova linija ih kreira link koji otvara taj file
    row +=1
workbook.close()


# Extracting the document number from PDF documents 

## Findings
- Extracting text directly from PDF documents have multiple issues including:
    - PDF documents that contain symbols or non-embedded fonts returns incorrect characters when parsed. for example: `(12)` is sometimes parsed as `a2)` or `(»j` and `(10)` is parsed as `(Io)` or `(io)`. (This issue happens across  all the pdf parsers that we tested)
    - PDF files can have different encoding and in some cases the PDF parsing libraries are not able to parse the file correctly returning empty text or line feeds as the parsing result.
    - Some PDF files are made from scanned documents (images not text)
- PDF text extraction is a time consuming process. In some cases, a patent document could take up to 5 Minutes to run through an OCR engine and tens of seconds to be processed by a PDF parser
- Patent documents are not uniform in terms of their structure. In some cases, the Bibliographic data is written in a tabular format without a layout and in other cases in split page format.
- OCR engines like `tesseract` doesn't suffer from the text parsing and encoding issues that PDF parsers have. One drawback of OCR engines is the processing time compared to regular text parsers.

## Approach
The recommended approach to parse the patent and patent publication numbers is:
- Use `PyPDF2` to load the first page (contains the doc number) of pdf document and write out a temporary pdf file
- Attempt to parse the text of the tmp file. If this succeeds, save the value in-memory to cross-check against the OCR result
- Use `fitz` to capture an image of the tmp pdf document and save it to a tmp .png file
- Use the OCR engine `tesseract` to extract the text from the tmp image
- Use Regex to extract the document number from the extracted text from the PDF parsing step and the OCR step
- Process the matching doc numbers (remove additional chars) and cross check them against each-other for validation  

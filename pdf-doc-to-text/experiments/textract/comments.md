## Assessment
1. Do you recommend the textract package for parsing the text from PDF documents?

Yes

2. What are the reasons for your decision? 

- The textract package wraps multiple text parser  `tesseract` (OCR-based parser), `pdftotext` and `pdfminer`. This enables us to parse both scanned and text pdfs with "one library".
- Simple installation besides the fact that we might have to install some os-packages on the server ourselves
- Good parsing quality for both text and OCR docs
- The whole package is one function `process(...args)`

3. What are the cons of the textract framework?
- Inability to pass additional parameters to the downstream parsers (we can only call the process() function). I think this is OK for our case since we only need this library for text parsing.
- Poor documentation. The library is very simple "calls the cli of the parser packages" and I think we can still use it.

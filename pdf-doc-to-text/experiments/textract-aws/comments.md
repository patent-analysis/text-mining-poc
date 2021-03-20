## Extracting text from PDF files using the AWS Textract service assessment
### 1. Do you recommend the AWS Textract service for parsing text from PDF documents?

No

### 2. What are the reasons for your decision? 

- The Textract service didn't parse the epitopes in almost all cases. In addition, I found that Textract didn't parse the amino acid sequences correctly. for example: `I`s were sometimes interpreted as `/`  and in other cases were completely skipped.
- The Textract framework is great for OCR-based files and highlighting the location of the detected text in the document (coordinates of each detected word). In our case, we need a simpler text parsing framework for both OCR and text-based pdf files. 


### 3. Is there a case where you find Textract to be useful for this project?
If we need to highlight or visualize the location of the parsed text in the original document, AWS Textract would be a good solution for this case.

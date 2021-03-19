## Assessment
1. Do you recommend Textract for parsing the text from PDF documents?

No

2. What are the reasons for your decision? 

- The Textract framework is great for OCR and highlighting the location of the detected text within the document. In our case, we need a simpler text parsing framework that can read a PDF document and extract the text for preprocessing in the pipeline. 
- Textract missed the epitopes in almost all cases which is one of the key data points that we are looking for. In addition, I found that Textract miss-parsed some sequences where  `I`s were either interpreted as `/` or completely skipped.

3. Is there a case where you find Textract to be useful for this project?
If we need to extract text from PDF images (OCR), Textract could be considered as one of the solutions to solve this case.

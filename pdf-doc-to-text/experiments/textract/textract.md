## Steps to test the textract document analysis and text detection features.

### upload the patents to an s3 bucket
```
# from this directory and using an aws profile called me, run the commands below
aws s3 cp ../../patents/us8859741.pdf s3://patents-test-docs/us8859741.pdf --acl private --profile me

aws s3 cp ../../patents/US9550837.pdf  s3://patents-test-docs/US9550837.pdf --acl private  --profile me

aws s3 cp ../../patents/US2010068199.pdf s3://patents-test-docs/US2010068199.pdf --acl private --profile me
```


### Trigger the text detection jobs
```
aws textract  start-document-text-detection  --document-location '{"S3Object":{"Bucket":"patents-test-docs","Name":"us8859741.pdf"}}' --profile me
"JobId": "b46c9dce4d1310c8697611012b966145326ac97976e5a126e8afc0478029c2ea"

aws textract  start-document-text-detection  --document-location '{"S3Object":{"Bucket":"patents-test-docs","Name":"US9550837.pdf"}}' --profile me
"JobId": "88ee0b3b58ddf94bb6f08cc8911bb5ca46b40ee99183654836d4644092f97506"

aws textract  start-document-text-detection  --document-location '{"S3Object":{"Bucket":"patents-test-docs","Name":"US2010068199.pdf"}}' --profile me
"JobId": "ea407759457d9faea017dcaf28df3a684273cc9a38acd2b74eab8d6894b75318"
```


### Trigger the document analysis jobs
```
aws textract  start-document-analysis  --feature-types '["TABLES","FORMS"]' --document-location '{"S3Object":{"Bucket":"patents-test-docs","Name":"us8859741.pdf"}}' --profile me
"JobId": "1a80da1f428c114bae5a8360f7d335517fd0c6d436cd3d1c420583c50b0fb189"

aws textract  start-document-analysis  --feature-types '["TABLES","FORMS"]' --document-location '{"S3Object":{"Bucket":"patents-test-docs","Name":"US9550837.pdf"}}' --profile me
"JobId": "9c3ffeb16dfd6c193e061a6e1c0a8d00991c901691c61617b1cc8fc3cdc080c3"

aws textract  start-document-analysis  --feature-types '["TABLES","FORMS"]' --document-location '{"S3Object":{"Bucket":"patents-test-docs","Name":"US2010068199.pdf"}}' --profile me
"JobId": "da512e243d348803611757e234d3cbbd811cd17192e43d914c7ecd794902678e"
```

### Inspect the results
```console
aws textract get-document-text-detection --profile me  --job-id b46c9dce4d1310c8697611012b966145326ac97976e5a126e8afc0478029c2ea > detection_us8859741.json

aws textract get-document-text-detection --profile me  --job-id 88ee0b3b58ddf94bb6f08cc8911bb5ca46b40ee99183654836d4644092f97506 > detection_US9550837.json

aws textract get-document-text-detection --profile me  --job-id ea407759457d9faea017dcaf28df3a684273cc9a38acd2b74eab8d6894b75318 > detection_US2010068199.json

aws textract get-document-analysis --profile me  --job-id 1a80da1f428c114bae5a8360f7d335517fd0c6d436cd3d1c420583c50b0fb189 > analysis_us8859741.json

aws textract get-document-analysis --profile me  --job-id 9c3ffeb16dfd6c193e061a6e1c0a8d00991c901691c61617b1cc8fc3cdc080c3 > analysis_US9550837.json

aws textract get-document-analysis --profile me  --job-id da512e243d348803611757e234d3cbbd811cd17192e43d914c7ecd794902678e > analysis_US2010068199.json
```

### Comments about the results can be found in the comments.md file
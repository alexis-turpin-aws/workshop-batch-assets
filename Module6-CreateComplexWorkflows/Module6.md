# Module 6: Combine AWS Batch & Step Functions to create complex workflows

In this module, we will create a workflow with Step Functions to parallelize multiple executions of your AWS Batch jobs. Each execution uses a different Stock parameter. Stock parameters are stored in a file we upload in the s3 bucket. S3 triggers a Lambda that invokes a State Machine that parses the file, then runs one job per line.

## Instructions

1. In Cloud9 IDE, create a file and write some random stock symbols:

`echo -e "TSLA\nNVDA\nFB\nNFLX\nINTC" > stocks.txt`

1. Go to **Lambda**, click **Create function**. Name it *lambdaParseS3Object. *Select **Python 3.8**. Attach role TODO. Click **Create function.** Copy the code in *src/lambda/lambdaParseS3Object.py *and paste it the Designer*. ***Save**.

2. Go to **Step Functions **and create a new** State Machine**. Copy the snippet in src/statemachines/template.json and paste it in the Designer. Replace *JOB-DEFINITION-NAME:REVISION_ID* and* JOB-QUEUE-NAME* with your Job parameters. Refresh the graph to render the definition. Click **Next**. Select role *stepFunctionsServiceRole*, finally click **Create State Machine**.

3. Now your State Machine is ready, we need to invoke it when the *stocks.txt* file is uploaded in the S3 bucket we created in the first module. Go to **Lambda**, click **Create function**. Name it *lambdaStartStateMachine. *Select **Python 3.8**. Attach role TODO. Click **Create function.** Copy the code in *src/lambda/lambdaStartStateMachine.py *and paste it the Designer. Edit the variable* STEP_FUNCTION_ARN *by the ARN of your State Machine. **Save**.

4. Go to **S3**. Select your bucket, click on **Properties** tab then **Events. **Add notification:

    Name: *S3PutObject*
    Events: *PUT*
    Prefix: *stocks.txt*
    Send to: *Lambda Function*
    Lambda: *lambdaStartStateMachine*
    **Save**.

1. Upload *stocks.txt *in bucket root. Go to **Step Functions** and look at the State Machine executions. Check the results in the **S3** bucket.


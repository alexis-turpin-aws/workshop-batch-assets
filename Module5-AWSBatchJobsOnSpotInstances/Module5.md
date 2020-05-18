# Module 5: Run AWS Batch jobs on EC2 Spot Instances

In this module, you will learn how to run batch jobs using AWS Batch on a compute environment backed by Amazon EC2 Spot Instances. AWS Batch’s native integration with EC2 Spot Instances means you can save up to 90% on your compute costs when compared to On-Demand pricing.

## Instructions

1. In the AWS Batch console, create a new **Compute environment**.
2. In **Create a compute environment** section:

* Make sure using **Managed Compute environment type**.
* Use `simulator-compute-environment-spot`
* Pick the **Service role** you just created.
* Select e as Instance role.

Keep the defaults.

1. In **Configure your compute resources** section, choose **Spot **and leave the rest as default.
2. In **Networking** section, select your VPC **Workshop Batch**, subnets and Security Groups.
3. Finally, click **Create**.
4. Go to **Job Queues **and edit the queue you created.
5. Add the Compute environment for Spot you just created and move it first on the list. Click **Edit**.
6. Now you are ready to run your job on Spot Instances. Go to **Jobs** and clone the last successful job. **Submit job**.
7. Now that your job has been executed on Spot Instances, it’s helpful to quantify the savings you have achieved compared to On-Demand pricing. To visualize your savings, go to the **Spot Requests** section of the EC2 console and click on the **savings summary** button. This will show you a summary of your achieved savings from using Spot Instances.


# Next step 

You have successfully built an batch job backed by Amazon EC2 Spot Instances.

Go to [**Module 6 : Create complex Workflows**](../Module6-CreateComplexWorkflows/Module6.md) section to create Complex Workflows by using Step Functions. 



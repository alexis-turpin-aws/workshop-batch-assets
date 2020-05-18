# Run Monte Carlo Simulations on a Fully Managed Solution using AWS Batch


* [Introduction](#intro)
	* [Requirements](#req)
	* [Lab Overview](#labs)
	* [Conventions](#conventions)
* [Let's Start](#begin)

<a name="intro"></a>
## Introduction:  
Algorithmic trading, or algo-trading is the process of using algorithms for placing a stock trade based on a set of perceived market conditions. These algorithms are based on price, quantity or other mathematical model without the risk of human emotion influencing the buy or sell action. This workshop will walk your through some of the basic tools and concepts that algorithmic traders employ to build fully automated trading systems. 

Monte Carlo Simulations involve repeated random sampling to model the probability of a complex problem that is difficult to predict using other methods due to the nature of the variables involved. We will use Monte Carlo Simulations to simulate and predict future stock movement by repeatedly sampling random stock values based on past results. 

The goal of this workshop is not to become financial gurus. I doubt we'll be rich at the end, but hopefully we'll have learned how to build batch processing pipelines using AWS Batch service and save up to 90% using Spot Instances. 

If you'd like to learn more: [Basics of Algorithmic Trading: Concepts and Examples](https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp)

<a name="req"></a>
### Requirements:  
* AWS account with elevated privileges allowing you to interact with EC2, AWS Batch, Step Functions, S3 and Lambda.
* Familiarity with Python, AWS, and basic understanding of [algorithmic stock trading](http://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp)  - not required but a bonus

<a name="Labs"></a>
### Lab Overview:  
These labs are designed to be completed in sequence.  If you are reading this at a live AWS event, the workshop attendants will give you a high level run down of the labs.  Then it's up to you to follow the instructions below to complete the labs.

**Module 1:** Running The Code In a Cloud9 Environment  
**Module 2:** Build a Docker anf Push to Amazon ECR  
**Module 3:** Create a First AWS Batch Job  
**Module 4:** Manage Retries  
**Module 5:** Run AWS Batch Jobs on Spot Instances  
**Module 6:** Create Complex Workflows with Step Functions  

<a name="conventions"></a>
### Conventions:  
Throughout README files, we provide commands for you to run in the Cloud9 IDE. These commands will look like this: 

<pre>
$ docket build -t <b><i>simulator</i></b>
</pre>


<a name="begin"></a>
## Let's start

Move on to [**Module 1: Running The Code In a Cloud9 Environment**](./Module1-RunningTheCodeinTheCloud9/Module1.md)




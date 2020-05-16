# Module 1 : Running the code in the Cloud9 IDE

In this module, you will use the Cloud9 IDE to download the simulation code and running the application locally in the IDE. 

As an optional step, you can test out Cloud9's debugging features

## Instructions

1. In the terminal window of the cloud9 environment, enter to downloaded Module1 directory with:

	```bash
	cd workshop/Module1-RunningTheCodeinTheCloud9
	```
	
1. Create a virtual environment for python 3.6. (There are also many other benefits of using [virtualenv](https://virtualenv.pypa.io/en/stable/) in managing python dependencies. )

	```bash
	virtualenv venv
	source venv/bin/activate
	```
		
1. Now take a look at the main source code file, `simulator.py` in this folder. 

	To do this, you can use the code editor of the Cloud9 IDE. Go to the left hand **Environment** tool bar, click into the `workshop` folder, and then into `Module1-RunningTheCodeinTheCloud9`
		
1. As you can see in the beginning of the file, multiple external libraries such as `pandas_datareader` and `numpy` are used in the code. We need to install the dependencies so we can run the code locally

	The required libraries are listed in `requirements.txt`, also in this folder
	
	Back to the terminal window at bottom of screen, install the required dependencies by typing:
	
	```
	pip install -r requirements.txt 
	```

1. You are now ready to run the code locally 

	As you can see in the `simulator.py` code, you can run this program by passing in different parameters. 
	
	In the terminal, try the following: 
	
	Show help message with `-h`
	
	```
	python simulator.py -h
	```

	Specify number of iterations to simulate: 
	
	```
	python simulator.py --iterations 50
	```
	
	You should see a csv generated as the result of the simulation run. We didn't specify a S3 bucket to upload the results to, so it's stored in the local file directory: 
	
	<img src="images/local-results-with-ls.png" width="80%">
	
	
	If you see an error, don't worry. Sometimes downloading the ticker data from Yahoo finance fail, so just rerun the script a few times.
	
1. You can open the resulting csv to see what it looks like. 
	
1.	Now, run the simulator in by specifying number of iterations and the bucket name you created in Module 1:
	
	```
	python simulator.py --iterations 50 --s3_bucket <replace_with_your_bucket_name>
	```

	When it succeeds, you should see the output like this:
	
	You can then go to the [S3 console](https://console.aws.amazon.com/s3/home) and verify the results have been uploaded to S3
	

## Next step

Move on to [**Module 2: Build a docker container**](./Module2-BuildDockerAndPushToAmazonECR/Module2.md)

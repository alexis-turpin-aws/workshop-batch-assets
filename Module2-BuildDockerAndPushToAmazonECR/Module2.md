# Module 2: Build a docker container and push to Amazon ECR

Now we have tested the application, it's time to build a docker container! 

To build a docker container, we need to create a **Dockerfile**, a text document that contains all the commands to assemble an image. See more reference on Dockerfile [here](https://docs.docker.com/engine/reference/builder/#environment-replacement)

## Build Docker 

1. Create a file in the Cloud9 IDE by going to **File** --> **New File**

1. Paste in below as the content for the Dockerfile:

	```
	FROM python:3.6.3
	COPY simulator.py simulator.py
	COPY requirements.txt requirements.txt
	RUN pip install -r requirements.txt
	CMD ["python",  "simulator.py", "--iterations", "10"]
	```
	
	Take a moment to review at how a simple Docker file is written: 
	
	**FROM \<image>:\<tag>**  Sets the base image. Must be first instruction in Dockerfile.

	**COPY \<src> \<dest>** Copies new files or directories from \<src> and adds them to the filesystem of the container at the path \<dest>. 

	**RUN \<command>** Executes any commands in a new layer on top of the current image and commit the results.

	**CMD [“exec”, “param1”, “param2”]** Sets the command to be executed when running the image.

1. Save the file as **Dockerfile** in the `Module1-RunningTheCodeinTheCloud9/` folder - **Make sure to captalize the D!**

1. In the terminal:

	Ensure you are in the `Module1-RunningTheCodeinTheCloud9/` directory:

	```
	cd ~/environment/workshop/Module1-RunningTheCodeinTheCloud9
	```

	Build the docker image with tag `simulator`
	
	```
	docker build -t simulator .    
	```
	
1. You should now see your newly built docker image by running:

	```
	docker images
	```

1. You can run the docker image locally by 

	```
	docker run -t simulator
	```
	
	When you don't specify additional commands, the container will run the `CMD` argument specified in our **Dockerfile** by default. When it's done executing all the commands, the container will exit. 
	
1. You can override the command the container runs by doing `docker run -t simulator <command to run instead of default>`

	For example, the below will run the `ls` command in the container
	
	```
	docker run -t simulator ls
	```
	
	The below will run the `python simulator.py --iterations 20 --stock AAPL` command in the container

	```
	docker run -t simulator python simulator.py --iterations 20 --stock AAPL
	```
	
	Or the below will run the container and give you interactive shell access to it:

	```
	docker run -it simulator /bin/bash
	```
	
	For example: 
	
	To exit out of the interactive bash, type: 
	
	```
	exit
	```
	
1. You may notice if try running the docker container with a s3 bucket, the run will fail: 

	```
	 docker run  -i simulator  python simulator.py --iterations 40 --s3_bucket <your-bucket-name>
	```
	
	this is because the S3 SDK is trying to look for credentials to sign the request with. Typically in a dev environment, your credentials are stored in `~/.aws` folder, but your container doesn't have access to it. 
	
	Add the `-v ~/.aws:/root/.aws` flag to the command like below to mount the `~/.aws` folder from the host machine into the `/root/.aws` folder in the container:
	
	```
	 docker run  -v ~/.aws:/root/.aws  -it simulator  python simulator.py --iterations 50 --s3_bucket <your-bucket-name>
	```
	
	Luckily, when you run the container using AWS Batch, the credential problem is automatically handled by assigning an IAM role to the container. See more info on that [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)
	
	
## Push the docker container to Amazon ECR

1. Go to the [ECR Console](https://us-east-2.console.aws.amazon.com/ecs/home?region=us-east-2#/repositories) (You can reach there also by looking for "ECS" or "container service" in the list of services from the console home page and go to ECR **Repositories** 
	
1. Click on **Create repository**

1. Give a name, such as `repository-simulator` to your repo, then click **Next Step**
	
1. Build, tag and push your Docker Image with **View Push Commands** button in the repository console page provided. Follow the commands (a-d) to login to the registry, build the container, tag the container and push to the repo. 
	
1. After the push succeeds, now if you check your ECR repository, you should see the pushed docker image


## Next step

Move on to [**Module 3: Create a First AWS Batch Job**](../Module3-CreateFirstAWSBatchJob/Module3.md)

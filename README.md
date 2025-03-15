Step 1:
Install all the dependencies required to run..

Install Docker Desktop or Docker Hub as the backend code will be pushed into the docker container 
The backend used in FastApi first runn the docker file and then run the frontend 


commands to build the container and upload the code:

docker build -t your_username/your_image_name:tag .

docker images

docker login

docker push your_username/your_image_name:tag

Then check your docker desktop application if container has been created..

Step 2:

Run your frontend 

cd my-app
npm start 


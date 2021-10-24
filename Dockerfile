#Create a ubuntu base image with python 3 installed.
# Use the Python3.7.2 image
FROM python:3.7.2-stretch

EXPOSE 5000/tcp

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt


# TODO remove this line when sqlite is replace by other DB
RUN python db.py

CMD [ "python", "./run.py" ]

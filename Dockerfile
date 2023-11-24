# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app
RUN pip install requests
# Copy the local application files into the container
COPY calculator.py .
COPY usdinr.py .
# Define the command to run the application
ENTRYPOINT ["python"]

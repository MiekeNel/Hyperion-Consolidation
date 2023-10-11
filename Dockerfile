# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for non-interactive installation
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

# Create and set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container at /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app/
COPY . /app/

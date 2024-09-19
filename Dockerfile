# Use the official Python image from the DockerHub
FROM python:3.12

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Set the working directory in docker
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose port
EXPOSE 8000

# Assign permissions to the django.sh file
RUN chmod 755 ./django.sh

# entrypoint to run the django.sh file
ENTRYPOINT ["/app/django.sh"]
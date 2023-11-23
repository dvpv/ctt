# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable
ENV TODO_APP_DATABASE_URI "mysql+pymysql://backend:j9#8j8sdfa97hsdf7hIAHSDf@localhost/todo"

# Run app.py when the container launches
CMD ["python", "app.py"]

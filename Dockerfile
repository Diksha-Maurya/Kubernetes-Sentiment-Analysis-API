# Dockerfile

# Using the official Python image as a base
FROM python:3.9-slim

# Setting the working directory inside the container
WORKDIR /app

# Copying the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying the rest of the application code
COPY . .

# Exposing the port the app runs on
EXPOSE 5000

CMD ["python", "app.py"]
# Use an official Python runtime as a base image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /imcooking

# Copy the dependencies file to the working directory
COPY requirements.txt /imcooking/

# Install any dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /imcooking/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "./imcooking/manage.py", "runserver", "0.0.0.0:8000"]
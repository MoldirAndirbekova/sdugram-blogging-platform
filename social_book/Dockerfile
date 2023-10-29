# Use an official Python runtime as the base image
FROM python:3.8

# Set environment variables for Python and Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application source code to the container
COPY . .

# Expose the port that the Django application will listen on
EXPOSE 8000

# Start the Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]

# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in environment.yml
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "testenv", "/bin/bash", "-c"]

# Run the application
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "testenv", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
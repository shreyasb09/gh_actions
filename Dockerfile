FROM python:3.9-slim

WORKDIR /app

# Copy the ieg_package directory into the Docker image
COPY ./ieg_package /app/ieg_package

# Copy the cpcost.py script into the Docker image
COPY ./gh_actions/cpcost.py /app/cpcost.py

# Set the PYTHONPATH to include the ieg_package directory
ENV PYTHONPATH=/app/ieg_package

ENTRYPOINT ["python", "/app/cpcost.py"]

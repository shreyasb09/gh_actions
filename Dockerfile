FROM python:3.9

# Install AWS CLI
RUN apt-get update && \
    apt install -y awscli

# Set the AWS_DEFAULT_REGION environment variable
ENV AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}

# Set the AWS credentials environment variables
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_SESSION_TOKEN=${AWS_SESSION_TOKEN}

# Set the PIP_INDEX_URL environment variable
ENV PIP_INDEX_URL=${PIP_INDEX_URL}

# Copy the pip.conf file
COPY pipconf/pip.conf /root/.pip/pip.conf

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy your application code
COPY cpcost.py /app/cpcost.py

# Run the Python script in the background
CMD python /app/cpcost.py

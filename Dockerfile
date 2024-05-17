# Build stage
FROM python:3.9-slim as build
WORKDIR /app

# Install AWS CLI
RUN apt-get update && apt-get install -y awscli

# Configure AWS credentials
RUN aws configure set region ap-south-1

# Log in to AWS CodeArtifact
RUN mkdir -p ~/.pip
RUN aws codeartifact login --tool pip --repository ieg --domain amgbeta --domain-owner 109667701036 --region ap-south-1
RUN echo "[global]\nindex-url = https://aws:${CODEARTIFACT_AUTH_TOKEN}@amgbeta-109667701036.d.codeartifact.ap-south-1.amazonaws.com/pypi/ieg/simple/\nextra-index-url = https://pypi.org/simple/" > ~/.pip/pip.conf

# Install ieg package
RUN pip install ieg==0.1.0

# Copy cpcost.py
COPY gh_actions/cpcost.py /app/cpcost.py

# Final stage
FROM python:3.9-slim
WORKDIR /app
COPY --from=build /app/cpcost.py /app/cpcost.py
CMD ["python", "cpcost.py"]

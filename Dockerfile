# Install AWS CLI
RUN apt-get update && apt-get install -y awscli

# Install pip
RUN apt-get install -y python3-pip

# Assume the IAM role
ENV AWS_ROLE_ARN=arn:aws:iam::109667701036:role/cpcostiota-role
RUN aws configure set role_arn $AWS_ROLE_ARN && \
    aws configure set source_profile default

# Configure AWS CLI to use the assumed role
RUN mkdir -p ~/.aws && \
    echo -e "[default]\nrole_arn = ${AWS_ROLE_ARN}\ncredential_source = Ec2InstanceMetadata" > ~/.aws/config

# Your other Dockerfile instructions...

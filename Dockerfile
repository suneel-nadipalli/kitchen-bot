FROM public.ecr.aws/lambda/python:3.11

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire directory into the container
COPY . .

# Set the command to start Lambda handler
CMD ["main.handler"]

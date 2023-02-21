############### Environment Build Image ################
# The basis is a "heavy" (~1GB, ~500M compressed) image with all the necessary
# libraries for building modules
FROM snakepacker/python:all as builder

# Create a virtual environment and update pip
RUN python3.10 -m venv /usr/share/python3/app
RUN /usr/share/python3/app/bin/pip install -U pip

# We install dependencies separately to cache, during the subsequent assembly
# Docker skip this step if requirements.txt doesn't change
COPY requirements*.txt /tmp/
RUN /usr/share/python3/app/bin/pip install -Ur /tmp/requirements.txt

########################### Final look ############################
# As a basis we take a "light" (~100M, ~50M compressed) image with python
FROM snakepacker/python:3.10 as api

# Copy the finished virtual environment into it from the builder container
COPY --from=builder /usr/share/python3/app /usr/share/python3/app
COPY ./app /app
ENV PATH="/usr/share/python3/app/bin:${PATH}"
ENV PYTHONPATH="$PYTHONPATH"
COPY ./app /app

# Set the default command to run on container startup
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]

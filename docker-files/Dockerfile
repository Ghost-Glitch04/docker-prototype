# Base image — Ubuntu 24.04 LTS
# This is always the first instruction. Everything builds on top of this layer.
FROM ubuntu:24.04

# Install packages in a single RUN to keep it one layer.
# - apt-get update refreshes the package index first
# - apt-get install -y installs without prompting
# - rm -rf /var/lib/apt/lists/* removes the index cache to keep the layer small
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container.
# All subsequent COPY, RUN, and CMD instructions operate relative to this path.
WORKDIR /app

# Copy hello.sh from the host (relative to build context) into /app/ inside the container.
COPY hello.sh .

# Make the script executable.
RUN chmod +x hello.sh

# Default command — runs when the container starts.
# JSON array form is preferred: avoids spawning an extra shell process.
CMD ["./hello.sh"]

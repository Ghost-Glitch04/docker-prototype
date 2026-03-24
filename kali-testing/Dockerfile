# Base Image — Kali Linux Rolling
# This is always the first instruction. Everything builds on top of this layer.
FROM kalilinux/kali-rolling:latest

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install base utilities and development tools
# - apt-get update refreshes the package index first
# - apt-get install -y installs without prompting
# - --no-install-recommends skips suggested packages to keep the image small
# - rm -rf /var/lib/apt/lists/* removes the index cache to keep the layer small
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    vim \
    nano \
    ssh \
    zsh \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Network Scanners, Reconnaissance, Vulnerability Scanning, and Enumeration
RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap \
    ffuf \
    whatweb \
    nuclei \
    nikto \
    enum4linux \
    smbclient \
    hydra \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Web Exploitation Tools
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gobuster \
#     sqlmap \
#     burpsuite \
#     && rm -rf /var/lib/apt/lists/*

# Install packages - Binary/Pwn
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gdb \
#     radare2 \
#     ltrace \
#     binwalk \
#     && rm -rf /var/lib/apt/lists/*
# RUN pip3 install pwntools

# Set Working Directory to /CTF
WORKDIR /CTF

# Start zsh shell when the container starts
CMD ["/bin/zsh"]
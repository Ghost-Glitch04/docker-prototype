# Base Image — Kali Linux Rolling
# This is always the first instruction. Everything builds on top of this layer.
FROM kalilinux/kali-rolling:latest

# Install packages in a single RUN to keep it one layer.
# Install curl and wget for downloading files from the internet.
# - apt-get update refreshes the package index first
# - apt-get install -y installs without prompting
# - rm -rf /var/lib/apt/lists/* removes the index cache to keep the layer small
RUN apt-get update && apt-get install -y \
    curl wget \
    && rm -rf /var/lib/apt/lists/*

# Install packagers - Development tools
RUN apt-get update && apt-get install -y \
    python3 git \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Network Scanners and Initial Reconnaissance Tools
RUN apt-get update && apt-get install -y \
    nmap fuff whatweb nuclei \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Vulnerability Scanners
RUN apt-get update && apt-get install -y \
    nikto openvas \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Enumeration and Exploitation Tools
RUN apt-get update && apt-get install -y \
    enum4linux smbclient hydra \
    && rm -rf /var/lib/apt/lists/*
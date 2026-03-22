# X11 Forwarding variant — renders live on the host display
# Run with: xhost +local:docker
#           docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix turtle-spiral:v1
FROM python:3.12-slim

# python3-tk — tkinter, required by turtle
# No Xvfb or Ghostscript needed — we use the host's X server directly
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY spiral.py .

CMD ["python3", "spiral.py"]

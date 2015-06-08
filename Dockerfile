FROM python:2.7-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends skytools3-ticker && \
    rm -rf /var/lib/apt/lists/*

COPY entrypoint.py /

CMD ["python2.7", "/entrypoint.py"]

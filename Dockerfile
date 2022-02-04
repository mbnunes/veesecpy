FROM alpine

RUN apk add --no-cache python3 ffmpeg
RUN mkdir -p /veesecpy/data
WORKDIR /veesecpy

COPY main.py /veesecpy
COPY config.json /veesecpy

CMD ["python3", "main.py"]
FROM fedora:39

WORKDIR /app
COPY ./protobuf/src /app/protos

RUN dnf4 update -y \
    && dnf4 install -y wget unzip python3 python3-pip \
    && ln /usr/bin/python3 /usr/bin/python \
    && python3 -m pip install --upgrade pip setuptools \
    && wget https://github.com/protocolbuffers/protobuf/releases/download/v25.2/protoc-25.2-linux-x86_64.zip \
    && unzip protoc-25.2-linux-x86_64.zip -d protoc \
    && mv protoc/bin/* /usr/local/bin/ \
    && mv protoc/include/* /usr/local/include/ \
    && python -m pip install grpcio-tools

RUN groupadd -g 1000 appuser \
    && useradd -r -u 1000 -g appuser appuser \
    && mkdir gen \
    && chown -R 1000:1000 /app/gen \
    && chmod 755 /app/gen

USER 1000

RUN whoami && id && ls -la /app/gen
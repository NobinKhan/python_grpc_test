FROM fedora:39

# Build time arguments
ARG UID
ARG GID

# Update the package list, install wget unzip python3-pip
RUN dnf4 update -y \
    && dnf4 install -y wget unzip python3-pip \
    && ln /usr/bin/python3 /usr/bin/python

# Create a non-root user, and grant password-less sudo permissions
RUN groupadd --gid $GID nonroot \
    && useradd --uid $UID --gid $GID -r nonroot \
    && echo 'nonroot ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers \
    && wget https://github.com/protocolbuffers/protobuf/releases/download/v25.2/protoc-25.2-linux-x86_64.zip \
    && unzip protoc-25.2-linux-x86_64.zip -d protoc \
    && mv protoc/bin/* /usr/local/bin/ \
    && mv protoc/include/* /usr/local/include/ \
    && python -m pip install grpcio-tools

# Set the non-root user as the default user
USER nonroot

# Set the working directory
WORKDIR /home/nonroot/app

# Copy files into the container and set the appropriate permissions
COPY --chown=nonroot:nonroot ./protobuf/src /home/nonroot/app/protos
RUN mkdir /home/nonroot/app/gen \
    && chmod -R 755 /home/nonroot/app /home/nonroot/app/gen \
    && chown nonroot:nonroot /home/nonroot/app /home/nonroot/app/gen \
    && python -m grpc_tools.protoc -I./protos/ --python_out=./gen/ --pyi_out=./gen/ --grpc_python_out=./gen/ ./protos/helloworld.proto
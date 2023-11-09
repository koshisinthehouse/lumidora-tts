FROM ghcr.io/arunk140/serve-piper-tts:latest

WORKDIR /go/src/app
COPY voices /go/src/app/models
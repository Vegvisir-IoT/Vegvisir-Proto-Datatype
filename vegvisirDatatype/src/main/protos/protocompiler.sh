#!/bin/bash

# Compiles protobuf files at once
# Author: Gloire Rubambiza
# Version: 3/11/2019

protoc -I=. --python_out=. vegvisirlower.proto
protoc -I=. --python_out=. common.proto
protoc -I=. --python_out=. charlottewrapper.proto
protoc -I=. --python_out=. vegvisirprotocol.proto

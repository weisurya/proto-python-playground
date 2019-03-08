#!/usr/bin/env bash
protoc --python_out=. simple.proto
protoc --python_out=. enum_example.proto
protoc --python_out=. complex.proto
#!/usr/bin/env bash

set -e

local_repo=${LOCAL_REPO?Variable LOCAL_REPO is required}
model_name=${MODEL_NAME?Variable MODEL_NAME is required}
tokenizer_name=${TOKENIZER_NAME?Variable TOKENIZER_NAME is required}

docker build --build-arg "MODEL_NAME=$model_name" --build-arg "TOKENIZER_NAME=$tokenizer_name" -t "$local_repo" .

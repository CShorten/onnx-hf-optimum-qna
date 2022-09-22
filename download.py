#!/usr/bin/env python3

from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from optimum.onnxruntime import ORTModelForQuestionAnswering

import os
import sys

model_name = os.getenv('MODEL_NAME')
tokenizer_name = os.getenv('TOKENIZER_NAME') # different tokenizer name for the ORT models

if model_name is None or model_name == "":
    print("Fatal: MODEL_NAME is required")
    sys.exit(1)

if tokenizer_name is None or tokenizer_name == "":
    print("Fatal: TOKENIZER_NAME is required")
    sys.exit(1)

print("Downloading model {} from huggingface model hub".format(model_name))

model = ORTModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

model.save_pretrained('./models/model')
tokenizer.save_pretrained('./models/model')

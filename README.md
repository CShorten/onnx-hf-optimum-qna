# qna-transformers-models
The inference container for the qna module

## Documentation

Documentation for this module can be found [here](https://weaviate.io/developers/weaviate/current/reader-generator-modules/qna-transformers.html).

## Build Docker container

```
LOCAL_REPO="qna-transformers" MODEL_NAME="optimum/roberta-base-squad2" TOKENIZER_NAME="deepset/roberta-base-squad2" ./cicd/build.sh
```

### Local development

Installing `cmake` and `pkg-config` may be required to successfully install all requirements
```
brew install cmake
brew install pkg-config
```

### Downloading model

Run command: 
```
MODEL_NAME=optimum/roberta-base-squad2 TOKENIZER_NAME=deepset/roberta-base-squad2 ./download.py
```

### Running local server

Run command:
```
python3 -m uvicorn app:app --host 0.0.0.0 --port 8000    
```

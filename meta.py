from transformers import AutoConfig

class Meta:
    config: AutoConfig

    def __init__(self, model_path):
        # temporary fix, not sure if the ONNX models have AutoConfigs
        self.config = AutoConfig.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

    def get(self):
        return {
            'model': self.config.to_dict()
        }

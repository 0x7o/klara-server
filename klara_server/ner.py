from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from config import Config


class Ner:
    def __init__(self, config: Config):
        self.tokenizer = AutoTokenizer.from_pretrained(
            config.get_config("ner_model_name")
        )
        self.model = AutoModelForTokenClassification.from_pretrained(
            config.get_config("ner_model_name")
        ).to(config.get_config("ner_device"))
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def get_entities(self, text):
        entities = self.nlp(text)
        return entities
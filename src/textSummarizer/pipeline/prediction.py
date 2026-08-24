from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline



class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {
            "length_penalty": 1.0,
            "num_beams": 5,
            "max_length": 64,
            "min_length": 10,
            "early_stopping": True
        }

        model = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model_path
        )

        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )

        inputs = {
            key: value.to(model.device)
            for key, value in inputs.items()
        }

        summary_ids = model.generate(
            **inputs,
            **gen_kwargs
        )

        print("Dialogue:")
        print(text)

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )

        print("\nModel Summary:")
        print(summary)

        return s

        
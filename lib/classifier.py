from transformers import pipeline

model_id = "isaacaderogba/tonality"
classifier = pipeline("text-classification", model=model_id)

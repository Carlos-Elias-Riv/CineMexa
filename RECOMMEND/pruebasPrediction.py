from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-es-en")
src = "es"
trg = "en"
model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
sample_text = "Las vicisitudes de tres amiguitos se mezclan con el nacimiento del Piccolo Coro del Instituto Antoniano de Bologna, de la mano de Mariele Ventre, una profesora de música apasionada y dulce."
batch = tokenizer([sample_text], return_tensors="pt")
generated_ids= model.generate(**batch)
translated = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(translated)



newtokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
newmodel = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

emotion = pipeline('sentiment-analysis', 
                    model='arpanghoshal/EmoRoBERTa')

emotion_labels = emotion(translated)
print(emotion_labels)



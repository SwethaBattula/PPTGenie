from google import genai

client = genai.Client(api_key="AIzaSyDB7HvQVINQC6DbEoCBtPshrCDq8uAw7Ks")
models = client.models.list()
for m in models:
    print(m.name)

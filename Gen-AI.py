from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter your prompt: ")

result = generator(
    prompt,
    max_length=100,
    num_return_sequences=1
)

print("\nGenerated Text:")
print(result[0]["generated_text"])

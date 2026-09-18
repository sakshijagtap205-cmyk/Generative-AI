from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

print("AI Story Generator")
topic = input("Enter a story topic: ")

prompt = "Write a short story about " + topic

result = generator(
    prompt,
    max_length=200,
    num_return_sequences=1,
    do_sample=True
)

print("\nGenerated Story:\n")
print(result[0]["generated_text"])
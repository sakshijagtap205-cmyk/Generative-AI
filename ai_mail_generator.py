from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

print("AI Email Generator")

purpose = input("Enter email purpose: ")
tone = input("Enter tone (formal/friendly): ")

prompt = f"Write a {tone} professional email about {purpose}."

result = generator(
    prompt,
    max_length=150,
    num_return_sequences=1,
    do_sample=True
)

print("\nGenerated Email:\n")
print(result[0]["generated_text"])
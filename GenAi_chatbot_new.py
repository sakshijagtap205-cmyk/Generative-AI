
from transformers import pipeline

# Load GPT-2 text generation model
print("Loading GPT-2 model... Please wait.")

chatbot = pipeline(
    "text-generation",
    model="gpt2"
)

# E-commerce chatbot function
def customer_support(user_message):

    message = user_message.lower()

    # Predefined domain-specific responses
    if "order" in message or "tracking" in message:
        prompt = (
            "Customer support assistant: "
            "To track your order, please visit the "
            "My Orders section and check the tracking status. "
            "Customer: " + user_message +
            "\nAssistant:"
        )

    elif "return" in message or "refund" in message:
        prompt = (
            "Customer support assistant: "
            "You can request a return or refund through "
            "the Returns section. Check the seller's return policy. "
            "Customer: " + user_message +
            "\nAssistant:"
        )

    elif "product" in message or "price" in message:
        prompt = (
            "Customer support assistant: "
            "Please check the product page for price, "
            "features, availability, and specifications. "
            "Customer: " + user_message +
            "\nAssistant:"
        )

    elif "complaint" in message or "problem" in message:
        prompt = (
            "Customer support assistant: "
            "We are sorry for the inconvenience. "
            "Please provide your order ID and describe the issue "
            "so our support team can help. "
            "Customer: " + user_message +
            "\nAssistant:"
        )

    elif "hello" in message or "hi" in message:
        prompt = (
            "Customer support assistant: "
            "Hello! Welcome to our online store. "
            "How may I help you today? "
            "Customer: " + user_message +
            "\nAssistant:"
        )

    else:
        prompt = (
            "Customer support assistant: "
            "I can help with orders, returns, products, "
            "refunds, and complaints. "
            "Customer: " + user_message +
            "\nAssistant:"
        )

    # Generate response using GPT-2
    result = chatbot(
        prompt,
        max_new_tokens=45,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.6,
        pad_token_id=50256
    )

    # Extract generated response
    generated_text = result[0]["generated_text"]
    response = generated_text.split("Assistant:")[-1].strip()

    return response


# Main chatbot loop
print("\n===== E-Commerce GPT Chatbot =====")
print("Type 'exit' to stop the chatbot.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Chatbot: Thank you for visiting our store!")
        break

    answer = customer_support(user_input)
    print("Chatbot:", answer)

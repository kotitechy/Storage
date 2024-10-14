def chat_bot(key, question="hi"):

    from huggingface_hub import InferenceClient

    client = InferenceClient(api_key=key)
    response_parts=[]
    for message in client.chat_completion(
    	model="mistralai/Mistral-7B-Instruct-v0.3",
    	messages=[{"role": "user", "content": f"{question}?"}],
    	max_tokens=500,
    	stream=True,
    ):
        # print(message.choices[0].delta.content, end="")
        response_parts.append(message.choices[0].delta.content)
    # Join all parts into a single string
    full_response = ''.join(response_parts)
    return full_response

# key="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"
# model="google-bert/bert-large-uncased-whole-word-masking-finetuned-squad"
# question="who is priminister of india"

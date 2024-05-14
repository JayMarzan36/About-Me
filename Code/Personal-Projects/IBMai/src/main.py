import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "path to model"

tokenizer = AutoTokenizer.from_pretrained(model_path, padding_side= "left")

model = AutoModelForCausalLM.from_pretrained(model_path, device_map="cpu")

model.eval()


test_Input = "Can you write code to find the max value in a list of numbers."

chat = [{"role": "system", "content": "You are a helpfull coding assistant"}, 
        { "role": "user", "content": test_Input}]
# tokenizer.chat_template = chat

formatted_chat = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat])


input_tokens = tokenizer(formatted_chat, return_tensors="pt")

#
    
output = model.generate(**input_tokens, max_new_tokens= 100)
output = tokenizer.batch_decode(output)

for i in output:
    print(i)
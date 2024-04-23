import torch
from pprint import pprint
from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM


model_name_new = "D:/huggingface_model/meta-llama/Llama-2-7b-chat-hf"  # Your path

base_model = AutoModelForCausalLM.from_pretrained(
    'meta-llama/Llama-2-7b-chat-hf',
    trust_remote_code=True,
    device_map="auto",
    torch_dtype=torch.float16,   # optional if you have enough VRAM
)
tokenizer = AutoTokenizer.from_pretrained('meta-llama/Llama-2-7b-chat-hf')
_ = base_model.cuda()

q = "What is the NVDA stock market trend forecast ?"
encoded_new = tokenizer(q, return_tensors = "pt")["input_ids"]
generated_new = base_model.generate(encoded_new.cuda())[0, encoded_new.shape[-1]:]
decoded_new = tokenizer.decode(generated_new, skip_special_tokens=True).strip()
pprint(decoded_new)
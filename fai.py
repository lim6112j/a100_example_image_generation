from diffusers import AutoPipelineForText2Image
import torch
import sys
prompt = sys.argv[1]
filename = sys.argv[2]
pipeline = AutoPipelineForText2Image.from_pretrained(
    'black-forest-labs/FLUX.1-dev', torch_dtype=torch.bfloat16).to('cuda')
pipeline.load_lora_weights('openfree/flux-chatgpt-ghibli-lora',
                           weight_name='flux-chatgpt-ghibli-lora.safetensors')
image = pipeline(prompt).images[0]
image.save(filename)

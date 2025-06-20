import torch
from diffusers import FluxPipeline

from huggingface_hub import login
import sys

hf_token = ""
login(hf_token, add_to_git_credential=True)

# pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16).to("cuda")
pipe = FluxPipeline.from_pretrained(
    "lodestones/Chroma", torch_dtype=torch.bfloat16).to("cuda")
generator = torch.Generator(device="cuda").manual_seed(0)
prompt = sys.argv[1]
filename = sys.argv[2]

# Generate the image using the GPU
image = pipe(
    prompt,
    guidance_scale=0.0,
    num_inference_steps=4,
    max_sequence_length=256,
    generator=generator
).images[0]

image.save(filename)

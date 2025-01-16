import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(torch.cuda.current_device()))
print("Is CUDA available:", torch.cuda.is_available())
print("Current device:", torch.cuda.current_device())
print("CUDA version:", torch.version.cuda)
print(torch.__version__)
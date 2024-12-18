import os
import torch

# Number of GPUs available. Use 0 for CPU mode.
ngpu = torch.cuda.device_count()

# device = torch.device("cuda" if (torch.cuda.is_available() and ngpu > 0) else "cpu")

# Number of workers for dataloader
# NUM_WORKERS = os.cpu_count()
NUM_WORKERS = torch.cuda.device_count()

# Batch size during training
batch_size = 128

# Spatial size of training images. All images will be resized to this
#   size using a transformer.
image_size = 64

# Number of channels in the training images. For color images this is 3
nc = 3

# Size of z latent vector (i.e. size of generator input)
nz = 100

# Size of feature maps in generator
ngf = 64

# Size of feature maps in discriminator
ndf = 64

# Number of training epochs
num_epochs = 3

# Learning rate for optimizers
lr = 0.0002

# Beta1 hyperparameter for Adam optimizers
beta1 = 0.5
# -*- coding: utf-8 -*-
"""00_pytorch_exercises.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pPqR-4Xx2fwrvoYc1WWxdtJQrwdPn45U
"""

import torch

# 1. Documentation reading - A big part of deep learning (and learning to code in general) is getting familiar with the documentation of a certain framework you're using. We'll be using the PyTorch documentation a lot throughout the rest of this course. So I'd recommend spending 10-minutes reading the following (it's okay if you don't get some things for now, the focus is not yet full understanding, it's awareness). See the documentation on torch.Tensor and for torch.cuda.

#2. Create a random tensor with shape (7, 7).
torch.rand(7,7)
# -*- coding: utf-8 -*-
"""00_pytorch_fundamentals_video.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vxMQTU0lzdcjnTvHVhRtZIzMimbBN-fR

## 00.pytorch.PyTorch Fundamentals

> Indented block



Resource notebook:https://www.learnpytorch.io/00_pytorch_fundamentals/

If a question https://github.com/mrdbourke/pytorch-deep-learning/discussions
"""

print("Hello Im excited to learn pytorch")

!nvidia-smi

import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(torch.__version__)

"""## Intro to tensors

###creating tensors

PyTorch tensors are created using 'torch.Tensor()'-https://pytorch.org/docs/stable/tensors.html
"""

# scalar
scalar = torch.tensor(7)
scalar

scalar.ndim

#Get tensor back as Python int
scalar.item()

#vector
vector = torch.tensor([7,7])
vector

vector.ndim

vector.shape

# matrix
MATRIX = torch.tensor([[7,8],
             [9,10]])
MATRIX

MATRIX.ndim

# FIRST DIMENSION
MATRIX[0]

MATRIX[1]

MATRIX.shape

#TENSOR
TENSOR = torch.tensor([[[1,2,3],
            [3,4,5],
            [2,6,7]]])
TENSOR

TENSOR.ndim

# ONE 3BY3 TENSOR
# 第一个1 代表outer bracket，第二个数字3代表3个框住数字的框，第3个数字3代表一个最小框内的3个数字
TENSOR.shape

TENSOR[0]

TENSOR[1]

TENSOR[2]

"""#random tensors

Why random tensors?

Random tensors are important  because the way many neural networks learn is that they start with tensors full of random numbers and then adjust those random numbers to better represent the data

'Start with random numbers -> look at data -> update random numbers->look at data -> update random numbers'

Torch.random tensors - https://pytorch.org/docs/stable/generated/torch.rand.html
"""

#Create a random tensor of size(3,4)
random_tensor = torch.rand(3,4)
random_tensor

random_tensor.ndim

#Create a random tensor with similar shape to an image tensor
random_image_size_tensor = torch.rand(size=(3,224,224)) # height,width, color channels (R, G, B)
random_image_size_tensor.shape,random_image_size_tensor.ndim
# torch.rand(3,4)=torch.rand(size=(3,4))

"""### Zeros and ones"""

#Create a tensor of all zeros
zeros = torch.zeros(3,4)
zeros

zeros*random_tensor

#Create a tensor of all ones
ones = torch.ones(3,4)
ones

ones.dtype

random_tensor.dtype

"""### Creating a range of tensors and tensors-like"""

# Use torch.range() and get deprecated message, use torch.arange()
one_to_ten = torch.arange(start=1,end=11,step=1)
one_to_ten

#creating tensors like
ten_zeros = torch.zeros_like(input=one_to_ten)
ten_zeros

"""### Tensor datatypes

**Note:** Tensor datatypes is one of the 3 big issues/errors with PyTorch& Deep learning
1. Tensor not right datatype
2. Tensor not right shape
3. Tensor not on the right device

Precision in computing-
https://en.wikipedia.org/wiki/Precision_(computer_science)

"""

# Float 32 tensor
float_32_tensor = torch.tensor([3.0,6.0,9.0],
                dtype=None,# What datatype is the tensor,(e.g. float32 or float16)可以被定义为torch.float16等等；matter with precision in computing
                device="cuda",# What device is your tensor on
                requires_grad=False)# Whether or not to track gradients with this tensors operation
float_32_tensor

float_32_tensor.dtype

float_16_tensor = float_32_tensor.type(torch.float16)
float_16_tensor # check the tensor datatype

float_16_tensor*float_32_tensor#此处没有出现error，但其他dtype不match的情况可能会error

int_32_tensor = torch.tensor([3,6,9],dtype=torch.int32)# no dots to make it float
int_32_tensor

float_32_tensor * int_32_tensor

"""### Getting information from tensors (tensor attributes)

1. Tensor not right datatype - to get datatype from a tensor, can use'tensor.dtype'
2. Tensor not right shape - to get shape from a tensor, can use 'tensor.shape'
3. Tensor not on the right device - to get device from a tensor, can use 'tensor.device'
"""

# create a tensor
some_tensor = torch.rand(3,4)
some_tensor

some_tensor.size, some_tensor.shape #attribute doesn't have a bracket

some_tensor.size

some_tensor.size() #function has its bracket behind

# Find out details about some tensor
print(some_tensor)
print(f"Datatype of tensor:{some_tensor.dtype}")
print(f"Shape of tensor:{some_tensor.shape}")
print(f"Device tensor is on:{some_tensor.device}")

"""from ast import Add
### Manipulating Tensors(tensor operations)

Tensor operations include:
* Addition
* Subtraction
* Multiplication(element-wise)
* Division
* Matrix multiplication
"""

# Create a tensor and add 1- to it
tensor = torch.tensor([1,2,3])
tensor+10

# Multiply tensor by 10
tensor*10

tensor

# Subtract 10
tensor-10

# Try out PyTorch in-built functions
torch.mul(tensor,10)

torch.add(tensor,10)

"""### Matrix multiplication

Two main ways of performing multiplication in neural networkd and deep learning

1 Element-wise multiplication
2 Matrix multiplication(dot product)

More information on multiplying matrixes-
https://www.mathsisfun.com/algebra/matrix-multiplying.html
"""

# Element wise multiplication
print(tensor,"*",tensor)
print(f"Equals:{tensor*tensor}")

# Matrix multiplication
torch.matmul(tensor,tensor)

tensor

#matrix multiplication by hand
1*1+2*2+3*3

# Commented out IPython magic to ensure Python compatibility.
# %%time
# value=0
# for i in range(len(tensor)):
#  value +=tensor[i]*tensor[i]
# print(value)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# torch.matmul(tensor,tensor)
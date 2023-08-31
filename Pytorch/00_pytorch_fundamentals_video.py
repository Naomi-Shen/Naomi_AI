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

float_32_tensor * int_32_tensor # error

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

There are 2 main rules that performing matrix multiplication needs to satisfy:
1. The **inner dimensions** must match:
* only'(3,2)@(2,3)'will work but not (3,2)@(3,2)
2. The resulting matrix has the shape of the **outing dimensions**:
* '(2,3)*(3,2)'->'(2,2)'
* '(3,2)*(2,3)'->'(3,2)'
"""

torch.rand(3,2).shape

# Element wise multiplication
print(tensor,"*",tensor)
print(f"Equals:{tensor*tensor}")

# Matrix multiplication
torch.matmul(tensor,tensor)


tensor @tensor

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


"""### One of the most common errors in deep learning:shape errors

check:http://matrixmultiplication.xyz/

"""

# Shapes for matrix multiplication
tensor_A = torch.tensor([[1,2],
              [3,4],
              [5,6]])
tensor_B = torch.tensor([[7,10],
              [8,11],
              [9,12]])

# torch.matmul = torch.mm
torch.mm(tensor_A,tensor_B)

tensor_A.shape,tensor_B.shape

"""To fix the tensor shape issues, we can manipulate the shape of one of our tensors using **teanspose**

A **transpose** switches the axes or dimensions of a given tensor
"""

tensor_B.T,tensor_B.T.shape

tensor_B,tensor_B.shape

torch.mm(tensor_A,tensor_B.T)

torch.mm(tensor_A,tensor_B.T).shape

# The matrix multiplication operation works when tensor_B is transposed
print(f"Original shapes: tensor_A ={tensor_A.shape}, tensor_B ={tensor_B.shape}")
print(f"New shapes: tensor_A ={tensor_A.shape}(same shape as above),tensor_B.T ={tensor_B.T.shape}")
print(f"Multiplying:{tensor_A.shape}@{tensor_B.shape}<- inner dimensions must match")
print("Output:\n")
output = torch.matmul(tensor_A,tensor_B.T)
print(output)
print(f"\nOutput shape:{output.shape}")

"""## Finding the min, max,mean, sum, etc (tensor aggregation)"""

# Create a tensor
x = torch.arange(1,100,10)
x,x.dtype

# Find the min
torch.min(x),x.min()

# Find the max
torch.max(x),x.max()

# Find the mean - note: the torch.mean() function requires a tensor of float32 datatype to work
torch.mean(x.type(torch.float32)),x.type(torch.float).mean()

# Find the sum
torch.sum(x),x.sum()

"""## Finding the positional min and max"""

# Find the position in tensor that has the minimum value with argmin() -> returns index position of target tensor where the minimum value occurs
x.argmin()

x[0]

#  Find the position of maximum value
x.argmax()

x[9]

x

"""## Reshaping, stacking, squeezing and unsqueezing tensors

* Reshaping - reshapes an input tensor to a defined shape
* View - return a view of an input of certain shape but keep the same memory as the original tensor
* Stacking - combine multiple tensors on top of each other(vstack) or side by side (hstack)
* Squeeze - remove all "1" dimensions from a tensor
* Unsqueeze - add a "1" dimension to a target tensor
* Permute - return a view of the input with dimensions permuted(swapped) in a certain way
"""

# Create a tensor
import torch
x = torch.arange(1.,10.)
x,x.shape

# Add an extra dimension
x_reshaped = x.reshape(9,1)
x_reshaped,x_reshaped.shape

# Change the view
z = x.view(1,9)
z,z.shape

# Changing z changes x(because a view of a tensor shares the same memory as the original input)
z[:,0] = 5
z,x

# Stack tensors on top of each other
x_stacked = torch.stack([x,x,x,x], dim=0)
x_stacked

# Stack tensors on top of each other
x_stacked = torch.stack([x,x,x,x], dim=1)
x_stacked

# Note:vstack using dimension=0,hstack using dimension=1

# torch.squeeze() - removes all single dimensions from a target tensor
print(f"Previous tensor:{z}")
print(f"Previous shape:{x_reshaped.shape}")

# Remove extra dimensions from x_reshaped
z_squeezed = z.squeeze()
print(f"\nNew tensor:{z_squeezed}")
print(f"New shape:{z_squeezed.shape}")

# torch.unsqueeze() - adds a single dimension to a target tensor at a specific dim (dimension)
print(f"Previous target:{z_squeezed}")
print(f"Previous shape:{z_squeezed.shape}")

# Add an extra dimension with unsqueeze
z_unsqueezed = z_squeezed.unsqueeze(dim=0）#could be 1 or any number
print(f"\nNew tensor:{z_unsqueezed}")
print(f"New shape:{z_unsqueezed.shape}")

# torch.permute - rearrange the dimensions of a target tensor in a specified order
x_original = torch.rand(size = (224,224,3)) #[height,width,colour_channels]

# Permute the original tensor to rearrange the axis (or dim) order
x_permuted = x_original.permute(2,0,1) #shifts axis 0->1,1->2,2->0

print(f"Previous shape:{x_original.shape}")
print(f"New shape:{x_permuted.shape}") #[colour_channels,height,width]

x_original[0,:,:] 

x_original[0,0,0] =728218
x_original[0,0,0], x_permuted[0,0,0]

"""## Indexing (selecting data from tensors)

Indexing with PyTorch is similar to indexing with Numpy.
"""

# Create a tensor
import torch
x = torch.arange(1,10).reshape(1,3,3) #从1开始到10-1=9
x,x.shape

# Let's index on our new tensor
x[0]

# Let's index on the middle bracket(dim=1)
x[0][0] # whose effect is the same as x[0,0]

# Let's index on the most inner bracket (last dimension)
x[0][0][0]
x[0][1][1]

# You can also use ":" to select "all" of a target dimension
x[:,0]

# Get all values of 0th and 1st dimensions but only index 1 of 2nd dimension
x[:,:,1]
# result would be tensor([[2, 5, 8]])

# Get all values of the 0 dimension but only the 1 index value of 1st and 2nd dimension
x[:,1,1] # result:tensor([5])
#comparison: x[0,1,1] result:tensor(5)

# Get index 0 of 0th and 1st dimension and all values of 2nd dimension
x[0,0,:] #result:tensor([1, 2, 3])
#comparison x[0][0],result:tensor([1, 2, 3])

# Index on x to return 9
# Index on x to return 3,6,9
x

x[:,2,2] #result:tensor([9])

x[0,2,2] #result:tensor(9)

x[:,:,2]
def AND_gate(x1, x2):
    # Weights and threshold for AND gate
    w1, w2, theta = 1, 1, 1.5
    # Calculate the weighted sum
    weighted_sum = x1 * w1 + x2 * w2
    # Apply the threshold
    return 1 if weighted_sum >= theta else 0

# Test the AND gate
print("AND Gate:")
print(AND_gate(0, 0))  # Output: 0
print(AND_gate(0, 1))  # Output: 0
print(AND_gate(1, 0))  # Output: 0
print(AND_gate(1, 1))  # Output: 1

def OR_gate(x1, x2):
    # Weights and threshold for OR gate
    w1, w2, theta = 1, 1, 0.5
    # Calculate the weighted sum
    weighted_sum = x1 * w1 + x2 * w2
    # Apply the threshold
    return 1 if weighted_sum >= theta else 0

# Test the OR gate
print("OR Gate:")
print(OR_gate(0, 0))  # Output: 0
print(OR_gate(0, 1))  # Output: 1
print(OR_gate(1, 0))  # Output: 1
print(OR_gate(1, 1))  # Output: 1


def NAND_gate(x1, x2):
    # Weights and threshold for NAND gate
    w1, w2, theta = -1, -1, -1.5
    # Calculate the weighted sum
    weighted_sum = x1 * w1 + x2 * w2
    # Apply the threshold
    return 1 if weighted_sum >= theta else 0

# Test the NAND gate
print("NAND Gate:")
print(NAND_gate(0, 0))  # Output: 1
print(NAND_gate(0, 1))  # Output: 1
print(NAND_gate(1, 0))  # Output: 1
print(NAND_gate(1, 1))  # Output: 0

def NOR_gate(x1, x2):
    # Weights and threshold for NOR gate
    w1, w2, theta = -1, -1, -0.5
    # Calculate the weighted sum
    weighted_sum = x1 * w1 + x2 * w2
    # Apply the threshold
    return 1 if weighted_sum >= theta else 0

# Test the NOR gate
print("NOR Gate:")
print(NOR_gate(0, 0))  # Output: 1
print(NOR_gate(0, 1))  # Output: 0
print(NOR_gate(1, 0))  # Output: 0
print(NOR_gate(1, 1))  # Output: 0

def XOR_gate(x1, x2):
    # First layer: NAND and OR gates
    nand_output = NAND_gate(x1, x2)
    or_output = OR_gate(x1, x2)
    # Second layer: AND gate
    return AND_gate(nand_output, or_output)

# Test the XOR gate
print("XOR Gate:")
print(XOR_gate(0, 0))  # Output: 0
print(XOR_gate(0, 1))  # Output: 1
print(XOR_gate(1, 0))  # Output: 1
print(XOR_gate(1, 1))  # Output: 0


def AND_gate_custom(x1, x2, w1=1, w2=1, theta=1.5):
    weighted_sum = x1 * w1 + x2 * w2
    return 1 if weighted_sum >= theta else 0

# Experimenting with different weights
print("AND Gate with custom weights:")
print(AND_gate_custom(0, 0, 1, 1, 1.5))  # Output: 0
print(AND_gate_custom(0, 1, 1, 1, 1.5))  # Output: 0
print(AND_gate_custom(1, 0, 1, 1, 1.5))  # Output: 0
print(AND_gate_custom(1, 1, 1, 1, 1.5))  # Output: 1


def AND_gate_bipolar(x1, x2):
    w1, w2, theta = 1, 1, 1.5
    weighted_sum = x1 * w1 + x2 * w2
    return 1 if weighted_sum >= theta else -1  # Bipolar output

# Test the bipolar AND gate
print("Bipolar AND Gate:")
print(AND_gate_bipolar(-1, -1))  # Output: -1
print(AND_gate_bipolar(-1, 1))   # Output: -1
print(AND_gate_bipolar(1, -1))   # Output: -1
print(AND_gate_bipolar(1, 1))    # Output: 1


import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR input and output
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize weights
np.random.seed(42)
weights_input_hidden = np.random.rand(2, 2)
weights_hidden_output = np.random.rand(2, 1)

# Learning rate
learning_rate = 0.1
final_output = None
# Training the network
for epoch in range(10000):
    # Forward propagation
    hidden_input = np.dot(X, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, weights_hidden_output)
    final_output = sigmoid(final_input)

    # Backpropagation
    error = y - final_output
    d_output = error * sigmoid_derivative(final_output)
    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights
    weights_hidden_output += hidden_output.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden) * learning_rate

# Test the network after training
print("Predicted Output:")
print(final_output)

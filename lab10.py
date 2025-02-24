# Initialize weights and bias
w1, w2, b = 0.5, 0.5, -1

# Activation function (Step function)
def activate(x):
    return 1 if x >= 0 else 0

# Training the perceptron
def train_perceptron(inputs, desired_outputs, learning_rate, epochs):
    global w1, w2, b
    for epoch in range(epochs):
        total_error = 0
        for i in range(len(inputs)):
            A, B = inputs[i]
            target_output = desired_outputs[i]

            # Calculate the output
            output = activate(w1 * A + w2 * B + b)

            # Calculate the error
            error = target_output - output

            # Update weights and bias
            w1 += learning_rate * error * A
            w2 += learning_rate * error * B
            b += learning_rate * error

            # Accumulate the total error
            total_error += abs(error)

        # Stop training if the error is zero
        if total_error == 0:
            break

# Inputs and desired outputs for AND gate
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
desired_outputs = [0, 0, 0, 1]

# Training parameters
learning_rate = 0.1
epochs = 100

# Train the perceptron
train_perceptron(inputs, desired_outputs, learning_rate, epochs)

# Test the trained perceptron
for i in range(len(inputs)):
    A, B = inputs[i]
    output = activate(w1 * A + w2 * B + b)
    print(f"Input: ({A}, {B})  Output: {output}")

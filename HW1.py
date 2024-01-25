import numpy as np

class Neuron:
    def __init__(self, weights, threshold):
        """
        Initialize the neuron with specified weights and threshold.
        :param weights: List of weights for the inputs.
        :param threshold: Threshold for activation.
        """
        self.weights = weights
        self.threshold = threshold

    def activate(self, inputs):
        """
        Activate the neuron with given inputs.
        :param inputs: Binary inputs to the neuron.
        :return: 1 if the neuron activates, 0 otherwise.
        """
        # Calculate weighted sum of inputs
        weighted_sum = sum(w * i for w, i in zip(self.weights, inputs))

        # Activation function: check if weighted sum is greater than threshold
        return 1 if weighted_sum >= self.threshold else 0
    
def train(self, training_inputs, expected_output, learning_rate=0.1):
        """
        Train the neuron using the perceptron learning rule.
        :param training_inputs: List of training inputs.
        :param expected_output: Expected output for the training inputs.
        :param learning_rate: Rate at which the weights are adjusted.
        """
        actual_output = self.activate(training_inputs)
        error = expected_output - actual_output

        # Adjust weights and threshold based on the error
        self.weights = [w + (learning_rate * error * x) for w, x in zip(self.weights, training_inputs)]
        self.threshold -= learning_rate * error


# Example usage
if __name__ == "__main__":
    # Create a neuron with specified weights and threshold
    weights = [0.5, 0.5, -0.5]  # Example weights
    threshold = 0.5            # Example threshold

    neuron = Neuron(weights, threshold)

    # Test the neuron with a set of inputs
    inputs = [1, 1, 0]  # Example inputs
    output = neuron.activate(inputs)
    print(f"Output: {output}")
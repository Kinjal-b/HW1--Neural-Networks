# HW1--Neural-Networks

## Non Programming Assignment

#### 1. How does natural neuron work?

Answer.

A natural neuron, also known as a biological neuron, is the basic working unit of the brain and the nervous system. It is a specialized cell responsible for processing and transmitting information through electrical and chemical signals. Here's a simplified description of how a natural neuron works:

Structure of a Neuron: A typical neuron consists of a cell body (soma), dendrites, and an axon. The cell body contains the nucleus and cytoplasm. Dendrites are tree-like structures that receive signals from other neurons and conduct them towards the cell body. The axon is a long, thin fiber that transmits signals away from the cell body to other neurons, muscles, or glands.

Receiving Signals: The process starts when a neuron receives signals from other neurons. These signals are received at the synapses (the junctions between neurons) on the dendrites or sometimes directly on the cell body. These incoming signals can be either excitatory (increasing the likelihood that the neuron will fire) or inhibitory (decreasing the likelihood of the neuron firing).

Integration of Signals: Inside the neuron, the received signals are summed up. This summation is a complex process, involving both spatial summation (combining signals received at different locations on the neuron) and temporal summation (combining signals received at different times).

Action Potential (Firing): If the combined strength of the excitatory signals minus the inhibitory signals is above a certain threshold, the neuron becomes activated and generates an electrical impulse known as an action potential. This action potential is an all-or-nothing response and travels along the axon.

Signal Transmission: The action potential travels down the axon to the axon terminals, where it triggers the release of neurotransmitters. These neurotransmitters are chemicals that cross the synaptic gap and bind to receptors on the adjacent neuron, thus transmitting the signal onward.

Resetting: After firing, the neuron goes through a refractory period during which it cannot fire again immediately. This is a reset mechanism that ensures signals travel in one direction and allows the neuron to prepare for the next signal.

Neurotransmitter Clearance: Finally, neurotransmitters in the synaptic gap are either broken down or reabsorbed, clearing the synapse and readying it for the next signal.

The process of neurons communicating through electrical impulses and chemical signals is fundamental to all neural activities, including thought, feeling, movement, and the functioning of the senses. The human brain contains approximately 86 billion neurons, each capable of forming thousands of synaptic connections, making the neural network incredibly complex and powerful.

#### 2. How does natural neuron transmit signal to other neurons?

Answer.

Natural neurons transmit signals to other neurons through a process that involves both electrical and chemical steps. This process is fundamental to neuronal communication and forms the basis of how the brain and nervous system operate. Here's a step-by-step overview of how this transmission occurs:

Generation of an Action Potential: The process begins in the transmitting neuron (presynaptic neuron) with the generation of an action potential, which is an electrical impulse. This occurs when the neuron is activated and the electrical charge inside the neuron becomes more positive, reaching a threshold level.

Propagation of the Action Potential: The action potential travels along the axon of the neuron towards the axon terminals. This movement is facilitated by the opening and closing of voltage-gated ion channels along the axon's membrane.

Reaching the Synapse: The axon terminal of the presynaptic neuron is in close proximity to the dendrite or cell body of the next neuron (postsynaptic neuron). The point of contact is known as a synapse. However, the neurons do not physically touch; there is a small gap known as the synaptic cleft.

Release of Neurotransmitters: When the action potential reaches the axon terminal, it triggers the release of chemicals known as neurotransmitters. These neurotransmitters are stored in small sac-like structures called synaptic vesicles.

Crossing the Synaptic Cleft: The neurotransmitters are released into the synaptic cleft and diffuse across this gap to the postsynaptic neuron.

Binding to Receptors: On the surface of the postsynaptic neuron, there are specific receptors. The neurotransmitters bind to these receptors, much like a key fits into a lock. The binding of neurotransmitters to receptors causes changes in the postsynaptic neuron.

Postsynaptic Potential: The binding of neurotransmitters can result in either excitatory or inhibitory signals in the postsynaptic neuron. If the signal is excitatory, it may bring the postsynaptic neuron closer to firing its own action potential. If it is inhibitory, it may move the neuron further from firing.

Signal Termination: Finally, the signal is terminated so that the neurotransmitters do not continue to affect the postsynaptic neuron indefinitely. This termination can occur through various mechanisms, such as the breakdown of neurotransmitters in the synaptic cleft, their reabsorption into the presynaptic neuron, or their diffusion away from the synapse.

This process of synaptic transmission allows neurons to communicate rapidly and efficiently, enabling complex functions such as movement, perception, thinking, and feeling. The precise patterns of synaptic connections and the types of neurotransmitters released are fundamental to the functioning of the brain and the nervous system.

#### 3. Describe the McCulloch and Pitts model of artificial neuron?

Answer.

The McCulloch and Pitts model of an artificial neuron, developed by Warren McCulloch and Walter Pitts in 1943, is a simplified representation of a biological neuron and one of the earliest conceptualizations of neural networks. This model laid the groundwork for future developments in artificial intelligence and computational neuroscience. Here's a description of the model:

Binary Inputs and Outputs: In the McCulloch and Pitts neuron model, neurons are conceptualized as simple logic gates with binary inputs and outputs. Inputs can either be 0 (representing an inactive neuron) or 1 (representing an active neuron).

Weights: Each input connection to the neuron has a weight associated with it. In the original model, these weights are often considered to be either excitatory (positive) or inhibitory (negative), but in the simplest form, the weights are typically standardized (for example, all weights could be 1).

Summation and Thresholding: The neuron calculates the weighted sum of its inputs. This sum is then compared to a predefined threshold. The original McCulloch and Pitts model used a simple linear summation without any multiplicative weights.

Activation Function: If the total weighted sum of the inputs exceeds the threshold, the neuron 'fires' and outputs a 1; if not, it outputs a 0. This binary step function is the activation function in the McCulloch and Pitts model.

Simplified Representation of Neural Activity: The McCulloch and Pitts model simplifies the complex electrochemical processes of biological neurons into binary states, capturing the essence of neural activation and synaptic transmission in a way that can be mathematically and computationally modeled.

Networks of Neurons: Multiple McCulloch and Pitts neurons can be connected together to form a network, allowing for the representation of more complex logical functions. The model demonstrated that networks of simple units could compute a wide variety of logical relationships and was influential in the development of later neural network architectures.

While the McCulloch and Pitts model is a highly simplified version of real neural activity, lacking many features of actual neurons (like varying synaptic strengths, temporal dynamics, and more complex activation functions), it was significant in showing that computational models could capture fundamental aspects of neural processing and paved the way for the development of more sophisticated neural network models in artificial intelligence.
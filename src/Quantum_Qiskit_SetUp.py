# Install packages

# Colab
# !pip3 install qiskit
# !pip3 install qiskit-ibm-runtime
# !pip3 install qiskit[visualization]

# Local machine (Just install the requirements.txt file)
# pip install qiskit
# pip install qiskit-ibm-runtime
# pip install qiskit[visualization]

# Import the packages
from qiskit import QuantumCircuit

# Adding 2 qubits
qc = QuantumCircuit(2)

# Adding a Hadamard gate on qubit 0, which puts it in superposition
# Convert the qubit to superposition
qc.h(0)

# Add a CNOT (also called CX) gate to entangle the two qubits (also know as Conditional Not)
qc.cx(0, 1)

# Map the qubits to classical measurement
qc.measure_all()

# Visualize the circuit
qc.draw("mpl")

# Another way to create the same circuit
qc2 = QuantumCircuit(2)
qc2.h(1)
qc2.cx(0, 1)
qc2.measure_all()
qc2.draw("mpl")

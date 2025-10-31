# Import the packages
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Create a Quantum Circuit with one qubit
qc = QuantumCircuit(1)
qc.h(0)

# Use the Aer backend simulator
sim = Aer.get_backend('aer_simulator')

# Save the statevector
qc.save_statevector()

# Execute the quantum circuit
result = sim.run(qc).result()

# Retrieve the current statevector
state = result.get_statevector()

# Visualize the statevector on a Bloch Sphere. The qubit |0> has been put in superposition |+>
fig = plot_bloch_multivector(state)
fig

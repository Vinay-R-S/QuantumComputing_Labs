# Practical 2 - Single Qubit Gates and Bloch Sphere Visulatization

# Import the packages
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# 1. Use the Aer backend simulator - Simulate Quantum circuit on local machine
# 2. Save the current state-vector
# 3. Execute the quantum circuit
# 4. Retrieve the current state vector
# 5. Visualize the statevector on a Bloch Sphere.

# Creating a Quantum Circuit with 4 qubits
qc = QuantumCircuit(4)

sim = Aer.get_backend("aer_simulator")
qc.save_statevector()
result = sim.run(qc).result()
state = result.get_statevector()

fig = plot_bloch_multivector(state)

# Applying Single Qubit Gates: H, X, Y, Z
qc_gates = QuantumCircuit(4)

qc_gates.h(0)
qc_gates.x(1)
qc_gates.y(2)
qc_gates.z(3)

sim = Aer.get_backend("aer_simulator")
qc_gates.save_statevector()
result = sim.run(qc_gates).result()
state_gates = result.get_statevector()

fig = plot_bloch_multivector(state_gates)

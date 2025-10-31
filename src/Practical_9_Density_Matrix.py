# Practical 9 - Density Matrix

# Import the packages
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a 2-qubit bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

# Save the density matrix at the end of the circuit
qc.save_density_matrix()

# Initialize Aer simulator with density matrix method
simulator = AerSimulator(method='density_matrix')

tcirc = transpile(qc, simulator)

result = simulator.run(tcirc).result()

# Extract the density matrix from the result
density_matrix = result.data(0)['density_matrix']

print("Density matrix of the Bell state:")
print(density_matrix)

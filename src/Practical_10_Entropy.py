# Practical 10 - Entorpy

# Import the packages
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import DensityMatrix, partial_trace, entropy

# Create a 2-qubit Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx( 0, 1 )
qc.save_density_matrix()

# Simulate
sim = AerSimulator( method = "density_matrix" )
result = sim.run(qc).result()
dm = result.data(0)[ "density_matrix" ]

# Create DensityMatrix object of full system
rho = DensityMatrix( dm )

# Compute reduced density matrix of qubit-0 by tracing out qubit-1
reduced_rho = partial_trace( rho, [1] )

# Calculate von Neumann entropy of the reduced state
"""
Important detail:
The Bell state as a whole two-qubit system is pure, so von Neumann entropy of
the entire density matrix is 0 (or numerical zero).
The subsystems (each single qubit reduced density matrices) are mixed and have
non-zero entropy (~1 bit).
How to correctly see the entropy of 1 bit for the Bell state:
Compute the reduced density matrix of a single qubit by tracing out the other
qubit, then calculate the entropy of this reduced state.
Partial Trace function operation effectively "ignores" or "discards" the
subsystem(s) in the list from the full quantum state, providing the quantum
state of the remaining subsystems alone with all correlations accounted for.
"""

S_whole = entropy ( rho, base = 2 )
S_single = entropy( reduced_rho, base = 2 )

# Entropy should be close to 0 for the whole 2-qubit system
print( "Entropy of whole two qubits system (bits):", S_whole )

# Entropy should be close to 1 indicating mixed state
print( "Entropy of reduced single qubit (bits):", S_single )

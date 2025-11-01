# Quantum Teleportation of One Qubit (Ideal Unitary Simulation)
# This program demonstrates the perfect teleportation of an arbitrary quantum state
# from Qubit 0 (Alice) to Qubit 2 (Bob) using a Statevector Simulator.

# Import necessary Qiskit packages
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import state_fidelity, partial_trace, Statevector
import numpy as np

# -----------------------------------------------------------
# 1. PREPARE THE ARBITRARY STATE |psi> TO BE TELEPORTED

# Create an arbitrary single-qubit state (|psi>) on Qubit 0.
initial_qc = QuantumCircuit(1)
# Example: Apply H gate and T gate to create a non-trivial state: |psi> = T |+>
initial_qc.h(0)
initial_qc.t(0)

# Convert the circuit to a Statevector for comparison later
initial_state = Statevector.from_instruction(initial_qc)
print(f"--- Input State |psi> Preparation ---")
# Note: In Colab, the LaTeX output may not render visually, but it provides the vector data.
print(f"Initial State (Qubit 0):")
print(initial_state.draw(output='text')) # Use draw method instead of to_latex

# -----------------------------------------------------------
# 2. QUANTUM TELEPORTATION CIRCUIT CONSTRUCTION

# Create the main circuit with 3 qubits (Q0, Q1, Q2)
# Q0: State to be teleported (Alice's side)
# Q1: Alice's half of the Bell pair (Alice's side/Ancilla)
# Q2: Bob's half/Destination qubit (Bob's side)
qc = QuantumCircuit(3)

# Initialize Qubit 0 with the state to be teleported (|psi>)
qc.initialize(initial_state, 0)
qc.barrier(range(3))


# Create the Bell Pair (Entangled channel) on Qubits 1 and 2
# This is the "EPR Pair" shared between Alice (Q1) and Bob (Q2)
qc.h(1)
qc.cx(1, 2)
qc.barrier(range(3))


# Perform the Bell State Measurement (BSM) operations on Qubits 0 and 1 (Alice's side)
# 1. CNOT from Q0 to Q1
qc.cx(0, 1)
# 2. Hadamard on Q0
qc.h(0)
qc.barrier(range(3))


# Bob's Conditional Corrections (Unitary Equivalent)
# In an ideal simulation, we replace classical feedback (based on measurement results)
# with controlled unitary gates from Q0 and Q1 onto the destination Q2.

# Apply X correction controlled by Qubit 1
qc.cx(1, 2)
# Apply Z correction controlled by Qubit 0
qc.cz(0, 2)
qc.barrier(range(3))

# -----------------------------------------------------------
# 3. SIMULATION AND FIDELITY CALCULATION

# Save the final statevector after all operations
qc.save_statevector()

# Use the Statevector simulator
sim = AerSimulator(method='statevector')
qc_compiled = transpile(qc, sim)

# Run the simulation
result = sim.run(qc_compiled).result()
# Get the final 3-qubit statevector
final_state_3q = result.get_statevector(qc)

# Trace out the unneeded qubits (Q0 and Q1, the control/ancilla qubits)
# to isolate the final state of the destination qubit (Q2).
# We trace out indices 0 and 1. The remaining qubit is Q2 (index 2).
rho_out = partial_trace(final_state_3q, [0, 1])

# Calculate the fidelity between the original input state and the teleported state
# Fidelity measures how close the two states are (1.0 is perfect match).
fidelity = state_fidelity(initial_state, rho_out)

print(f"\n--- Results ---")
print(f"Destination State (Qubit 2 Density Matrix):")
print(rho_out.draw(output='text')) # Use draw method instead of to_latex
print(f"Fidelity (Input |psi> vs Output Qubit 2): {fidelity:.8f}")

# The fidelity should be very close to 1.0 (perfect teleportation)
if np.isclose(fidelity, 1.0):
    print("\nConclusion: Quantum teleportation was successful! Fidelity is near 1.0.")
else:
    print("\nConclusion: Teleportation failed. Fidelity is low.")

print("\n--- Full Circuit Diagram ---")
print(qc.draw('text'))

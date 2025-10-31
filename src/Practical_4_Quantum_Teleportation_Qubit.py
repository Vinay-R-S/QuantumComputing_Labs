# Practical 4 - Quantum Teleportation

# Import the packages
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import state_fidelity, partial_trace, Statevector
from qiskit.visualization import plot_histogram

# Step 1: Prepare the initial state to teleport on qubit 0
initial_qc = QuantumCircuit(1)
initial_qc.h(0)
initial_qc.t(0)
initial_state = Statevector.from_instruction(initial_qc)

# Step 2: Create quantum circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Step 3: Prepare qubit 0 to be teleported (T gate)
qc.h(0)
qc.t(0)

# Step 4: Create entangled Bell pair (qubits 1 & 2)
qc.h(1)
qc.cx(1, 2)

# Step 5: Teleportation protocol
qc.cx(0, 1)
qc.h(0)

# Step 6: Measure qubits 0 & 1 and store results
qc.measure([0, 1], [0, 1])

# Step 7: Conditional corrections based on measurement outcomes
qc.cx(1, 2)
qc.cz(0, 2)

# Step 8: Save the statevector before measuring qubit 2
qc.save_statevector()

# Step 9: Measure the destination qubit (qubit 2)
qc.measure(2, 2)

# Step 10: Remove final measurements for statevector output
qc_no_meas = qc.remove_final_measurements(inplace=False)

# Step 11: Create AerSimulator with statevector method
sim = AerSimulator(method='statevector')
qc_compiled = transpile(qc_no_meas, sim)

# Step 12: Run simulation and get statevector
result = sim.run(qc_compiled).result()
final_state = result.get_statevector()

# Step 13: Partial trace to get qubit 2 state
rho_out = partial_trace(final_state, [0, 1])

# Step 14: Calculate fidelity
fidelity = state_fidelity(initial_state, rho_out)
print(f"Fidelity between input and teleported qubit: {fidelity:.1f}")

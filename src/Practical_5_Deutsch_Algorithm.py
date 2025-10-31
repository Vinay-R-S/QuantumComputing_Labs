# Pratical 5 - Desutsch Algorithm

# Import the packages
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def constant_oracle_0():
    """Oracle for f(x) = 0 (constant) - identity"""
    oracle = QuantumCircuit(2)
    return oracle

def constant_oracle_1():
    """Oracle for f(x) = 1 (constant) - flips the output qubit"""
    oracle = QuantumCircuit(2)
    oracle.x(1)
    return oracle

def balanced_oracle_x():
    """Oracle for f(x) = x (balanced) - CNOT gate"""
    oracle = QuantumCircuit(2)
    oracle.cx(0, 1)
    return oracle

def deutsch_algorithm(oracle):
    # Create a 2-qubit, 1-classical-bit circuit
    qc = QuantumCircuit(2, 1)
    # Initialize second qubit to |1>
    qc.x(1)
    # Apply Hadamard on both qubits
    qc.h([0, 1])
    qc.barrier() # add a barrier for readability
    # Apply the oracle
    qc.compose(oracle, inplace=True) # append the oracle circuit to qc
    qc.barrier()
    # Apply Hadamard on the first qubit
    qc.h(0)
    # Measure the first qubit
    qc.measure(0, 0)
    return qc

# Select oracle to test; change to test different oracles
oracle = balanced_oracle_x()

# Create the Deutsch algorithm circuit with the chosen oracle
circuit = deutsch_algorithm(oracle)
print(circuit.draw())

# Use Qiskit Aer simulator
simulator = AerSimulator()

# Execute the circuit on the simulator with 100 shots
result = simulator.run(circuit, shots=100).result()
counts = result.get_counts()

print("Measurement results:", counts)

# Plot the results
hist_fig = plot_histogram(counts)
hist_fig

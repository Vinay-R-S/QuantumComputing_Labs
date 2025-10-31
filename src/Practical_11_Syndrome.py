# Practical 11 - Syndrome

# Import the packages
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import DensityMatrix, partial_trace, entropy

def bit_flip_code_with_syndrome(bit_flip_error = "Flase", error_qubit = 1):
    """
    Three-qubit bit-flip code with syndrome measurement.
    
    Encoding a logical qubit into three physical qubits, introducing a bit-flip error
    on one of the qubits, and measuring the syndrome using two ancillary qubits.
    """
    
    #  5 qubits: 3 data qubits + 2 ancilla for syndrome measurement
    qc = QuantumCircuit(5,2)
    
    # Prepare logical qubit in |+> for demonstration
    qc.h(0)
    qc.barrier()
    
    # Encoding: copy qubit 0 state to qubits 1 and 2
    qc.ex(0,1)
    qc.ex(0,2)
    qc.barrier()
    
    if bit_flip_error:
        qc.x(error_qubit)
    qc.barrier()
    
    # Syndrome measurement:
    # Check parity between qubits 0 and 1, store in ancilla 3
    qc.cx(0,3)
    qc.cx(1,3)
    
    # Check parity between qubits 0 and 2, store in ancilla 4
    qc.cx(1,4)  
    qc.cx(2,4)
    
    # Measure ancillary qubits to get syndrome bits
    qc.measure([3,4], [0,1])
    
    return qc

def phase_flip_code_with_syndrome(phase_flip_error = "False", error_qubit = 1):
    """
    Three-qubit phase-flip code with syndrome measurement.
    
    Applies Hadamard before and after the bit-flip code to convert phase-flip errors
    into bit-flip errors, allowing the same syndrome measurement approach.
    """
    
    #  5 qubits: 3 data qubits + 2 ancilla for syndrome measurement
    qc = QuantumCircuit(5,2)
    
    # Prepare logical qubit in |+> for demonstration
    qc.h(0)
    qc.barrier()
    
    # Encoding: with repetation code
    qc.cx(0,1)
    qc.cx(0,2)
    qc.barrier()
    
    # Hadamard to switch the phase-flip basis
    qc.h([0,1,2])
    
    # Apply phase-flip error simulated bt Z gate on specified qubit
    if phase_flip_error:
        qc.z(error_qubit)
    qc.barrier()
    
    # Hadamard to change back
    qc.h([0,1,2])
    
    # Syndrome measurement:
    # Check parity between qubits 0 and 1, store in ancilla 3
    qc.ex(0,3)
    qc.ex(1,3)
    qc.cx(1,4)
    qc.cx(2,4)
    
    qc.measure
    
    # Check parity between qubits 0 and 2, store in ancilla 4
    qc.ex(1,4)

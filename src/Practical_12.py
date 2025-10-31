# Practical 12: Density Matrices, Entropy, Quantum Error Correction, and Interferometry

# Import the packages
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

# 📍 Density Matrix of Bell State
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

qc.save_density_matrix()

sim = AerSimulator(method = "density_matrix")

tcirc = transpile(qc, sim)
res = sim.run(tcirc).result()
density_matrix = res.data(0)['density_matrix']

print ("Density matrix of bell state:")
print(density_matrix)

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import DensityMatrix, partial_trace, entropy

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
qc.save_density_matrix()

sim = AerSimulator( method = "density_matrix" )
result = sim.run(qc).result()
dm = result.data(0)[ "density_matrix" ]

# Create DensityMatrix object of full system
rho = DensityMatrix( dm )

# Compute reduced density matrix of qubit-0 by tracing out qubit-1
reduced_rho = partial_trace( rho, [1] )

# Calculate von Neumann entropy of the reduced state

S_whole = entropy (rho, base = 2)
S_single = entropy( reduced_rho,base = 2)

print("Entropy of which two qubits system (bits): ", S_whole)
print("Entropy of which two qubits system (bits): ", S_single)


from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 📍 Entropy code with syndrome measurement
def bit_flip_code_with_syndrome( bit_flip_error = False, error_qubit = 1):
  qc = QuantumCircuit( 5,2 )
  qc.h(0)
  qc.barrier()

  qc.cx( 0,1 )
  qc.cx( 0,2 )
  qc.barrier()

  if bit_flip_error:
    qc.x( error_qubit )
  qc.barrier()

  #syndrome measurement
  qc.cx( 0,3 )
  qc.cx( 1,3 )

  qc.cx( 1,4 )
  qc.cx( 2,4 )

  qc.measure( [3,4] ,[1,2] )

def bit_flip_code_with_syndrome( bit_flip_error = False, error_qubit = 1):
  qc = QuantumCircuit( 5,2 )
  qc.h(0)
  qc.barrier()

  qc.cx( 0,2 )
  qc.cx( 0,2 )
  qc.barrier()

  qc.h([0,1,2])

  if bit_flip_error:
    qc.x( error_qubit )
  qc.barrier()

  qc.h([0,1,2])

  #syndrome measurement
  qc.cx( 0,3 )
  qc.cx( 1,3 )
  qc.cx( 1,4 )
  qc.cx( 2,4 )

  qc.measure( [3,4] ,[1,2] )

  Simulator = AerSimulator()

  qc_phase_flip = phase_flip_code_with_syndrome(phase_flip_error = True, error_qubit = 1)
  compiled_phase = transpile( qc_phase_flip, simulator )
  result_phase_flip = simulator.run( compiled_phase_flip, shots = 1024 ).result()
  counts_phase_flip = result_phase_flip.get_counts()

  fig, axs = plt.subplots(1,2, figsize = (12,4))
  plot_histogram( counts_bit_flip,
                 ax = axs[0],
                  title = "Phase flip code syndrome")

  plt.show()

# 📍 Mach-Zehnder Interferometer Circuit
def mach_zehnder_interferometer(phase_shift = 0):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.rz(phase_shift, 0)
    qc.h(0)
    qc.measure(0, 0)
    return qc

simulator = AerSimulator()

phase_shifts = np.linspace(0, 2 * np.pi, 10)
results = []
legend_labels = []
for phase_shift in phase_shifts:
    qc = mach_zehnder_interferometer(phase_shift = phase_shift)
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots = 1024)
    counts = job.result().get_counts()
    results.append(counts)
    legend_labels.append(f"Phase shift: {phase_shift:.2f}")
    print(f"Phase shift: {phase_shift:.2f}")

phase_shifts = np.linspace(0, 2 * np.pi, 10)
results = []
legend_labels = []

for phase in phase_shifts:
  qc = mach_zehnder_interferometer(phase_shift = phase)
  compiled_circuit = transpile(qc, simulator)
  job = simulator.run(compiled_circuit, shots = 1024)
  counts = job.result().get_counts()
  results.append(counts)
  legend_labels.append(f"Phase shift: {phase:.2f}")
  print(f"Phase shift: {phase:.2f} -> Counts: {counts}")

  fig=plot_histogram(results,legend=legend_labels)

fig.show()

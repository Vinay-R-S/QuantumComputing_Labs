# Practical 3 - Multiple Qubits system and Entanglement

# Import the packages
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# from from google.colab google.colab import import drive drive
from IPython.display import display, Image

# Create a Quatum Circuit with two qubits
qc = QuantumCircuit(2)

# Apply Hadamard gate on the qubit-0
qc.h(0)

# Apply CNOT(CX) gate with qubit-0 as control qubit and qubit-1 as target qubit to create the Bell States
qc.cx(0,1)

# Use the Aer backend simulator
sim = Aer.get_backend("aer_simulator")

# Save the current statevector
qc.save_statevector()

# Execute the quantum circuit
result = sim.run(qc).result()

# Retrieve the current statevector
state = result.get_statevector()

# Visualize the statevector on a Bloch Sphere. This shows that the individual qubits are in mixed
# state, when measured the qubits collapse to the base state in entangled mode i.e., based on
# state of one qubit we can deduce the state of the other qubit.

# To savve the image to Google Drive, uncomment the following lines and run in Google Colab environment
# drive.mount( "/content/drive" )
# fig = plot_bloch_multivector(state)

# filename = "./Images/Practical-3_Entanglement_Bell_State_Bloch_Sphere.png"
# fig.savefig(filename)
# plt.close(fig)
# display(Image(filename))

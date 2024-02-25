import qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a Quantum Circuit with 3 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit to create a superposition
qc.h(0)

# Use a CNOT gate to entangle the first and second qubits
# 0 - first qubit as a control, 1 - second qubit as a target (target is the one being flipped if needed)
qc.cx(0, 1)

# Measure the second qubit and store the results in the second classical bit (collapses all entangled qubits due to physics)
qc.measure([1], [1])

# Let's draw the circuit to visualize what we have
print(qc.draw())



# Use the Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
job = execute(qc, simulator, shots=1024)
result = job.result()

counts = result.get_counts(qc)
print("\nTotal count for 0 and 1 are:", counts)
plot_histogram(counts)
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Define the hidden string
hidden_string = "0101010000101011110001010110"

# Create a quantum circuit with 8 qubits for the input and 1 auxiliary qubit, plus classical bits for measurement
qc = QuantumCircuit(len(hidden_string) + 1, len(hidden_string))

# Apply Hadamard gates to the input qubits to create a superposition
qc.h(range(len(hidden_string)))

# Put the auxiliary qubit in state |-> to facilitate phase kickback
qc.x(len(hidden_string))
qc.h(len(hidden_string))

# Apply the oracle: For each '1' in the hidden string, apply a CNOT between that qubit and the auxiliary qubit
for i, bit in enumerate(hidden_string):
    if bit == "1":
        qc.cx(i, len(hidden_string))

# Apply Hadamard gates to the input qubits again
qc.h(range(len(hidden_string)))

# Measure the input qubits
qc.measure(range(len(hidden_string)), range(len(hidden_string)))

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1)
result = job.result()
counts = result.get_counts(qc)
print(counts)

# Optional: Plot the histogram of results
plot_histogram(counts)

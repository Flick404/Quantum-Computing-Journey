from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Step 1: Create the quantum circuit
# q0: State to teleport, q1: Alice's part of the entangled pair, q2: Bob's part of the entangled pair
# c0, c1: Classical bits to hold the measurement results from Alice, c2: Classical bit for Bob's measurement (optional)
qc = QuantumCircuit(3, 3)

# Step 2: Create entanglement between Alice's and Bob's qubits (q1 and q2)
qc.h(1)  # Apply Hadamard gate to q1
qc.cx(1, 2)  # CNOT with q1 as control and q2 as target

# Step 3: Prepare the initial state to teleport (q0), if specific state preparation is required
# Example: Teleporting |1> state (uncomment the next line to teleport |1>)
# qc.x(0)

# Step 4: Perform Bell-state measurement on q0 and q1
qc.cx(0, 1)  # CNOT with q0 as control and q1 as target
qc.h(0)  # Hadamard on q0

# Step 5: Measure qubits q0 and q1 into classical bits c0 and c1
qc.measure(0, 0)
qc.measure(1, 1)

# Step 6: Apply conditional operations on q2 based on the measurement results
qc.cx(1, 2)  # Apply CNOT to q2 controlled by q1's measurement result
qc.cz(0, 2)  # Apply CZ to q2 controlled by q0's measurement result

# Optional: Measure q2 to verify the teleportation
qc.measure(2, 2)

# Display the circuit
print(qc.draw())

# Execute the circuit on the qasm simulator
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()

# Get the counts and plot the histogram
counts = result.get_counts(qc)
print("\nMeasurement Results:", counts)
plot_histogram(counts)

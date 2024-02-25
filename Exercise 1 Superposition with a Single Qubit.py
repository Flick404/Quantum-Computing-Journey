import qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(1, 1)

qc.h(0)

qc.measure(0, 0)


simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
job = execute(qc, simulator, shots=1024)
result = job.result()

counts = result.get_counts(qc)
print("\nTotal count for 0 and 1 are:", counts)
plot_histogram(counts)
import qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(2, 2)

qc.h(0)

qc.cx(0, 1)
qc.x(1)

qc.measure([0, 1], [0, 1])

print(qc.draw())

# Use the Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
job = execute(qc, simulator, shots=1024)
result = job.result()

counts = result.get_counts(qc)
print(counts)
plot_histogram(counts)
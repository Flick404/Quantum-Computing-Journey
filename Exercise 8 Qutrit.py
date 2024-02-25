# Come up with workaround for qiskit to repsresent 3d qubit

from qiskit import QuantumCircuit, Aer, execute
import numpy as np


qc = QuantumCircuit(1, 1)
theta = 2 * np.arccos(np.sqrt(1/3))
qc.ry(theta, 0)
qc.measure(0, 0)

third = QuantumCircuit(1, 1)
third.h(0)
third.measure(0, 0)


results_dict = {0: 0, 1: 0, 2: 0}


for _ in range(1024):
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1)
    result = job.result()
    counts = result.get_counts(qc)
    keys = list(counts.keys())

    if keys[0] == "0":
        final = 0
    else:  # Any outcome other than "0" should trigger the 'third' circuit
        job = execute(third, simulator, shots=1)
        result = job.result()
        counts = result.get_counts(third)
        tkeys = list(counts.keys())

        if tkeys[0] == "1":
            final = 2
        else:
            final = 1

    results_dict[final] += 1

print(results_dict)

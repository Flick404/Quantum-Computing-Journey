from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import math

def find_theta():
    reply = input("Give me desired ratio between states, split them by space: ")
    nums = reply.split(" ")
    
    # Ensure two numbers were entered
    if len(nums) != 2:
        print("Invalid input. Please enter two numbers separated by space.")
        return None
    
    try:
        # Convert input to integers or floats
        num1 = float(int(nums[0]))
        num2 = float(int(nums[1]))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None
    
    ratio_sqrt = math.sqrt(num1 / num2)
    theta = 2 * math.atan(ratio_sqrt)
    
    return theta

theta = find_theta()

qc = QuantumCircuit(1, 1)  # Create a quantum circuit with one qubit
qc.ry(theta, 0)  # Apply Ry gate with angle theta to qubit 0
qc.measure(0, 0)  # Measure the state of the qubit

# Visualize the circuit
print(qc.draw())

print(f" Calculated theta is: {theta}")

# Execute the circuit on a simulator
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)

# Display the results
print("\nTotal count for 0 and 1 are:", counts)
plot_histogram(counts)

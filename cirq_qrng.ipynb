try:
    import cirq
except ImportError:
    print("installing cirq...")
    !pip install --quiet cirq
    import cirq

    print("installed cirq.")

# !pip install qiskit qiskit-aer cirq --quiet # install qiskit tools quietly so there is no logs

from qiskit import QuantumCircuit #tool to make quantum circuts
from qiskit_aer import Aer
import time
import cirq

start_qiskit = time.time()

num_bits = 16

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

backend = Aer.get_backend('qasm_simulator')
job = backend.run(qc, shots=num_bits)
counts = job.result().get_counts()

random_bits = ""
for outcome, count in counts.items():
    random_bits += outcome * count

end_qiskit = time.time()

random_bits = random_bits[:num_bits]
random_number = int(random_bits, 2)
print("Random bits:", random_bits)
print("Random number:", random_number)
print(f"Execution time: {end_qiskit - start_qiskit:.5f} seconds\n")

start_cirq = time.time()

qubit = cirq.GridQubit(0, 0)
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT gate (superposition)
    cirq.measure(qubit, key='m')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=num_bits)

measurements = result.measurements['m'].flatten()
random_bits_cirq = ''.join(map(str, measurements))
random_number_cirq = int(random_bits_cirq, 2)

end_cirq = time.time()

print("Cirq QRNG")
print("Random bits:", random_bits_cirq)
print("Random number:", random_number_cirq)
print(f"Execution time: {end_cirq - start_cirq:.5f} seconds\n")

print(circuit)

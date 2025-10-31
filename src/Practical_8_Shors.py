# Practical 8 - Shors Algorithm

# Import the packages
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import math
from fractions import Fraction

def continued_fraction( x, max_denominator ):
    frac = Fraction( x ).limit_denominator( max_denominator )
    return frac.denominator

def quantum_order_finding( a, N ):
    n = int( math.ceil( math.log2( N ) ) )
    
    qc = QuantumCircuit( 2*n + n, 2*n )
    qc.x( 2*n + n - 1 )
    qc.h( range( 2*n ) )
    
    # Inverse QFT on upper register (simplified)
    for qubit in range( 2*n // 2):
        qc.swap( qubit, 2*n - qubit - 1 )
    for j in range( 2*n ):
        for m in range( j ):
            qc.cp( -math.pi / float( 2 ** ( j - m ) ), m, j )
        qc.h( j )
        
    qc.measure( range( 2*n ), range( 2*n ) )
    
    simulator = AerSimulator()
    job = simulator.run( qc, shots = 1024 )
    result = job.result()
    counts = result.get_counts()
    
    measured = max( counts, key = counts.get )
    decimal = int( measured, 2 )
    
    phase = decimal / ( 2 ** ( 2 * n ) )
    r = continued_fraction( phase, N )
    
    return r

def find_factors( N ):
    for a in range( 2, N ):
        if math.gcd( a, N ) != 1:
            factor = math.gcd(a, N)
            print( f"Found non-trivial factor {factor} by gcd with a={a}" )
            return factor
    
        print( f"Trying a = {a}" )
        r = quantum_order_finding (a, N )
        print( f"Estimated order r = {r}" )
    
        if r is None or r % 2 != 0:
            print( f"r = {r} is odd or None; trying next a" )
            continue
    
        x = pow( a, r // 2, N )
        
        if x == N - 1:
            print( "x ≡ -1 mod N; trying next a" )
            continue
    
        factor1 = math.gcd( x - 1, N )
        factor2 = math.gcd( x + 1, N )
    
        print( f"Possible factors: {factor1}, {factor2}" )
        if factor1 != 1 and factor1 != N:
            print( f"Non-trivial factor found: {factor1}" )
            return factor1

        if factor2 != 1 and factor2 != N:
            print (f"Non-trivial factor found: {factor2}" )
            return factor2

    print("Failed to find factors with all candidates")
    return None

N = 11235
factor = find_factors(N)
print(f"Result: factor of {N} is {factor}")

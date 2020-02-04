import sys
import os
import msprime
import timeit

start = timeit.default_timer()

def my_simulator( s_samplesSize, s_Ne, s_lenght, s_mutationRate, s_fileName, s_recombinationRate=0):
    """
    This function will generate the genome simulations usign msprime
    """
    print("We start to process your sample: " + s_fileName)
    simulatedSequences = msprime.simulate(sample_size=s_samplesSize, Ne=s_Ne, length=s_lenght, mutation_rate=s_mutationRate, recombination_rate=s_recombinationRate)
    print("The simulation of your sample " + s_fileName + " IS FINISHED!")
    
    print("We are going to draw the coalescent tree of your sample: " + s_fileName)
    treeSimulations = simulatedSequences.first()
    print(treeSimulations.draw(format="unicode"))
    
    print("Writing down vcf format of sample " + s_fileName)
    with open("./simulationsFiles/"+s_fileName+".vcf", "w") as vcf_file:
        simulatedSequences.write_vcf(vcf_file)
    
    print("Writing down fasta format of sample " + s_fileName)
    with open("./simulationsFiles/"+s_fileName+".fasta", "w") as fasta_file:
        simulatedSequences.write_fasta(fasta_file)
    
def exponentialrange(start, end, exp=10):
    expRange=[]
    while start <= end:
        #print (start)
        expRange.append(start)
        # Here, I actually also can use ** for exp, but I already did it this way so, no problem
        start= start*exp 
    return (expRange)
    

numSim=1
for i_samplesSize in range (10, 101, 10):
    for j_Ne in range(10,101,10):
        if j_Ne >= i_samplesSize:
            for k_lenght in exponentialrange(1000,100001):
                mutationRates=[1e-9,1e-8,1e-6,1e-3,1e-0]
                for l_mutation in mutationRates:
                    recombinationRates=[1e-9,1e-8,1e-6,1e-3,1e-0,0]
                    for m_recombination in recombinationRates:
                        fileName="SIMULATION_"+str(numSim)+"_sampleSize-"+str(i_samplesSize)+"_Ne-"+str(j_Ne)+"_lenght-"+str(k_lenght)+"_mutation-"+str(l_mutation)+"_recombination-"+str(m_recombination)
                        my_simulator(i_samplesSize, j_Ne, k_lenght, l_mutation, fileName, m_recombination )
                        numSim += 1

stop = timeit.default_timer()
total_time = stop - start

# output running time in a nice format.
mins, secs = divmod(total_time, 60)
hours, mins = divmod(mins, 60)

sys.stdout.write("Total running time: %d:%d:%d.\n" % (hours, mins, secs))

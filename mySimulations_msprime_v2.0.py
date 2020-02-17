import sys
import os
import msprime
import timeit

# Start timer for the script
start = timeit.default_timer()

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        
	print '''
        
	Simulated genomes using msprime
        Sarai Reyes
        sarai.reyes.av@gmail.com
	
	Description:
	This function will generate simulated genomes based on a coalescent model. 
	It is using the module msprime, more infomration about msprime can be found it here: https://msprime.readthedocs.io/en/stable/
	
	
	Usage/Input:
        python simulatedGenomes_msprime.py --help 
        python3.8 FrequencyNucleotidesInBamFiles.py [reference.fasta] [mapFile.bam] [sample name]
        
	Output:
	The following outputs are genaretd by default but you can choose no generate them
	1. Print th coalescemt trees in the screen
	2. Simulated genomes in vcf file format
	3. Simulated genomes in fasta file format
	
	##### HAVENT FINISHED
	
	'''
        exit(0)

def my_simulator( s_samplesSize, s_Ne, s_lenght, s_mutationRate, s_fileName, s_recombinationRate=0, ):
    """
    This function will generate the genome simulations using msprime
    Input:
    
    """
    print("We start to process your sample: " + s_fileName)
    # Main line generating the simulation
    simulatedSequences = msprime.simulate(sample_size=s_samplesSize, Ne=s_Ne, length=s_lenght, mutation_rate=s_mutationRate, recombination_rate=s_recombinationRate)
    print("The simulation of your sample " + s_fileName + " IS FINISHED!")
    
    #print("We are going to draw the coalescent tree of your sample: " + s_fileName)
    #treeSimulations = simulatedSequences.first()
    #print(treeSimulations.draw(format="unicode"))
    
    # Print the simulation in a vcf file format
    print("Writing down vcf format of sample " + s_fileName)
    with open("./simulationsFiles/"+s_fileName+".vcf", "w") as vcf_file:
        simulatedSequences.write_vcf(vcf_file)
    
    # Print the simulation in a fasta file format
    #print("Writing down fasta format of sample " + s_fileName)
    #with open("./simulationsFiles/"+s_fileName+".fasta", "w") as fasta_file:
     #   simulatedSequences.write_fasta(fasta_file)
    

numSim=1
sampleSizes=[50,500]
for i_samplesSize in sampleSizes:
	Nes=[1000,10000]
    for j_Ne in Nes:
    	exponentialRanges=[10000000, 100000000]
    	for k_lenght in exponentialRanges:
                mutationRates=[7e-9,1.3e-8]
                for l_mutation in mutationRates:
                    recombinationRates=[8e-9,1.6e-8,0]
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

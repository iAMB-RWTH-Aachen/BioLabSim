import random
import matplotlib.pyplot as plt
import numpy as np


def random_sequence_generator(length:int) -> str:
   nucleotides = ['A', 'T', 'C', 'G']
   return ''.join(random.choice(nucleotides) for i in range(length))

def get_promoter_sequence(activator:str) -> str:
    if activator == 'glucose': length = 56
    if activator == 'glycerol':length = 40
    return random_sequence_generator(length)

def get_activator_sequence(metabolism:str) -> str:
    if metabolism == 'glucose': length = 115
    if metabolism == 'glycerol':length = 166
    return random_sequence_generator(length)

def get_repressor_sequence(metabolism:str) -> str:
    if metabolism == 'glucose': length = 150
    if metabolism == 'glycerol':length = 174
    return random_sequence_generator(length)

def get_putida_genome(promoter:str, regulator:str) -> str:
    putida_genome = random_sequence_generator(random.randint(100, 1000))+ promoter+regulator
    putida_genome += random_sequence_generator(random.randint(0, 1000))
    return putida_genome


def perform_batch_experiment(mutant, insert):
    time = np.arange(0, 10)
    if len(insert.seq) == 56 + 115:
        glc = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
        glyc = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
        # glc activator + glc promoter
    if len(insert.seq) == 56 + 150:
        glc = [5] * 10
        glyc = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
        # glc repressor+ glc_promoter
    if len(insert.seq) == 56 + 166:
        glc = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
        glyc = [5, 4, 4, 3, 3, 3, 3, 3, 3, 3]
        # glyc activator + glc promoter
    if len(insert.seq) == 56 + 174:
        glc = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
        glyc = [5, 5, 5, 5, 5, 4, 3, 2, 1, 0]
        # glyc repressor + glc promoter
    if len(insert.seq) == 40 + 115:
        glc = [5, 4, 3, 3, 2, 2, 2, 2, 2, 2]
        glyc = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
        # glc activator + glyc promoter
    if len(insert.seq) == 40 + 150:
        glc = [5, 5, 5, 5, 5, 4, 3, 2, 1, 0]
        glyc = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
        # glc repressor+ glyc_promoter
    if len(insert.seq) == 40 + 166:
        glc = [5] * 10
        glyc = [5, 4, 4, 3, 3, 2, 2, 2, 1, 1]
        # glyc activator + glyc promoter
    if len(insert.seq) == 40 + 174:
        glc = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
        glyc = [5] * 10
        # glyc repressor + glyc promoter

    plt.plot(time, glc, label= 'glucose [$g_{glc}/L$]')
    plt.plot(time, glyc,  label= 'glycerol [$g_{glyc}/L$]')
    plt.xlabel('concentration [g/L]')
    plt.ylabel('time[h]')
    plt.legend()
    plt.show()
from algorithms.fifo import FIFO
from algorithms.LRU import LRU
from algorithms.clock import Clock
from algorithms.OPT import OPT
from utils.generator import generate_access_sequence
from utils.performance import evaluate_performance

def main():
    num_frames = 3
    num_pages = 5
    sequence_length = 10
    access_sequence = generate_access_sequence(num_pages, sequence_length)

    print("Testing FIFO Algorithm:")
    fifo = FIFO(num_frames)
    page_faults_fifo = evaluate_performance(fifo, access_sequence)
    print(f"Total Page Faults (FIFO): {page_faults_fifo}\n")

    print("Testing LRU Algorithm:")
    lru = LRU(num_frames)
    page_faults_lru = evaluate_performance(lru, access_sequence)
    print(f"Total Page Faults (LRU): {page_faults_lru}\n")

    print("Testing Clock Algorithm:")
    clock = Clock(num_frames)
    page_faults_clock = evaluate_performance(clock, access_sequence)
    print(f"Total Page Faults (Clock): {page_faults_clock}\n")

    print("Testing OPT Algorithm:")
    opt = OPT(num_frames)
    page_faults_opt = evaluate_performance(opt, access_sequence)
    print(f"Total Page Faults (OPT): {page_faults_opt}")

if __name__ == "__main__":
    main()
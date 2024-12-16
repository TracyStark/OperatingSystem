from algorithms.fifo import FIFO
from algorithms.LRU import LRU
from algorithms.clock import Clock
from algorithms.OPT import OPT
from algorithms.improvedClock import ImprovedClock  
from utils.generator import generate_access_sequence
from utils.performance import evaluate_performance

def main():
    num_frames = 10  # 内存的帧数
    num_pages = 20  # 总页数
    sequence_length = 50  # 访问序列长度
    access_sequence = generate_access_sequence(num_pages, sequence_length)

    algorithms = {
        "FIFO": FIFO(num_frames),
        "LRU": LRU(num_frames),
        "Clock": Clock(num_frames),
        "OPT": OPT(num_frames),
        "Improved Clock": ImprovedClock(num_frames)
    }

    results = {}

    for name, algorithm in algorithms.items():
        print(f"Testing {name} Algorithm:")
        page_faults = evaluate_performance(algorithm, access_sequence)
        results[name] = page_faults
        print(f"Total Page Faults ({name}): {page_faults}\n")

    print("Summary of Page Faults and Rates:")
    for name, page_faults in results.items():
        fault_rate = page_faults / sequence_length
        print(f"{name} - Page Faults: {page_faults}, Fault Rate: {fault_rate:.2f}")

if __name__ == "__main__":
    main()
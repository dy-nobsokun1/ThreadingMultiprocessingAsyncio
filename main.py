import multiprocessing_task
import threading_task
import async_task
import generate_numbers
import asyncio
import multiprocessing

def main():
    # Step 1: Generate numbers file
    print("Generating numbers.txt file...")
    generate_numbers.generate_numbers_file("numbers.txt", 10000, 100000, 1000000)
    
    # Step 2: Read numbers from file
    print("Reading numbers from file...")
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    # Step 3: Run multiprocessing task to find primes
    print("Running multiprocessing task to find primes...")
    chunk_size = len(numbers) // multiprocessing.cpu_count()  # Divide numbers by available CPUs
    primes = multiprocessing_task.find_primes_in_range(numbers, chunk_size)
    print(f"Prime numbers found: {primes[:10]}...")  # Print first 10 primes for brevity

    # Step 4: Run threading task to simulate I/O
    print("Running threading I/O tasks...")
    threading_task.run_io_tasks()  # Assuming it simulates some unrelated I/O tasks

    # Step 5: Run async tasks to write primes to files
    print("Running async file write tasks...")
    asyncio.run(async_task.run_async_tasks(primes))

if __name__ == "__main__":
    main()

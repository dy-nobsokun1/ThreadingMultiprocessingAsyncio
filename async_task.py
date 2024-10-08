import asyncio

async def async_write_to_file(filename, data, duration):
    """Simulate async writing to a file."""
    print(f"Starting async write to {filename}")
    await asyncio.sleep(duration)  # Simulate writing delay
    with open(filename, 'w') as f:
        f.write('\n'.join(map(str, data)))  # Write data to the file
    print(f"Completed async write to {filename}")

async def run_async_tasks(primes):
    """Run multiple async file writes concurrently."""
    # Create a list of async tasks to write primes to different files
    tasks = [
        async_write_to_file(f"primes_{i}.txt", primes[i::5], 2) for i in range(5)
    ]
    await asyncio.gather(*tasks)  # Execute all tasks concurrently
    print("All async tasks completed.")

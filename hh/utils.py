import functools
import time


def timeit(func):
    @functools.cache
    @functools.wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


def save_pq(df, path):
    print(f'Writing Dataframe to {path}')
    df.write_parquet(path)

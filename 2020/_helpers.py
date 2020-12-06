import functools
import time

#
# for data where a newline marks the end of a new group
# 
# returns a list with a sublist for every group
#
def grouped_reader(filename, parse_fn = lambda x: x):
    output = []
    temp = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                output.append(temp)
                temp = []
            else:
                temp.append(parse_fn(line))
        output.append(temp)
    return output

# measure time of a method (borrowed from safetymonkey)
def timer(func):
  @functools.wraps(func)
  def wrapper_timer(*args, **kwargs):
    tic = time.perf_counter()
    value = func(*args, **kwargs)
    toc = time.perf_counter()
    elapsed_time = toc - tic
    print(f"Elapsed time: {elapsed_time:0.4f} seconds")
    return value

  return wrapper_timer
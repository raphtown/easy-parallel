# Parallel

## Installation

`make requirements`

## Usage

```
def foo(x, y):
  return x + y

num_threads = 10
inputs = [(x * x, x) for x in range(10)]

import parallel as par
results = par.submit_jobs(foo, inputs, num_threads)
print results
```

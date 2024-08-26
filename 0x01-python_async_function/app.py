#!/usr/bin/env python3
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    result = await asyncio.gather(
        *tuple(map(lambda _ : task_wait_random(max_delay), range(n)))
    )
    return result

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
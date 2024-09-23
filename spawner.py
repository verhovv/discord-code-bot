import asyncio
import sys
import time
from asyncio import subprocess

from config import TIME_LIMIT


async def test_code(code: str, stdin_string: str) -> [str, float]:
    process = await subprocess.create_subprocess_exec(
        sys.executable, '-c', code,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    process.stdin.write(bytes(stdin_string, 'utf-8'))

    start_time = time.time()
    async with asyncio.timeout(TIME_LIMIT):
        stdout, stderr = await process.communicate()

    time_passed = time.time() - start_time

    if stdout:
        return stdout.decode(), time_passed
    if stderr:
        return stderr.decode(), time_passed

    return 'Program do nothing', 0

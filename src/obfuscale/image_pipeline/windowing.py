"""Placeholders for Head, Head–Tail, HTS windowing."""


def head(data: bytes, n: int) -> bytes:
    return data[:n]


def head_tail(data: bytes, n: int) -> bytes:
    half = n // 2
    return (
        data[:half] + data[-(n - half) :]
        if len(data) >= n
        else (data + b"\x00" * (n - len(data)))
    )

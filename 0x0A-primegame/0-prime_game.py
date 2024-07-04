#!/usr/bin/python3
"""
Prime Game Implementation
"""


def sieve_of_eratosthenes(limit):
    """
    Generate all prime numbers up to a given limit
    using the Sieve of Eratosthenes.

    Args:
        limit (int): The upper limit up to which primes are to be found.

    Returns:
        list: A list of prime numbers up to the given limit.
    """
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes


def play_game(n, primes):
    """
    Simulate a single round of the game and determine the winner.

    Args:
        n (int): The upper limit of the set of consecutive integers.
        primes (list): A list of prime numbers up to the maximum limit.

    Returns:
        int: The winner of the game (0 for Maria, 1 for Ben).
    """
    available = [True] * (n + 1)
    turn = 0  # 0 for Maria, 1 for Ben
    for prime in primes:
        if prime > n:
            break
        if available[prime]:
            for multiple in range(prime, n + 1, prime):
                available[multiple] = False
            turn = 1 - turn  # Switch turns
    return turn


def isWinner(x, nums):
    """
    Determine the overall winner after x rounds of the game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of upper limits for each round.

    Returns:
        str: The name of the player that won the most rounds ("Maria" or "Ben").
             If the winner cannot be determined, returns None.
    """
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

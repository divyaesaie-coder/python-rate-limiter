# python-rate-limiter
A simple Python backend rate limiter that restricts request counts and temporarily blocks users after exceeding the limit.
# Python Rate Limiter

A beginner-friendly Python project that simulates backend API rate limiting using loops and timers.

## Features
- Tracks request count
- Limits maximum requests
- Temporary cooldown using time delay
- Automatically resets request counter

## Technologies Used
- Python 3
- time module

## How It Works
The program:
1. Accepts user requests
2. Counts the number of requests
3. Allows only limited requests
4. Blocks additional requests temporarily
5. Resets after waiting period

## Concepts Used
- while loop
- if-else conditions
- Counters
- time.sleep()
- Backend logic simulation

## Run the Program

```bash
python rate_limiter.py

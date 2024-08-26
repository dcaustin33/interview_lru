# LRU Cache Interview Question

The following repo contains code for an interview question aimed at assessing a candidate's understanding of an LRU (Least Recently Used) cache.

## Problem Overview

This problem should take around 20-30 minutes for a candidate to implement a decent solution.

The outline provided to the candidate will be minimal to observe how they think through the problem. Initially, we will ensure they understand what an LRU cache is (a red flag if they do not), and then task them with implementing one.

## Requirements

The candidate will be required to implement two methods:
- `put(key, value)`
- `get(key)`

The rest of the implementation will be left to their discretion.

## Likely Questions and Answers

- **Q:** What should be returned if the key is not in the cache?
  - **A:** Return `None`.
  
- **Q:** Is the cache infinite, or does it have a finite capacity?
  - **A:** The cache should have a finite capacity, which should be specified.

## Expectations

Any programming language is acceptable, as the focus is mainly on their ability to:
1. Implement a naive solution, likely using lists.
2. Optimize the solution using data structures like dictionaries, hashmaps, sets, etc., if time allows.

In this repo, we have provided two possible solutions using Python, along with numerous edge cases that can be used to test the candidate's implementation.
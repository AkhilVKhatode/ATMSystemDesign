# System Design - Design ATM Machine

This project simulates an ATM machine that dispenses cash using the **Chain of Responsibility** design pattern. It breaks down a requested amount into available denominations of `$50`, `$20`, and `$10` bills and handles any unprocessable remainder with an error handler.

## 🧩 Design Pattern Used
**Chain of Responsibility** – This behavioral pattern allows a request to pass through a chain of handlers until it is fully processed. Each handler is responsible for a specific denomination.

## 📂 Project Structure

- `Amount`: Holds the amount to be withdrawn.
- `Handler`: Abstract class defining the structure for currency handlers.
- `FiftyDollarHandler`, `TwentyDollarHandler`, `TenDollarHandler`: Concrete handlers for each bill denomination.
- `ErrorHandler`: Catches any amount that can't be processed by the available denominations.

## 🔁 Flow Overview

1. User enters a withdrawal amount (e.g., `$187`).
2. The request flows through the handler chain: `$50 → $20 → $10 → Error`.
3. Each handler processes its part and passes the remaining amount forward.

## ▶️ Example Output

Dispensing 3 x $50
Dispensing 1 x $20
Dispensing 1 x $10
Error: Cannot dispense the remaining amount of $7

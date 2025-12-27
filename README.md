# 🎱 Powerball Number Generator & Checker
An interactive Powerball project that generates lottery numbers and checks them against winning draws, built to practice Python fundamentals, input validation, and real-world edge case handling.
The goal of this project wasn’t to “beat the lottery,” but to build a clean, defensive program that handles bad input gracefully and behaves the way a real system should. Inpsired by Al Sweigart.

---

## ✨ Technologies
  - Python 3
  - Standard Library (random, sys)
  - CLI-based interaction

## 🚀 Features
  - Generates valid Powerball numbers (1–69 + Powerball 1–26)
  - Ensures all user-entered numbers are unique
  - Handles invalid input (duplicates, out-of-range values, non-numeric input)
  - Compares user numbers to winning numbers
  - Displays match results clearly in the terminal

## 🧠 The Process
I started this project as a simple number generator, but quickly realized that input handling was the real challenge.
Letting users enter five numbers sounds easy — until you account for:
  - Duplicate values
  - Numbers outside the allowed range
  - Unexpected input that crashes the program
Instead of letting the program fail, I added validation loops and clear error messages so users are guided back on track. This forced me to think more like an engineer and less like someone just trying to “get it to work.”
The biggest takeaway was learning how small defensive checks dramatically improve reliability, even in simple scripts.

## 🧪 What I Learned
  - Why validating user input is non-negotiable
  - How while loops can enforce constraints without hurting UX
  - The importance of failing safely instead of crashing
  - How small projects reveal real-world engineering habits
This project helped reinforce concepts I regularly see discussed in interviews: edge cases, defensive coding, and clarity over cleverness.

## 📷 Preview

<img width="524" height="339" alt="PB4" src="https://github.com/user-attachments/assets/d072a459-7312-4f33-8a93-eac4ab7a7943" />



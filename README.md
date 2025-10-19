# 🏦 Bank Account System (OOP Project in Python)

This project demonstrates all **4 Pillars of Object-Oriented Programming (OOP)** in Python:
1. **Encapsulation**
2. **Inheritance**
3. **Polymorphism**
4. **Abstraction**

---

## 🚀 Project Overview
The **Bank Account System** simulates different types of bank accounts (`SavingsAccount` and `CurrentAccount`) using OOP principles.

### ✨ Features
- Create different account types (Savings / Current)
- Deposit and withdraw money
- Secure balance handling using encapsulation
- Uses abstract base class to define a common structure for all account types
- Demonstrates method overriding and polymorphism

---

## 🧱 OOP Concepts Used

| Concept | Description | Example in Code |
|----------|--------------|----------------|
| **Encapsulation** | Private attributes and getter/setter methods protect data | `__balance`, `__account_number` |
| **Inheritance** | `SavingsAccount` and `CurrentAccount` inherit from `Account` | `class SavingsAccount(Account):` |
| **Polymorphism** | Same method behaves differently across subclasses | `deposit()`, `withdraw()` |
| **Abstraction** | Defines abstract methods to enforce structure | `@abstractmethod` in `Account` |


---

## 💻 Example Output


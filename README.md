# Quantum Car Factory

An object-oriented car factory simulation demonstrating the **Factory Pattern**, **Composition**, and **Polymorphism** design principles.

---

## Features

- **Three engine types:**
  - Gas Engine
  - Electric Engine
  - Hybrid Engine (Gas + Electric)

- **Car operations:**
  - `start()` → starts the car at speed 0
  - `stop()` → stops the car (only if speed is 0)
  - `accelerate()` → increases speed by 20 km/h (max 200 km/h)
  - `brake()` → decreases speed by 20 km/h

- **Engine operations:**
  - `increase()` → increases internal engine speed by 1
  - `decrease()` → decreases internal engine speed by 1

- **Hybrid engine behavior:**
  - Uses **Electric** when speed < 50 km/h
  - Uses **Gas** when speed >= 50 km/h
  - Never runs both engines simultaneously (cost optimized)

- Dynamic engine replacement via factory

---

## Project Structure

```
.
├── main.py
├── factory/
│   └── car_factory.py
├── cars/
│   └── car.py
└── engines/
    ├── engine.py
    ├── gas_engine.py
    ├── electric_engine.py
    └── hybrid_engine.py
```

---

## Design Patterns

### Factory Pattern
`CarFactory` creates cars with different engine types and replaces engines dynamically.

### Composition
A `Car` contains an `Engine` rather than inheriting from it.

### Polymorphism
Each engine implements `update_speed()` differently.

---

## How to Run

```bash
python main.py
```

---

## Example Output

```
=== Gas Car ===
Car started.
Accelerating... Speed = 20
Accelerating... Speed = 40
Braking... Speed = 20
Braking... Speed = 0
Car stopped.
------------------------------
=== Electric Car ===
...
=== Hybrid Car ===
...
[Hybrid] Using Electric Engine
[Hybrid] Using Gas Engine
...
=== Replace Engine (Gas -> Hybrid) ===
...
```
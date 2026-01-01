MAHA – Modular Adaptive Helper for Academics

MAHA is an academic software project developed in Python whose goal is to support engineering students at academic risk through an adaptive system that analyzes performance, identifies weaknesses, and generates personalized learning paths based on each student’s needs.

The system integrates algorithmic logic, data structures, a basic neural network, and a graphical user interface, combining concepts from software engineering, data analysis, and educational systems design.


🎯 Project Objective

Detect academic difficulties by subject and topic

Evaluate student mastery through adaptive questioning

Generate personalized learning paths based on results and prerequisites

Track progress through persistent student profiles

Provide all functionality through a user-friendly graphical interface


🧠 System Architecture

MAHA is structured into clearly separated modules to ensure maintainability and scalability:

├──main.py # Core system logic and execution flow

├── INTERFAZ.py # Graphical User Interface (GUI)

├── modelo_nn.py # Neural network for performance evaluation

├── GRAFO_LOGICA.py # Prerequisite and dependency logic (graph-based)

├── CONTENIDO.py # Academic content and question bank

├── PERFILES.py # Student profile management

├── UTILIDADES.py # Utility and helper functions

├── TEMA.py # Academic topic model

├── PREREQUISITOS.json # External definition of topic prerequisites

└── .venv/ # Virtual environment (not required in repo)



⚙️ Execution Flow

The user selects or creates a student profile

MAHA evaluates the student through topic-specific questions

Results are processed using:

Performance thresholds

Topic prerequisite relationships

A basic neural network model

A personalized learning path is generated

Student progress is saved and can be resumed in future sessions


📁 Module Overview
main.py

Main entry point of the system.
Coordinates profile management, evaluation logic, learning path generation, and integration between all modules.

INTERFAZ.py

Implements the graphical user interface (GUI), allowing the system to be used without relying on the terminal.
Displays profiles, evaluation results, and generated learning paths.

modelo_nn.py

Contains a basic neural network used to analyze student performance patterns and support decisions related to reinforcement or advancement.

GRAFO_LOGICA.py

Implements graph-based logic to model topic dependencies and enforce prerequisite completion before allowing progression.

CONTENIDO.py

Acts as the central repository of academic content, including theoretical material, question banks, topic metadata, and suggested learning paths.

PERFILES.py

Handles creation, loading, and persistent storage of student profiles and their performance history.

TEMA.py

Defines the Tema class, representing an academic topic, its content, mastery level, and current state within the learning path.

UTILIDADES.py

Provides helper functions for input normalization, text processing, and shared utilities used across the system.


📊 Evaluation Criteria

The system uses a default passing threshold of 0.8

If the threshold is not met:

The topic is reinforced

The learning path is adjusted

Dependent topics are temporarily locked

Topic prerequisites are dynamically loaded from PREREQUISITOS.json


🚀 Technologies Used

Python

Modular programming

Data structures

Graph-based logic

Basic neural networks

Graphical user interfaces

Persistent data storage

Object-oriented design


📌 Academic Context

MAHA was developed as a university-level academic project, integrating knowledge from programming, data structures, introductory artificial intelligence, software engineering, and systems design.

The project serves both as a functional educational tool and a technical demonstration of applied engineering concepts.


✨ Author

Marlon Molina
Cybernetics Engineering in Computer Systems
Universidad La Salle México

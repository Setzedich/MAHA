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

MAHA FINALIZED/
│
├── main.py              # Core system logic and execution flow
├── INTERFAZ.py          # Graphical User Interface (GUI)
├── modelo_nn.py         # Neural network for performance evaluation
├── GRAFO_LOGICA.py      # Prerequisite and dependency logic (graph-based)
├── CONTENIDO.py         # Academic content and question bank
├── PERFILES.py          # Student profile management
├── UTILIDADES.py        # Utility and helper functions
├── TEMA.py              # Academic topic model
├── PREREQUISITOS.json   # External definition of topic prerequisites
└── .venv/               # Virtual environment (not required in repo)


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
Responsible for:

Loading and managing student profiles

Coordinating evaluations

Generating adaptive learning paths

Integrating GUI, neural network, and content logic

Defines key parameters such as the passing threshold and admin mode.

INTERFAZ.py

Implements the graphical user interface (GUI).
Allows:

User interaction without terminal usage

Profile selection and creation

Visualization of results and learning paths

The interface is decoupled from core logic to simplify maintenance.

modelo_nn.py

Contains a basic neural network used to:

Analyze student performance patterns

Support reinforcement or advancement decisions

Introduce machine learning concepts in an academic context

Designed to be lightweight and educational rather than production-heavy.

GRAFO_LOGICA.py

Models topic relationships using graph-based logic:

Defines dependencies between academic topics

Prevents progression without mastering prerequisites

Ensures pedagogical coherence in generated learning paths

CONTENIDO.py

Acts as the central knowledge repository, containing:

Theoretical content per subject

Question banks

Suggested learning paths

Topic classification and metadata

This design allows easy extension to additional subjects.

PERFILES.py

Handles student profile management:

Creation and loading of profiles

Persistent storage of progress

Performance history tracking

Profiles enable continuity across multiple sessions.

TEMA.py

Defines the Tema class, representing:

An academic topic

Its content

Mastery level

Current state within the learning path

It is the fundamental unit of the system.

UTILIDADES.py

Provides auxiliary functions such as:

Input normalization

Text processing

General-purpose helpers used across modules

Keeps core modules clean and readable.


📊 Evaluation Criteria

The system uses a passing threshold (default: 0.8).

If a student does not meet the threshold:

The topic is reinforced

The learning path is adjusted

Dependent topics are temporarily locked

Prerequisites are dynamically loaded from PREREQUISITOS.json.


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

MAHA was developed as a university-level academic project, integrating knowledge from:

Programming fundamentals

Data structures

Introductory artificial intelligence

Software engineering

Systems design

The project serves both as a functional tool and a technical demonstration.


✨ Author
Marlon Molina
Cybernetics Engineering in Computer Systems
Universidad La Salle México

<div align="center">

# MAHA

### Mathematics Adaptive Helper Assistant

</div>

---

## About the Project

**MAHA** is an educational desktop application developed in **Python**.  
Its main objective is to help students reinforce academic topics through diagnostic questions, personalized learning paths, user profiles, visual content, prerequisite maps, and a neural network model that analyzes student performance.

The system includes different subjects such as mathematics, physics, chemistry, and programming. Each subject contains topics, exercises, explanations, and reinforcement content designed to guide the student according to their progress.

---

## Main Features

- Educational reinforcement system
- User profile management
- Diagnostic questionnaires
- Personalized learning progress
- Subject-based topic organization
- Prerequisite system between topics
- Visual learning resources using GIFs
- Interactive graphical interface
- Performance tracking
- Neural network model for learning analysis
- Dataset-based progress storage
- Topic recommendation support
- Graph-based visualization of subject relationships
- Save and load system for student profiles

---

## Technologies Used

- Python
- PySide6
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- NetworkX
- JSON
- CSV

---

## Project Structure

<pre>
MAHA/
│
├── GIFS/
│   ├── cada lado 3 cubo - geometria.gif
│   ├── derivada.gif
│   ├── dominio_rango.gif
│   ├── grafica de cos (x) - trigonometria.gif
│   ├── integral.gif
│   ├── magnitud_vector.gif
│   ├── pendiente.gif
│   ├── producto_punto.gif
│   ├── proporcion de sombras - geometria.gif
│   ├── sdfasfaf.gif
│   └── seno_circulo_unitario.gif
│
├── perfiles/
│   ├── angel.json
│   └── martin.json
│
├── CONTENIDO.py
├── GRAFO_LOGICA.py
├── INTERFAZ.py
├── PERFILES.py
├── PREREQUISITOS.json
├── TEMA.py
├── UTILIDADES.py
├── dataset_maha.csv
├── main.py
├── modelo_nn.py
├── nico.png
└── README.md
</pre>

---

## File Description

| File | Description |
|---|---|
| `main.py` | Main execution file of the project. |
| `INTERFAZ.py` | Contains the graphical user interface built with PySide6. |
| `CONTENIDO.py` | Stores subjects, topics, questions, explanations, and reinforcement content. |
| `TEMA.py` | Defines the topic structure and its behavior. |
| `PERFILES.py` | Manages user profiles and saves progress in JSON files. |
| `UTILIDADES.py` | Contains helper functions for text cleaning, validation, and answer processing. |
| `GRAFO_LOGICA.py` | Creates graph structures to represent subjects, topics, and prerequisites. |
| `modelo_nn.py` | Implements the neural network model used to analyze student performance. |
| `PREREQUISITOS.json` | Stores prerequisite relationships between topics. |
| `dataset_maha.csv` | Stores learning data used by the neural network model. |
| `GIFS/` | Contains visual resources used to explain academic topics. |
| `perfiles/` | Stores saved user profiles. |

---

## Subjects Included

The project includes learning paths for the following areas:

- Mathematics
- Physics
- Chemistry
- Programming

---

## Mathematics Topics

Some of the mathematics topics included are:

- Arithmetic
- Basic Algebra
- Geometry
- Trigonometry
- Analytic Geometry
- Precalculus
- Differential Calculus
- Integral Calculus
- Linear Algebra
- Vector Calculus
- Differential Equations
- Vectors and Geometry

---

## Physics Topics

The physics section includes topics such as:

- Vectors and magnitudes
- Kinematics
- Newton's laws
- Work and energy
- Basic electricity

---

## Chemistry Topics

The chemistry section includes fundamental topics such as:

- Atomic structure
- Chemical bonds
- Chemical reactions
- Stoichiometry
- Basic chemistry concepts

---

## Programming Topics

The programming section includes basic reinforcement topics related to programming logic and computational thinking.

---

## How the System Works

MAHA allows the student to create or load a profile.  
After selecting a subject and topic, the system can evaluate the student through diagnostic questions.

Based on the result, the system determines whether the student already understands the topic or needs reinforcement. If reinforcement is needed, the application provides explanations, visual resources, and additional practice.

The project also uses prerequisite logic, meaning some topics may depend on previous knowledge from other topics. This helps organize learning in a more structured way.

---

## Neural Network Model

The project includes a neural network model implemented in `modelo_nn.py`.

This model uses student performance data stored in:

<pre>
dataset_maha.csv
</pre>

The neural network can analyze information such as:

- Topic ID
- Student score
- Global percentage
- Number of attempts

This allows the system to support personalized learning decisions and future topic recommendations.

---

## User Profiles

User progress is saved in the `perfiles/` folder using JSON files.

Example:

<pre>
perfiles/angel.json
perfiles/martin.json
</pre>

Each profile stores information related to the student's progress, completed topics, and learning status.

---

## Visual Resources

The project includes GIF animations to help explain academic concepts visually.

Examples of included visual resources:

- Derivatives
- Integrals
- Domain and range
- Unit circle sine
- Dot product
- Vector magnitude
- Slope
- Geometry examples
- Trigonometric graphs

These resources make the learning process more interactive and easier to understand.

---

## Requirements

Before running the project, make sure you have Python installed.

Recommended Python version:

<pre>
Python 3.10 or higher
</pre>

Required libraries:

<pre>
PySide6
pandas
numpy
scikit-learn
matplotlib
networkx
</pre>

---

## Installation

Clone the repository:

<pre>
git clone https://github.com/your-username/MAHA.git
</pre>

Enter the project folder:

<pre>
cd MAHA
</pre>

Install the required libraries:

<pre>
pip install PySide6 pandas numpy scikit-learn matplotlib networkx
</pre>

---

## How to Run

Run the main file:

<pre>
python main.py
</pre>

If your system uses `python3`, run:

<pre>
python3 main.py
</pre>

---

## Important Notes

- Do not delete the `GIFS/` folder because it contains visual resources used by the application.
- Do not delete `PREREQUISITOS.json` because it stores topic dependency information.
- Do not delete the `perfiles/` folder if you want to keep saved student progress.
- Do not delete `dataset_maha.csv` because it stores learning data used by the neural network model.
- Make sure all files remain in the same project structure to avoid path errors.

---

## Educational Purpose

This project was developed as an academic software project to practice and demonstrate knowledge in:

- Python programming
- Object-oriented programming
- Graphical user interface development
- Educational software design
- File handling with JSON and CSV
- Data processing
- Neural network implementation
- Graph logic
- Student profile management
- Adaptive learning systems
- User experience design

---

## Future Improvements

Possible future improvements for the project include:

- Adding more subjects and topics
- Improving the neural network recommendations
- Adding more interactive exercises
- Creating a progress dashboard
- Adding more visual animations
- Implementing a login system
- Exporting student progress reports
- Adding difficulty levels
- Improving the interface design
- Adding database support

---

## Author

Developed by **Marlon Molina**.

---

## License

This project was created for educational purposes.

You may use it as a learning reference or modify it for academic and personal practice.

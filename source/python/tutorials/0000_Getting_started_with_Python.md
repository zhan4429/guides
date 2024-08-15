# Get started with Python
Welcome to your beginner’s guide to Python! This document is designed to get you up and running with Python programming. By the end of this tutorial, you’ll have Python installed and ready to code. Let’s get started and enjoy learning Python!
## What is Python
Python is a high-level general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. This means that the code we are writing should be readable by humans (us) and the empty space (idents such as tab) modify the code. Python is dynamically typed. Dynamic typing means we do not have to declare the type of data we are working with beforehand based on the characteristics of the data. It supports multiple programming paradigms including structured object-oriented and functional programming. (source: Wikipedia)

### The basics
**A popular programming language**
- Python is one of the most popular programming languages in the world known for its readability and simplicity. It is widely used by both beginners and experienced developers.

**Free and open source**
- Accessibility: Python is free to use and its source code is open to the public. It is developed under an OSI-approved open-source license.
- Community Support: Being open source Python has a large and active community. This community contributes to a vast array of libraries and tools making finding help and resources for your projects easier. The Python Package Index (PyPI) hosts thousands of third-party modules for Python. Both Python's standard library and the community-contributed modules allow for endless possibilities.

**Wide range of applications**
- Data Analysis
- Machine Learning
- Software Development
- Web Development
- Education

### The technical stuff
**High-level language**
Like C++ and Java, Python provides a higher level of abstraction than low-level languages like Assembly which are closer to machine code meaning Python abstracts away many of the complex details of the computer's hardware. This makes it easier to write and understand code.

**Interpreted and Dynamically Typed**
Python is an interpreted language meaning you can run your code directly without the need for a separate compilation step. Python can be used interactively running code line by line in a Python shell or an integrated development environment (IDE) like Jupyter Notebook. This allows for quick testing and debugging.

**Impact on Performance**
While Python's high-level nature and dynamic typing can lead to slower performance compared to some compiled languages like C++, the difference is often negligible for many applications. You can use libraries written in faster languages or optimize your code for performance-critical tasks.

**Optionally object-oriented but doesn’t force you to be (unlike Java)**
Python supports object-oriented programming (OOP) which is useful for organizing and managing larger codebases and a good choice for developing large-scale software applications.

## Why use Python
### The basics
**Free, open-source, and cross-platform**
- Cost-Effective: Python is free to download and use making it accessible to everyone. There are no licensing fees or costs associated with it.
- Open Source: Being open source, Python's source code is publicly available. You can inspect, modify, and distribute it fostering a collaborative environment.
- Cross-Platform: Python works on various operating systems including Windows, macOS, and Linux. This cross-platform compatibility means you can run your Python programs on any device without modifications.

**Scientific Libraries and Community**
- Scientific Libraries: Python boasts a plethora of scientific libraries such as NumPy, SciPy, Pandas, and Matplotlib. These libraries simplify complex mathematical computations, data manipulation, and visualization tasks.
- Community Support: Python has a large and passionate user community especially in scientific and academic circles. This community contributes to a wealth of resources, tutorials, and forums where you can seek help and share knowledge.

**Popularity in Data Science and Machine Learning**
Python is a go-to language for data science due to its comprehensive library ecosystem. Python offers a wide range of libraries and frameworks specifically designed for machine learning and data science making it easier for developers to implement ML algorithms. Such as NumPy, Pandas, PyTorch, Scikit-learn, TensorFlow, and Keras.

**Low learning curve**
Python's straightforward syntax and readability make learning easier than other programming languages. Beginners can quickly pick up the basics and start coding.

### The Technical Stuff
**Advanced Data Structures**
Python includes advanced data structures such as dictionaries (key-value pairs) and tuples (immutable sequences). These structures are efficient and easy to use which helps in organizing and managing.

**Flexibility**
You can use Python for scripting small tasks, developing complete applications, or anything in between.

**Human-Readable Syntax**
Python's syntax is designed to read and write easily. It uses indentation to define code blocks which enforces clean and readable code.

**Reproducible**
Python is free to use and Python code can be easily shared across different platforms and machines. This is especially useful in collaborative environments fostering transparency and collaboration.

### Summary
Learning Python is beneficial because it is free, open-source, and cross-platform making it accessible and versatile for a wide range of applications. Its extensive libraries, strong community support, straightforward syntax, and powerful data science and machine learning capabilities make it an ideal choice for beginners and experts.

## Where to use Python at Tufts
Python is available in most computer labs at Tufts University.

## What is that called? Terminology related to Python
**Kernel**  
In the context of computing and programming, a kernel is the core part of an operating system or an interactive computing environment. In Python, especially in environments like Jupyter notebooks, the kernel is the process that runs the user’s code. It receives input, executes it, and sends the output back to the front-end interface.

**Virtual Environment**  
A virtual environment is an isolated environment created to manage dependencies for different projects. Each virtual environment can have its own set of installed packages separate from the global Python environment which helps avoid conflicts between project dependencies.

**Python Distribution**  
A Python distribution is a package that includes the Python interpreter, the standard library, and often additional libraries and tools to help you get started with Python development. Examples include Anaconda and the official CPython distribution.

**Python Interpreter**  
The Python interpreter is the software that reads and executes Python code. It converts Python code into machine code that the computer’s hardware can understand. Common interpreters include CPython, PyPy, Jython, and IronPython.

**Python Module**  
A Python module is a single file containing Python code. Modules allow you to organize your Python code into manageable sections and they can be imported and used in other Python programs.

**Python Package**  
A Python package is a collection of modules organized in directories. Each package in Python contains a special `__init__.py` file making it easy to group related modules together.

**Python Library**    
A Python library is a collection of related modules and packages that provide specific functionalities making it easier to perform common tasks. Libraries are often broader and more comprehensive than individual packages.

**Pip (pip install)**   
Pip is the package installer for Python. It allows you to install and manage additional libraries and dependencies that are not included in the standard Python distribution. The command `pip install` is used to install a package from the Python Package Index (PyPI).

**Conda (conda install)**  
Conda is an open-source package management and environment management system that runs on Windows, macOS, and Linux. It can be used to install and manage software packages and dependencies including those outside the Python ecosystem. The command `conda install` is used to install packages from the Anaconda repository.

**File format: .py**  
A .py file is a plain text file containing Python code. It is the standard file extension for Python scripts.

**File format: .ipynb**  
An .ipynb file is an interactive Python notebook file used by Jupyter Notebooks. It allows you to combine executable code, narratives, visualizations, and other multimedia resources into a single document.

## How to get started with Python:
### How to install Python

**One option: Directly download Python to the computer**
Installing Python – [Download Python](https://wiki.python.org/moin/BeginnersGuide/Download)

**Best option: Anaconda – a Python distribution**
- Free and cross-platform
- Simple graphical interface
- Contains most packages
- Package manager
- Virtual environments
- Jupyter Notebook
- Spyder

### How to run Python script
**Option 1 - Command Line**
Interactive and text-based: the original way to control the computer and interact with your computer using text commands.

**Operating system:**
- **Windows**: Command Prompt and PowerShell
- **Linux and macOS**: Terminal

Also called a console – a common term for the command line interface. Anaconda has an Anaconda Prompt, a command line interface provided by the Anaconda distribution of Python.

**Option 2 - Write & Run** – code editor (file extension: .py)
Get a good text editor to write your Python code; some popular choices include:
- Sublime Text
- Atom
- Notepad++
- VS Code

Install Python extension within the software (you need to have Python installed on your local computer). Write your code in a text editor and save it with a `.py` extension. Execute the command in your command line interface (Command Prompt, Terminal, or Anaconda Prompt): `python filename.py` or run it directly within the editor like VS Code. It connects the terminal as well; the Conda will still work.

**Option 3 - Integrated Development Environment (IDE)**
All-in-one tool for programming providing a comprehensive environment for coding, helping with syntax, debugging, and more. Examples of IDE:
- **Spyder**: Comes with Anaconda and is great for data science.
- **PyCharm**: Powerful IDE used in data science and general Python development.
- **Thonny**: Designed for beginners providing a simple and clear interface.
- **Visual Studio Code**: This is a very powerful and versatile IDE for many types of code including Python. Additionally, you can use notebooks in this IDE which we discuss below.

**Option 4 – Notebook** 
Best option for data analysis and visualization. Notebooks are ideal for keeping a record of your work and integrating notes, code, and output all in one place. You can run and re-run code snippets individually. These code snippets are referred to as cells.

**Options for Notebooks:**
- **Jupyter Notebook**: The original Python notebook ships with Anaconda and runs on a local server allowing access to local storage.
  - Runs on a local server
  - Access local storage
  - Available on the Tufts HPC
- **Google Colab**: A web-based notebook that runs on Google servers providing an easy start with many pre-loaded libraries and integration with GitHub and Google Drive. 100% ONLINE: [colab.research.google.com](https://colab.research.google.com)
  - No Python installation needed
  - Most libraries pre-loaded
  - GPU and TPU acceleration available
  - Easier to collaborate and start off with

**Drawbacks:**
- Google-dependent
- Must upload all files
- Resources are capped
- Can only use `pip` for installing packages

### A summary of comparing the four options

| Feature         | Command Line              | Text Editor              | IDE                          | Notebook                      |
|-----------------|---------------------------|--------------------------|-----------------------------|------------------------------|
| Description     | Direct interaction with the system's shell or terminal | Simple text-based code editing | Integrated development environment with comprehensive tools | Interactive environment for writing and running code in chunks |
| Ease of Use     | Basic, requires knowledge of commands | Simple, user-friendly    | Advanced, user-friendly     | Highly user-friendly, especially for data analysis |
| Setup Complexity| Low, Python must be installed | Low, text editor installation | High, IDE installation and setup | Medium, installation of Jupyter or equivalent |
| Features        | Limited to command-line tools | Basic syntax highlighting, minimal features | Code completion, debugging, version control, project management | Inline code execution, visualization, markdown support |
| Best For        | Quick scripts, command-line tasks | Simple scripts, small projects | Large projects, full software development lifecycle | Data science, machine learning, exploratory data analysis |
| Example Tools   | Python Shell, Command Prompt, Terminal | Notepad++, Sublime Text, VS Code (as text editor) | PyCharm, VS Code (as IDE), Spyder | Jupyter Notebook, Google Colab |
| Code Execution  | Sequential, one command at a time | Sequential via command line or terminal | Integrated, can run, debug, and test within the environment | Interactive, allows running code in cells, supports re-running individual cells |
| Debugging       | Basic, print statements    | Basic, print statements  | Advanced, built-in debugging tools | Basic, some support through print statements or magic commands |
| Version Control | External tools (e.g. Git) | External tools (e.g. Git)| Integrated, built-in support for Git | External tools (e.g. Git)    |
| Visualization   | Limited, via external commands (e.g. matplotlib plots in separate windows) | Limited, via external commands | Good, integrated support for visualization libraries | Excellent, inline visualization directly in the notebook |
| Documentation   | Limited, help commands    | Limited, external documentation | Integrated, documentation and help features | Excellent, can include markdown and rich text alongside code |

For all our Python tutorials, we will use Notebooks to organize the text, code, and results. We use this format as it allows us to step through notes, annotations, and code clearly with results being shown for each cell.

### Workflow for preparing each Python notebook
1. Open the GitHub link from Uku to find the original Collab notebook.
2. Go to File > Save to Drive.
3. Share the Notebook with kyle.m.monahan@gmail.com as Editor.
4. Add the note for viewers to Save a Copy in Drive (see your notebook that we edited together for the text).
5. Then copy the Viewer access link to this notebook and add that link to the markdown file that will go on the website: 
   - This is meant to be a walk-through for you running this code in your own environment. 
   - If you would like to get started with Python, [click here](#). This is optional as you can use a browser-based environment (below). 
   - If you want to run the code interactively in a browser-based environment (Google Collab), [click here](#).

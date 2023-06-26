<h1>Fuzzy Logic Mental Health Diagnosis</h1>

<p>This project uses fuzzy logic to diagnose the mental health condition of a person based on their behavior, speech and medical history. The project is implemented in Python using the scikit-fuzzy library and the matplotlib library for visualization.</p>

<h2>How it works</h2>

<p>The project defines three input variables: behavior, speech and medical history. Each variable has three linguistic terms: normal, moderate and abnormal for behavior; coherent, mildly disorganized and disorganized for speech; and minimal, moderate and significant for medical history. The input variables are represented by Gaussian membership functions with different parameters.</p>

<p>The output variable is the mental health condition, which also has three linguistic terms: stable, moderate and severe. The output variable is also represented by Gaussian membership functions with different parameters.</p>

<p>The project defines five rules to infer the output variable from the input variables. The rules are:</p>

<ul> <li>If behavior is normal and speech is coherent and medical history is minimal then mental health condition is stable</li> <li>If behavior is abnormal or speech is disorganized then mental health condition is severe</li> <li>If medical history is significant and (behavior is moderate or speech is mildly disorganized) then mental health condition is severe</li> <li>If behavior is moderate and speech is mildly disorganized and medical history is moderate then mental health condition is moderate</li> <li>If behavior is normal and (speech is coherent or medical history is minimal) then mental health condition is stable</li> </ul>

<p>The project uses the Mamdani method to perform fuzzy inference and the centroid method to defuzzify the output.</p>

<h2>How to use it</h2>

<p>The project has three files: fuzzy_system_with_ui.py, fuzzy_system.ipynb and validation.ipynb. The .py file can be run as a Python script and the .ipynb files can be run as Jupyter notebooks.</p>

<p>The fuzzy_system_with_ui.py file has a graphical user interface (GUI) that allows the user to enter the values of the input variables using sliders. The GUI also displays the membership functions of the input and output variables and the diagnosis result as a number and a category.</p>

<p>The fuzzy_system.ipynb file shows plots for the antecedents and consequents of the fuzzy system. Additionally, the fuzzy_system.ipynb file saves and loads the fuzzy system to a file using pickle.</p>

<p>The validation.ipynb file uses a test dataset to evaluate the performance of the fuzzy system. It calculates the accuracy and precision of the system for different classes of the output variable.</p>

<p>To use the project, follow these steps:</p>

<ol> <li>Install the required libraries: scikit-fuzzy, matplotlib, numpy, tkinter</li> <li>Run the .py or .ipynb file of your choice</li> <li>For fuzzy_system_with_ui.py: <ul> <li>Adjust the sliders to enter the values of behavior, speech and medical history</li> <li>Click on the “Diagnose” button to get the diagnosis result</li> <li>Click on the “Show Membership Functions” button to see the membership functions</li> </ul> </li> <li>For fuzzy_system.ipynb: <ul> <li>Run the code cells to see the plots for the antecedents and consequents</li> <li>Run the code cells to save and load the fuzzy system using pickle</li> </ul> </li> <li>For validation.ipynb: <ul> <li>Load the test dataset from test_data.xlsx</li> <li>Run the code cells to generate random values for each linguistic term of each input variable</li> <li>Run the code cells to predict the output variable using the fuzzy system</li> <li>Run the code cells to calculate and print the accuracy and precision of the system</li> </ul> </li> </ol>

<h2>Example</h2>

<p>Here are some examples of using the project:</p>

<h3>Using fuzzy_system_with_ui.py or fuzzy_system.ipynb</h3>


<p>In this example, the input values are:</p>

<ul> <li>Behavior: 80</li> <li>Speech: 70</li> <li>Medical History: 60</li> </ul>

<p>The diagnosis result is:</p>

<ul> <li>Diagnosis: 66.67</li> <li>Diagnosis: Moderate</li> </ul>

<p>The membership functions are shown in the figure below:</p>

<img src=“membership_functions.png” alt=“Membership Functions”>

<h3>Using validation.ipynb</h3>


<p>In this example, the test dataset has 10 rows with different values for behavior, speech, medical history and expected mental health condition. The code generates random values for each linguistic term of each input variable. The code then predicts the mental health condition using the fuzzy system and compares it with the expected value. The code also calculates and prints the accuracy and precision of the system for different classes of the output variable.</p>

<p>The accuracy of the system is 0.7. The precision of the system for severe class is 1.0.</p>

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import tkinter as tk
import numpy as np

# Define Antecedents
behavior = ctrl.Antecedent(np.arange(0, 101, 1), 'Behavior')
speech = ctrl.Antecedent(np.arange(0, 101, 1), 'Speech')
medical_history = ctrl.Antecedent(np.arange(0, 101, 1), 'Medical History')

# Define Consequents
mental_health_condition = ctrl.Consequent(np.arange(0, 101, 1), 'Mental Health Condition')

# Define the membership functions for behavior
behavior['Normal'] = fuzz.gaussmf(behavior.universe, 0, 15)
behavior['Moderate'] = fuzz.gaussmf(behavior.universe, 50, 15)
behavior['Abnormal'] = fuzz.gaussmf(behavior.universe, 100, 15)

# Define the membership functions for speech
speech['Coherent'] = fuzz.gaussmf(speech.universe, 0, 15)
speech['Mildly Disorganized'] = fuzz.gaussmf(speech.universe, 50, 15)
speech['Disorganized'] = fuzz.gaussmf(speech.universe, 100, 15)

# Define the membership functions for medical history
medical_history['Minimal'] = fuzz.gaussmf(medical_history.universe, 0, 15)
medical_history['Moderate'] = fuzz.gaussmf(medical_history.universe, 50, 15)
medical_history['Significant'] = fuzz.gaussmf(
    medical_history.universe, 100, 15)

# Define the membership functions for the output variable
mental_health_condition['Stable'] = fuzz.gaussmf(
    mental_health_condition.universe, 0, 15)
mental_health_condition['Moderate'] = fuzz.gaussmf(
    mental_health_condition.universe, 50, 15)
mental_health_condition['Severe'] = fuzz.gaussmf(
    mental_health_condition.universe, 100, 15)

# Define the rules
rule1 = ctrl.Rule(behavior["Normal"] & speech["Coherent"] &
                  medical_history["Minimal"], mental_health_condition["Stable"])
rule2 = ctrl.Rule(
    (behavior["Abnormal"] | speech["Disorganized"]), mental_health_condition["Severe"])
rule3 = ctrl.Rule(medical_history["Significant"] & (
    behavior["Moderate"] | speech["Mildly Disorganized"]), mental_health_condition["Severe"])
rule4 = ctrl.Rule(behavior["Moderate"] & speech["Mildly Disorganized"]
                  & medical_history["Moderate"], mental_health_condition["Moderate"])
rule5 = ctrl.Rule(behavior["Normal"] & (
    speech["Coherent"] | medical_history["Minimal"]), mental_health_condition["Stable"])

# Create the control system
mental_health_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
mental_health_diagnosis = ctrl.ControlSystemSimulation(mental_health_ctrl)

# Define Membership Function Drawing


def show_membership_functions():
    # Create a new figure and plot the membership functions
    fig = plt.figure()
    mental_health_condition.view(sim=mental_health_diagnosis)
    plt.title('Membership Functions')

    # Create a canvas to display the plot
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Add a toolbar to the canvas
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Define the UI
def diagnose_mental_health():
    # Get the input values from the UI
    beahve = float(behavior_input.get())
    spee = float(speech_input.get())
    his = float(history_input.get())

    # Pass the input values to the control system
    mental_health_diagnosis.input['Behavior'] = beahve
    mental_health_diagnosis.input['Speech'] = spee
    mental_health_diagnosis.input['Medical History'] = his

    # Compute the output value
    mental_health_diagnosis.compute()

    # Get the output value from the control system
    diagnosis = mental_health_diagnosis.output['Mental Health Condition']

    # Display the diagnosis number
    diagnosis_label_number.config(
        text='Diagnosis: ' + str(round(diagnosis, 2)))

    # Display the diagnosis category
    if diagnosis <= 33:
        diagnosis_label_category.config(text='Diagnosis: Stable')
    elif diagnosis <= 66:
        diagnosis_label_category.config(text='Diagnosis: Moderate')
    else:
        diagnosis_label_category.config(text='Diagnosis: Severe')

    # Show the membership functions in a new window
    show_membership_functions()


# Create the UI
root = tk.Tk()
root.title('Mental Health Diagnosis')

behavior_label = tk.Label(root, text='Behavior:')
behavior_label.grid(row=0, column=0)
behavior_input = tk.Entry(root)
behavior_input.grid(row=0, column=1)

speech_label = tk.Label(root, text='Speech:')
speech_label.grid(row=1, column=0)
speech_input = tk.Entry(root)
speech_input.grid(row=1, column=1)

history_label = tk.Label(root, text='Medical History:')
history_label.grid(row=2, column=0)
history_input = tk.Entry(root)
history_input.grid(row=2, column=1)

diagnose_button = tk.Button(root, text='Diagnose',
                            command=diagnose_mental_health)
diagnose_button.grid(row=3, column=0)

diagnosis_label_number = tk.Label(root, text='Diagnosis Number: ')
diagnosis_label_number.grid(row=3, column=1)

diagnosis_label_category = tk.Label(root, text='Diagnosis Category: ')
diagnosis_label_category.grid(row=4, column=1)

root.mainloop()

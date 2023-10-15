### Driver Drowsiness Detection System

This repository contains a Python program designed to detect driver drowsiness by analyzing eye movements and yawing patterns in real-time. Detecting drowsiness is critical for road safety as it helps prevent accidents caused by driver fatigue.

### Installation and Configuration:

**Prerequisites:**

-   Ensure you have Anaconda installed on your system.

**Step 1: Update Conda**

bash

`conda update conda` 

**Step 2: Update Anaconda**

bash

`conda update anaconda` 

**Step 3: Create a Virtual Environment**

bash

`conda create -n env_dlib python=3.8` 

**Step 4: Activate the Virtual Environment**

bash

`conda activate env_dlib` 

**Step 5: Install dlib**

bash

`conda install -c conda-forge dlib` 

If all these steps are completed successfully, dlib will be installed in the virtual environment `env_dlib`. Use this environment for running the drowsiness detection system.

**Step to Deactivate the Virtual Environment**

bash

`conda deactivate` 

### Running the Drowsiness Detection System:

**Step 1: Clone the Repository**

bash

`git clone <repository_url>` 

**Step 2: Install System Requirements**

bash

`pip install -r requirements.txt` 

**Step 3: Set up and Run the System**

bash

`python app1.py` 

**Step 4: Access the System**

-   Open your web browser.
-   In the address bar, type `localhost:8000`. If port 8000 is already in use, Flask will automatically choose another available port and display it in the command prompt. In that case, access the system using `localhost:<port_number>`.

### About the Drowsiness Detection System:

The drowsiness detection system uses computer vision and machine learning to monitor driver behavior, focusing on two primary factors:

1.  **Eye Blink Detection:**
    
    -   The system calculates the Euclidean distance between the driver's eyelids. An increase in this distance, which often occurs when a person's eyes are closed or nearly closed, indicates drowsiness.
    -   When the system detects an unusual increase in eyelid distance over a certain period, it triggers an alert to notify the driver to stay alert.
2.  **Yawning Pattern Detection:**
    
    -   The program also monitors the driver's yawning patterns, a common sign of drowsiness.
    -   By analyzing facial expressions and movements, the system recognizes yawning and issues an alert if excessive yawning is detected.

### Safety Reminder:

This system is a valuable tool for drowsiness detection, but it should not replace the driver's responsibility to remain alert and attentive while driving. Always prioritize safe driving practices and use this system as an additional safety measure.

By following these steps, you can install, configure, and use the driver drowsiness detection system to enhance road safety.

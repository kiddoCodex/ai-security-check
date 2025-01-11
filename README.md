

# AI-Powered System Security Hardening

This repository contains an AI-powered system security assessment tool, inspired by Lynis, which analyzes and assesses the security status of a Linux system. The system uses machine learning to predict whether the system is secure or at risk based on certain configuration features, and it provides actionable recommendations to improve security.

### Key Features:
- **AI-based security assessment**: The system uses machine learning models to predict whether the system is secure or at risk.
- **Automated feature collection**: Automatically collects system features such as SSH root login, firewall status, disk usage, etc.
- **Actionable recommendations**: Based on the analysis, the tool provides suggestions to harden the system's security posture.
- **Minimal dependencies**: Built with Bash and Python, requiring only essential system libraries and Python packages.

## Table of Contents
1. [Installation](#installation)
2. [How It Works](#how-it-works)
3. [Usage](#usage)
4. [Machine Learning Model](#machine-learning-model)
5. [Contributing](#contributing)
6. [License](#license)

---

## Installation

### Prerequisites

1. **System requirements**: The tool is designed to run on Linux-based systems, including Kali, AlmaLinux, and Ubuntu.
2. **Python 3**: Ensure you have Python 3 and `pip` installed on your system.

```bash
sudo apt update
sudo apt install python3 python3-pip python3-dev

	3.	Required Python libraries: Install the required Python packages for machine learning.

pip3 install scikit-learn pandas

	4.	Clone the repository: Clone the repository to your local machine.

git clone https://github.com/yourusername/ai-security-hardening.git
cd ai-security-hardening

How It Works

The tool collects security-related features from the system, such as:
	•	SSH root login status
	•	Firewall status
	•	File permissions
	•	System updates
	•	Disk usage

These features are passed to a pre-trained machine learning model which predicts whether the system is secure or at risk. Based on the prediction, the tool provides a set of actionable recommendations to improve the security of the system.

Key Components:
	•	ai_security_check.sh: The main Bash script that collects system features and triggers the prediction process.
	•	predict_security.py: The Python script that loads the trained machine learning model and makes predictions based on the collected features.
	•	ml_model.py: The Python script used to train the machine learning model.

Usage

Once you have the repository set up and dependencies installed, you can run the tool as follows:
	1.	Make the Bash script executable:

chmod +x ai_security_check.sh

	2.	Run the security check:

sudo ./ai_security_check.sh

The script will:
	•	Collect security-related system features.
	•	Pass them to the trained machine learning model.
	•	Predict whether the system is secure or at risk.
	•	Provide actionable recommendations based on the model’s prediction.

Machine Learning Model

The machine learning model is trained using system configuration data, where features represent system security settings, and the target variable indicates whether the system is secure (1) or at risk (0).

Training the Model

The model is trained on labeled data that includes features such as:
	•	SSH root login status
	•	Firewall status
	•	Permissions of critical files
	•	System update status
	•	Disk usage status

You can train the model using the ml_model.py script by providing your own labeled data or by modifying the existing sample dataset. After training, the model is saved using Pickle for future predictions.

python3 ml_model.py

This will train the model and save it as system_security_model.pkl.

Making Predictions

Once the model is trained and saved, the system can predict the security status based on the collected features. The predict_security.py script is used for this purpose.

Contributing

If you want to contribute to the development of this project, feel free to fork the repository, create a branch, and submit a pull request. You can contribute by:
	•	Adding new security checks
	•	Improving the machine learning model
	•	Enhancing the feature collection scripts
	•	Adding more actionable recommendations

License

This project is licensed under the MIT License - see the LICENSE file for details.

Example Output:

When you run the tool, you will see the following output:

Collecting system features...
Features collected: 1, 1, 1, 1, 1
Predicting security status...
The system is secure.

If the system is at risk, you will receive a recommendation:

The system is at risk. Recommendations:
- Disable root login for SSH
- Enable firewall
- Secure file permissions
- Run system updates
- Check disk usage

Feel free to modify or extend this tool to suit your needs. If you encounter any issues, open an issue in the GitHub repository, and we’ll be happy to assist you.


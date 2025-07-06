# Klick Klack  
### Empowering Security Teams with Typing Biometrics  

**Klick Klack** is a slim, powerful Machine Learning application that recognizes users based on their typing patterns.  

It leverages an XGBoost Random Forest model to train on unique typing behaviors across key clusters, offering a novel biometric approach to user identification.

---

## Features  
- Typing-based user recognition  
- Interface for collecting typing data  
- Machine learning pipeline using XGBoost  
- Customizable dataset input and testing  

---

## Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/randomguy70/Klick-Klack
cd Klick-Klack
mkdir Raw_Data
mkdir Test_Data
```

### 2. Set Up Dependencies

I recommend using a virtual environment with [Anaconda](https://www.anaconda.com/docs/getting-started/anaconda/install) to avoid dependency conflicts.

```bash
# Create and activate conda environment
conda create --name klick-klack python=3.9
conda activate klick-klack
```

*Note: You'll need to run `conda activate klick-klack` each time you reopen your terminal.*

### 3. Install Required Libraries

```bash
pip install pandas xgboost scikit-learn
```

> `tkinter` comes preinstalled with most Python distributions, but you can always manually install.

---

## How to Use Klick Klack

### 1. Collect Typing Data
Run the interface with:
```bash
python app.py
```
This allows users to type sample articles. Their keystrokes will be logged and saved to `Raw_Data/`.  
*Tip: The more data you collect per user, the more accurate the model will be.*

### 2. Train the Model
After collecting enough data:
```bash
python main.py
```
This script trains Klick Klack to recognize users based on the typing samples stored in `Raw_Data/`.

> Want to use a different folder name? Modify `main.py` accordingly.

### 3. Identify a User
Place the keystroke data you want to identify in the `Test_Data/` folder, then run:
```bash
python predict.py
```
Predictions will be printed to the console.

---

## 😔 Windows Users
You're not forgotten — but you may need to tweak a few commands (e.g., paths and terminal syntax). If you get stuck, feel free to reach out.

---

## 🧪 Inspiration

This project drew inspiration from [this article on keystroke biometrics](https://www.sciencedirect.com/science/article/pii/S2352340923006091?via%3Dihub).

---

## 📬 Contributing

If you encounter bugs, have questions, or just want to geek out about typing biometrics — **please reach out** or open an issue. I'd love to hear from you.

---

## 🎉 Enjoy!
(Yes, this is an essential step.)

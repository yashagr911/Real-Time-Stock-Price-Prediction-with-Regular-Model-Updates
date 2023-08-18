import subprocess
import os

def run_script(script_path):
    subprocess.run(["python","-m", script_path], check=True)

if __name__ == "__main__":
    # Define paths to the three modules
    model_evaluation_script = "scripts.model_evaluation"
    model_train_script = "scripts.model_training"
    model_update_script = "scripts.model_update"

    # Run the scripts in sequence
    if not os.path.exists("models/saved_models/trained_model.pkl"):
        run_script(model_train_script)

    run_script(model_evaluation_script)
    run_script(model_update_script)

    print("All scripts executed successfully.")

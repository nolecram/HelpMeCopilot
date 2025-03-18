import os
import subprocess
import shutil
import argparse

def list_experiments(base_dir):
    experiments = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(('.py', '.ipynb', '.js', '.rb', '.cpp', '.c', '.sh', '.tf')):
                experiments.append(os.path.join(root, file))
    return experiments

def run_experiment(file_path):
    try:
        if file_path.endswith('.py'):
            subprocess.run(['python3', file_path], check=True)
        elif file_path.endswith('.sh'):
            subprocess.run(['bash', file_path], check=True)
        elif file_path.endswith('.ipynb'):
            print(f"Jupyter Notebook detected: {file_path}. Please run it manually.")
        elif file_path.endswith(('.cpp', '.c')):
            executable = file_path.rsplit('.', 1)[0]
            subprocess.run(['gcc', file_path, '-o', executable], check=True)
            subprocess.run([f'./{executable}'], check=True)
        elif file_path.endswith('.rb'):
            subprocess.run(['ruby', file_path], check=True)
        elif file_path.endswith('.js'):
            subprocess.run(['node', file_path], check=True)
        elif file_path.endswith('.tf'):
            print(f"Terraform file detected: {file_path}. Please validate and apply it manually.")
        else:
            print(f"Unsupported file type for: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {file_path}: {e}")

def check_dependencies():
    missing_dependencies = []

    # Check for Node.js
    if not shutil.which("node"):
        missing_dependencies.append("Node.js (node)")

    # Check for GCC
    if not shutil.which("gcc"):
        missing_dependencies.append("GCC")

    # Check for Sybase libraries (sybfront.h)
    sybase_header_path = "/usr/include/sybfront.h"  # Adjust this path as needed
    if not os.path.exists(sybase_header_path):
        missing_dependencies.append("Sybase libraries (sybfront.h)")

    return missing_dependencies

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run experiments in the repository.")
    parser.add_argument(
        "--experiment",
        type=str,
        help="Path to a specific experiment to run. If not provided, all experiments will be run.",
    )
    return parser.parse_args()

def main():
    args = parse_arguments()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    experiments_dir = os.path.join(base_dir, 'src')

    print("Checking dependencies...")
    missing_dependencies = check_dependencies()

    if missing_dependencies:
        print("\nThe following dependencies are missing:")
        for dep in missing_dependencies:
            print(f"- {dep}")
        print("\nPlease install the missing dependencies and try again.")
        return

    if args.experiment:
        print(f"\nRunning specified experiment: {args.experiment}")
        run_experiment(args.experiment)
        return

    print("\nListing all experiments...")
    experiments = list_experiments(experiments_dir)

    if not experiments:
        print("No experiments found.")
        return

    print("\nExperiments found:")
    for i, exp in enumerate(experiments, 1):
        print(f"{i}. {exp}")

    print("\nRunning experiments...")
    for exp in experiments:
        print(f"\nRunning: {exp}")
        run_experiment(exp)

if __name__ == "__main__":
    main()
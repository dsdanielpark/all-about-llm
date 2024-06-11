import subprocess

def sync_submodules():
    # Initialize and update submodules
    subprocess.run(["git", "submodule", "update", "--init", "--recursive"], check=True)
    # Sync and update submodules to the latest version
    subprocess.run(["git", "submodule", "foreach", "git", "pull", "origin", "main"], check=True)

def main():
    try:
        sync_submodules()
        print("All submodules are synced to the latest version.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while syncing submodules: {e}")

if __name__ == "__main__":
    main()

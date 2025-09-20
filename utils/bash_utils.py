
import subprocess


def open_file_in_vscode(file_path):
    subprocess.run(f"code {file_path}", check=True, text=True, shell=True)


def run_bash_commmand(command):
    subprocess.run(
        args=command,
        check=True,
        text=True,
        shell=True,
    )


def open_url(url):
    subprocess.run(f"brave-browser {url}", check=True, text=True, shell=True)


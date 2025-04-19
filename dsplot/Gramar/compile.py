import subprocess
import os


antlr = "antlr-4.13.2-complete.jar"
grammar_file = "GraphPlot.g4"
output_dir = "generated"
language = "Python3"

command = [
        "java", "-jar", antlr,
        f"-Dlanguage={language}",
        "-o", output_dir,
        "-visitor",
        grammar_file,
    ]


if __name__ == "__main__":
    os.makedirs(output_dir, exist_ok=True)
    try:
        subprocess.run(command, check=True)
        print("successfully compiled grammar!")

    except subprocess.CalledProcessError as e:
        print("compile error:", e)

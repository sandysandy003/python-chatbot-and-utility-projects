
import ast

def explain_line(line):
    text = line.strip()

    if not text:
        return "An empty line used for readability."
    if text.startswith("#"):
        return "A comment for people reading the code."
    if text.startswith("import ") or text.startswith("from "):
        return "Imports functionality from a Python module."
    if text.startswith("def "):
        return "Defines a reusable function."
    if text.startswith("class "):
        return "Defines a class for grouping data and behavior."
    if text.startswith("if "):
        return "Checks a condition and runs code if it is true."
    if text.startswith("elif "):
        return "Checks another condition if earlier conditions were false."
    if text == "else:":
        return "Runs when the preceding conditions were not met."
    if text.startswith("for "):
        return "Repeats a block of code for items in a sequence."
    if text.startswith("while "):
        return "Repeats code while a condition remains true."
    if text.startswith("return"):
        return "Sends a result back from a function."
    if text.startswith("print("):
        return "Displays information on the screen."
    if "=" in text and "==" not in text and not text.startswith(("if ", "elif ")):
        return "Assigns a value to a variable or target."
    if text.startswith(("try:", "except", "finally:")):
        return "Handles errors or code that must run during error handling."
    return "A Python statement or expression. Its exact purpose depends on the surrounding code."

print("=" * 45)
print("PYTHON CODE EXPLAINER")
print("Paste Python code below. Type END on a separate line when finished.")
print("Type EXIT to quit.")
print("=" * 45)

while True:
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "EXIT" and not lines:
            raise SystemExit
        if line.strip().upper() == "END":
            break
        lines.append(line)

    code_text = "\n".join(lines)

    if not code_text.strip():
        print("No code entered. Try again.")
        continue

    try:
        ast.parse(code_text)
        print("\nSyntax check: Python could parse this code.")
    except SyntaxError as error:
        print(f"\nSyntax issue near line {error.lineno}: {error.msg}")

    print("\nLine-by-line explanation:")
    for number, line in enumerate(lines, start=1):
        print(f"{number}. {line.strip() or '(blank line)'}")
        print(f"   Explanation: {explain_line(line)}")

    print("\nNote: These explanations use simple rules, not an AI model.")
    print("\nPaste another snippet, or type EXIT to quit.")

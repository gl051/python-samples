from pathlib import Path

print("Building a path to the README.md for pathlib sample")
p = Path(__file__)
# building a path is very intuitive
readme = p.cwd() / "samples/pathlib/README.md"
print(f"type: {type(readme)}")
print(f"string: {readme}")
print(f"is a file: {readme.is_file()}")
print(f"parts: {readme.parts}")
print(f"absolute: {readme.absolute}")
print(f"name, steam, suffix: {readme.name}, {readme.stem}, {readme.suffix}")
print(f"parent: {readme.parent}")

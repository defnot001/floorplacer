import os
import sys

from pathlib import Path

def prompt_file_path(question: str) -> Path:
  while True:
    raw_path: str = input(question)
    path: Path = Path(raw_path.strip('"'))

    # Expand the ~ character to the user's home directory
    expanded_path: Path = path.expanduser()

    if not expanded_path.is_absolute():
      executable_dir: Path = Path(sys.argv[0]).parent
      absolute_path: Path = executable_dir / expanded_path
    else:
      absolute_path: Path = expanded_path

    normalized_path: Path = absolute_path.resolve()

    if not normalized_path.exists():
      print(f"Error: The path {normalized_path} does not exist.")
      continue

    if not normalized_path.is_file():
      print(f"Error: The path {normalized_path} is not a file.")
      continue

    if normalized_path.suffix != ".litematic":
      print(f"Error: The file {normalized_path} is not a .litematic file.")
      continue

    return normalized_path

def prompt_placeholder_block() -> str:
  block_answer = input("Enter the placeholder block (leave empty for minecraft:beacon): ").strip()

  if block_answer == "":
    print(f"Using the placeholder block minecraft:beacon")
    return "minecraft:beacon"
  else:
    with_namespace = add_namespace_if_not_exists(block_answer)

    if is_valid_resource_location(with_namespace):
      return with_namespace
    else:
      print(f"Error: The resource location {with_namespace} is invalid.")
      return prompt_placeholder_block()

def add_namespace_if_not_exists(resource: str) -> str:
  if not resource.startswith("minecraft:"):
    return f"minecraft:{resource}"
  else:
    return resource

def is_valid_resource_location(resource: str) -> bool:
  return resource.startswith("minecraft:") and resource.count(":") == 1


def wait_for_exit(status: int = 0):
  input("Press Enter to exit...")
  sys.exit(status)
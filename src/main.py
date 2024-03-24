from prompt import prompt_file_path
from prompt import prompt_placeholder_block
from prompt import wait_for_exit

from typing import Tuple

type Coordinates = Tuple[int, int, int]

placeholder_block = "minecraft:beacon"
DATA_PALETTE = [
    "minecraft:white_shulker_box",
    "minecraft:orange_shulker_box", 
    "minecraft:magenta_shulker_box", 
    "minecraft:light_blue_shulker_box", 
    "minecraft:yellow_shulker_box", 
    "minecraft:lime_shulker_box", 
    "minecraft:pink_shulker_box",
    "minecraft:gray_shulker_box", 
    "minecraft:light_gray_shulker_box", 
    "minecraft:cyan_shulker_box", 
    "minecraft:purple_shulker_box", 
    "minecraft:blue_shulker_box", 
    "minecraft:brown_shulker_box", 
    "minecraft:green_shulker_box", 
    "minecraft:red_shulker_box"
]


def main():
    schematic_file_path = prompt_file_path("Enter the path to the schematic file: ")
    rom_file_path = prompt_file_path("Enter the path to the ROM file: ")
    placeholder_block = prompt_placeholder_block()


    print(f"Successfully loaded the schematic file from {schematic_file_path}")
    print(f"Successfully loaded the ROM file from {rom_file_path}")
    print(f"Using the placeholder block {placeholder_block}")

    wait_for_exit()


if __name__ == "__main__":
    main()

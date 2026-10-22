from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from BaseClasses import Item, ItemClassification
from worlds.minecraft_fabric.item.item_manager import UnprocessedMinecraftItem, ProcessedMinecraftItem
from worlds.minecraft_fabric.item.minecraft_items import get_all_items
from worlds.minecraft_fabric.options_consts import *

if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


# Gets all the items, and creates a dictionary for them
def get_item_table():
    items = {}
    unprocessed_items: list[UnprocessedMinecraftItem] = get_all_items()
    for i, item in enumerate(unprocessed_items):
        version_modids = item.version_modids.copy()
        earliest_version_index = ALL_VERSIONS.index(item.default_earliest_version)
        for j, ver in enumerate(ALL_VERSIONS):
            if ver not in version_modids and j >= earliest_version_index:
                version_modids.update({ver: item.default_modid})
        items.update({item.name: ProcessedMinecraftItem(item.name, item.classification, item.fill_type, i + 1, version_modids)})
    return items

# All Items
item_table: dict[str, ProcessedMinecraftItem] = get_item_table()

# ITEM GETTING #########################################################################################################

def is_filler(item: ProcessedMinecraftItem):
    return item.classification == ItemClassification.filler or item.classification == ItemClassification.useful

def get_junk_items():
    items_to_get = []
    for item in item_table.values():
        if is_filler(item) and item.fill_type == 0:
            items_to_get.append(item)
    return items_to_get

def get_progression_bl_items():
    items_to_get = []
    for item in item_table.values():
        if item.fill_type == 1:
            items_to_get.append(item)
    return items_to_get

def get_blank_filler():
    items_to_get = []
    for item in item_table.values():
        if is_filler(item) and item.fill_type == 2:
            items_to_get.append(item)
    return items_to_get

def get_item(name: str):
    retv = item_table.get(name)
    assert retv is not None
    return retv

# ITEM CREATION ########################################################################################################

def create_item(world: FabricMinecraftWorld, name: str):
    item = get_item(name)
    return Item(item.name, item.classification, item.item_id, world.player)

def can_add_to_pool(world: FabricMinecraftWorld, name: str):
    item = get_item(name)
    target_version = ALL_VERSIONS[world.options.target_game_version.value]
    return target_version in item.version_modids and item.version_modids[target_version] in world.options.enabled_mods.value

def add_item_to_pool(world: FabricMinecraftWorld, name: str, total_items: int):
    if can_add_to_pool(world, name):
        world.multiworld.itempool.append(create_item(world, name))
        total_items -= 1
    return total_items

def add_items_to_pool(world: FabricMinecraftWorld, name: str, count: int, total_items: int):
    for i in range(count):
        total_items = add_item_to_pool(world, name, total_items)
    return total_items

def add_optional_item(world: FabricMinecraftWorld, value: str, item: str, total_items: int):
    if value in world.options.randomized_abilities.value:
        return add_item_to_pool(world, item, total_items)
    else:
        return total_items
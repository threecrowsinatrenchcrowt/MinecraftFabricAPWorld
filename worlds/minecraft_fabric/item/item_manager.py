from dataclasses import dataclass
from BaseClasses import ItemClassification

@dataclass
class UnprocessedMinecraftItem:
    name: str
    classification: ItemClassification
    fill_type: int
    default_modid: str
    default_earliest_version: str
    version_modids: dict[str, str]

@dataclass
class ProcessedMinecraftItem:
    name: str
    classification: ItemClassification
    fill_type: int
    item_id: int
    version_modids: dict[str, str]

def needed(name: str, default_modid: str = "minecraft", default_earliest_version: str = "1.20.1", version_modids: dict[str, str] = {}):
    return UnprocessedMinecraftItem(name, ItemClassification.progression, 0, default_modid, default_earliest_version, version_modids)

def needed_bl(name: str, default_modid: str = "minecraft", default_earliest_version: str = "1.20.1", version_modids: dict[str, str] = {}):
    return UnprocessedMinecraftItem(name, ItemClassification.progression, 1, default_modid, default_earliest_version, version_modids)

def useful(name: str, default_modid: str = "minecraft", default_earliest_version: str = "1.20.1", version_modids: dict[str, str] = {}):
    return UnprocessedMinecraftItem(name, ItemClassification.useful, 0, default_modid, default_earliest_version, version_modids)

def filler(name: str, default_modid: str = "minecraft", default_earliest_version: str = "1.20.1", version_modids: dict[str, str] = {}):
    return UnprocessedMinecraftItem(name, ItemClassification.filler, 0, default_modid, default_earliest_version, version_modids)

def blank_filler(name: str, default_modid: str = "minecraft", default_earliest_version: str = "1.20.1", version_modids: dict[str, str] = {}):
    return UnprocessedMinecraftItem(name, ItemClassification.filler, 2, default_modid, default_earliest_version, version_modids)

def trap(name: str, default_modid: str = "minecraft", default_earliest_version: str = "1.20.1", version_modids: dict[str, str] = {}):
    return UnprocessedMinecraftItem(name, ItemClassification.trap, 0, default_modid, default_earliest_version, version_modids)
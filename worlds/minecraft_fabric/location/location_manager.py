
from dataclasses import dataclass
from worlds.minecraft_fabric.options_consts import *

@dataclass
class MinecraftLocation:
    name: str
    default_modid: str
    default_earliest_version: str
    version_modids: dict[str, str]
    index: int = -1
    
def loc(name: str, default_modid: str = "minecraft", default_earliest_version: str = "1.20.1", version_modids: dict[str, str] = {}):
    version_modids_processed = version_modids.copy()
    earliest_version_index = ALL_VERSIONS.index(default_earliest_version)
    for j, ver in enumerate(ALL_VERSIONS):
        if ver not in version_modids and j >= earliest_version_index:
            version_modids_processed.update({ver: default_modid})
    return MinecraftLocation(name, default_modid, default_earliest_version, version_modids_processed)
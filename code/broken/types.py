import warnings
from math import pi as PI
from typing import Set, TypeAlias

# Ignore mostly NumPy warnings
warnings.filterwarnings("ignore")

# # Custom types and utilities
Unchanged: TypeAlias = None
Channels:  TypeAlias = int
URL:       TypeAlias = str

# Units
Seconds:   TypeAlias = float
Minutes:   TypeAlias = float
Hours:     TypeAlias = float
Hertz:     TypeAlias = float
Samples:   TypeAlias = int
Bytes:     TypeAlias = int
Degrees:   TypeAlias = float
Radians:   TypeAlias = float
BPM:       TypeAlias = float
Pixel:     TypeAlias = int

# Recurring math constants
TAU:     float = (2*PI)
SQRT2:   float = (2**0.5)
SQRT3:   float = (3**0.5)
SQRT5:   float = (5**0.5)
SQRT_PI: float = (PI**0.5)

# Recurring computing constants
KB:  int = (1000)
MB:  int = (KB*1000)
GB:  int = (MB*1000)
TB:  int = (GB*1000)
PB:  int = (TB*1000)
KiB: int = (1024)
MiB: int = (KiB*1024)
GiB: int = (MiB*1024)
TiB: int = (GiB*1024)
PiB: int = (TiB*1024)

class FileExtensions:
    Audio:     Set[str] = {".wav", ".ogg", ".flac", ".mp3"}
    Image:     Set[str] = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"}
    Video:     Set[str] = {".mp4", ".mkv", ".webm", ".avi", ".mov", ".wmv", ".flv"}
    Font:      Set[str] = {".ttf", ".otf", ".woff", ".woff2"}
    Midi:      Set[str] = {".mid", ".midi"}
    Soundfont: Set[str] = {".sf2", ".sf3"}
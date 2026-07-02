__version__ = "0.1.0"

# Load .env as early as possible: several submodules read model names into
# module-level constants at import time (e.g. daily.DAILY_MODEL =
# os.environ.get("DAILY_MODEL", "glm-5.1")). Because `python -m research_news.X`
# imports this package before any submodule, calling load_dotenv() here ensures
# those constants see the .env values instead of falling back to hardcoded
# defaults. (Submodules also call load_dotenv() inside their entrypoints; that's
# harmless — load_dotenv is idempotent — but by then the constants are already
# bound, so this early call is the one that actually takes effect.)
from dotenv import load_dotenv as _load_dotenv

_load_dotenv()

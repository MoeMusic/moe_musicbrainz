"""Register the sub-modules of your plugin and expose their API functions."""

import moe
from moe import config

from . import my_plugin
from .my_plugin import *

__all__ = []
__all__.extend(my_plugin.__all__)


@moe.hookimpl
def plugin_registration():
    """Register the modules of your plugin."""
    config.CONFIG.pm.register(my_plugin, "my plugin")

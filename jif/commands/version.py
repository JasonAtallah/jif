import logging
from pkg_resources import get_distribution

logger  = logging.getLogger('jif')

def version():
    __version__ = get_distribution('jif').version
    logger.info(f'Version: {__version__}')
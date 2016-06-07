from setuptools import setup
from src import version
import shutil

# Keep a copy of the current version.py to restore it after installation.
shutil.copyfile('src/version.py', 'src/version.py.bak')
# Overwrite the version file before it's installed (and unable to read the repository).
with open('src/version.py','w') as f:
    f.write('VERSION="{}"\nPROTOCOL_VERSION="{}"\n'.format(version.VERSION, version.PROTOCOL_VERSION))


try:
    setup(
        name="electrum-server",
        version="1.0",
        scripts=['run_electrum_server.py','electrum-server'],
        install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
        package_dir={
            'electrumserver':'src'
        },
        py_modules=[
            'electrumserver.__init__',
            'electrumserver.utils',
            'electrumserver.storage',
            'electrumserver.deserialize',
            'electrumserver.networks',
            'electrumserver.blockchain_processor',
            'electrumserver.server_processor',
            'electrumserver.processor',
            'electrumserver.version',
            'electrumserver.ircthread',
            'electrumserver.stratum_tcp'
        ],
        description="Bitcoin Electrum Server",
        author="Thomas Voegtlin",
        author_email="thomasv@electrum.org",
        license="MIT Licence",
        url="https://github.com/spesmilo/electrum-server/",
        long_description="""Server for the Electrum Lightweight Bitcoin Wallet"""
    )
finally:
    # Always restore version.py
    shutil.move('src/version.py.bak', 'src/version.py')

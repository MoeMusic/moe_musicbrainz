###########
Musicbrainz
###########
This is a plugin for Moe utilizing the musicbrainz metadata source and provides the following features:

* Musicbrainz as an import souce.
* Update musicbrainz collections automatically on import or manually.
* Various API functions.

Configuration
=============
``username``
    Musicbrainz username.
``password``
    Musicbrainz password.

Collections
~~~~~~~~~~~
The following options involve auto updating a specific collection on musicbrainz, and should be specified under a ``musicbrainz.collection`` block as shown:

.. code-block:: toml

    [musicbrainz.collection]
    collection_id = "123"

.. important::

    Utilizing any of the collections functionality requires setting your musicbrainz username and password as described above.

``collection_id``
    Musicbrainz collection to automatically update.

``auto_add = False``
    Whether to automatically add new releases in the library to the collection defined in ``collection_id``.

``auto_remove = False``
    Whether to automatically remove releases from ``collection_id`` when removed from the library.

Custom Fields
=============
This plugin adds the following custom fields:

Track Fields
~~~~~~~~~~~~
* ``mb_track_id`` - musicbrainz track id

Album Fields
~~~~~~~~~~~~
* ``mb_album_id`` - musicbrainz album aka release id

Command-line Iterface
=====================
This plugin adds the following commands:

mbcol
~~~~~
Used to sync a musicbrainz collection with musicbrainz releases in the library. The collection synced is the one specified under ``collection_id`` in the user config.

.. code-block:: bash

    moe mbcol [-h] [-a | -e] [--add | --remove] query

By default, the musicbrainz collection will be set to the releases found in the queried items. If tracks or extras are queried, their associated album releases will be synced with the collection.

Positional Arguments
~~~~~~~~~~~~~~~~~~~~
``query``
    Query your library for items to sync your collection with. See the Moe query docs for more info.

Optional Arguments
~~~~~~~~~~~~~~~~~~
``-h, --help``
    Display the help message.
``-a, --album``
    Query for matching albums instead of tracks.
``-e, --extra``
    Query for matching extras instead of tracks.
``--add``
    Add releases to the collection.
``--remove``
    Remove releases from the collection.

***
API
***
``moe_musicbrainz``

.. automodule:: moe_musicbrainz.mb_core
   :members:
   :show-inheritance:

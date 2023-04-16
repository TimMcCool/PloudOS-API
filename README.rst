PloudosAPI
==========

Warning: This library is deprecated.

An API Wrapper to interact with ploudos.com
-----------------------------------------------

With PloudosAPI, you can start and stop your PloudOS servers, get the
server console, run commands and do lots of other stuff.

Install the package
-------------------

To install the package, run the command ``pip install PloudosAPI``.

Get started
-----------

Log in to your PloudOS account:

::

   import PloudosAPI
   session = PloudosAPI.login("username", "password") #replace with your PloudOS username / password

Get a PloudOS server by its id:

::

   server = session.get_server("server_id")

... or by its name:

::

   servers = session.get_servers_with_name("name")
   server = servers[0]

Start the server:

::

   server.start()

.. warning::
   Keeping a server online with a Bot or other programs is against the PloudOS `Terms of Service <https://ploudos.com/rules/>`_.

Get the server console and execute commands:
(Only works when the server is running)

::

   console = server.get_console()

   server.post_to_console("command") #replace with the command you want to run

Stop the PloudOS server:

::

   server.stop()


Get your PloudOS servers:

::

   my_servers = session.servers()

``session.servers()`` returns a dict with your PloudOS servers that looks like this:

.. code:: json

   {
       "owned" : [
           PloudosAPI.PloudosServer,
           PloudosAPI.PloudosServer,
           ...
       ],
       "shared" : [
           PloudosAPI.PloudosServer,
           PloudosAPI.PloudosServer,
           ...
       ]
   }

Other stuff
-----------

Force a server shutdown:

::

   server.force_stop()

Regenerate the server’s world:

::

   server.regenerate_world(*, seed="your_seed", hardcore=False)


Share the server with a PloudOS user:

::

   server.share_add("user")

Remove the access of a PloudOS user:

::

   server.share_remove("user")

Ban / Unban a minecraft player from the server:

::

   server.ban("player")

   server.unban("player")

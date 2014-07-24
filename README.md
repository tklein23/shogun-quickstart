shogun-quickstart
=================

Complete example project to allow quickstart with SHOGUN Machine Learning Toolbox

Installation
------------

Step 1: Get your copy of the shogun-quickstart project.

```
$ git clone https://github.com/tklein23/shogun-quickstart
```

Step 2: Clone the SHOGUN Machine Learning Toolbox sources and data repository.
Note this step will download approximately 250 MB of data.

```
$ git clone https://github.com/shogun-toolbox/shogun shogun
$ cd shogun
$ git submodule update --init
```

Step 3: Building and installing SHOGUN Machine Learning Toolbox.  The provided script
will build C++ library and modular interfaces for Java and Python and install it to
a local directory.  No superuser rights needed.  Here you go:

```
$ ../shogun-quickstart/scripts/setup-shogun.sh build-devel
$ . build-devel/activate-shogun
```

Congratulations!  Your local SHOGUN install is now complete.

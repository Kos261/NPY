Homework
########

Make ``homework_exercise`` package ``pip`` installable.
After bundle with ``python -m build --sdist`` archive should contain every files need to use package.
Remember to declare all package dependencies.

To test if package is properly installable run ``test_package.py`` script, like bellow: 

  .. code-block:: bash

    $ pip install .
    ...
    $ python test_package.py
    fun1:
     [[0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0.]]
    fun2: 18             


.. rm -rf dist/ build/ *.egg-info                                     delete dist
.. python -m build --sdist                                            build package
.. pip install dist/homework_exercise-0.1.0.tar.gz --force-reinstall  reinstall
.. pytest                                                             testing 
    

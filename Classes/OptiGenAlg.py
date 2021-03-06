# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Optimization/OptiGenAlg.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from inspect import getsource
from cloudpickle import dumps, loads
from ._check import CheckTypeError
from ._check import InitUnKnowClassError
from .OutputMultiOpti import OutputMultiOpti
from .OptiProblem import OptiProblem


class OptiGenAlg(FrozenClass):
    """Genetic algorithm class"""

    VERSION = 1

    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        multi_output=-1,
        selector=None,
        crossover=None,
        mutator=None,
        p_cross=0.9,
        p_mutate=0.1,
        size_pop=40,
        nb_gen=100,
        problem=-1,
        logger_name="Pyleecan.OptiGenAlg",
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if multi_output == -1:
            multi_output = OutputMultiOpti()
        if problem == -1:
            problem = OptiProblem()
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "multi_output" in list(init_dict.keys()):
                multi_output = init_dict["multi_output"]
            if "selector" in list(init_dict.keys()):
                selector = init_dict["selector"]
            if "crossover" in list(init_dict.keys()):
                crossover = init_dict["crossover"]
            if "mutator" in list(init_dict.keys()):
                mutator = init_dict["mutator"]
            if "p_cross" in list(init_dict.keys()):
                p_cross = init_dict["p_cross"]
            if "p_mutate" in list(init_dict.keys()):
                p_mutate = init_dict["p_mutate"]
            if "size_pop" in list(init_dict.keys()):
                size_pop = init_dict["size_pop"]
            if "nb_gen" in list(init_dict.keys()):
                nb_gen = init_dict["nb_gen"]
            if "problem" in list(init_dict.keys()):
                problem = init_dict["problem"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Initialisation by argument
        self.parent = None
        # multi_output can be None, a OutputMultiOpti object or a dict
        if isinstance(multi_output, dict):
            self.multi_output = OutputMultiOpti(init_dict=multi_output)
        else:
            self.multi_output = multi_output
        self.selector = selector
        self.crossover = crossover
        self.mutator = mutator
        self.p_cross = p_cross
        self.p_mutate = p_mutate
        self.size_pop = size_pop
        self.nb_gen = nb_gen
        # problem can be None, a OptiProblem object or a dict
        if isinstance(problem, dict):
            self.problem = OptiProblem(init_dict=problem)
        else:
            self.problem = problem
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OptiGenAlg_str = ""
        if self.parent is None:
            OptiGenAlg_str += "parent = None " + linesep
        else:
            OptiGenAlg_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.multi_output is not None:
            tmp = (
                self.multi_output.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            OptiGenAlg_str += "multi_output = " + tmp
        else:
            OptiGenAlg_str += "multi_output = None" + linesep + linesep
        if self._selector[1] is None:
            OptiGenAlg_str += "selector = " + str(self._selector[1])
        else:
            OptiGenAlg_str += (
                "selector = " + linesep + str(self._selector[1]) + linesep + linesep
            )
        if self._crossover[1] is None:
            OptiGenAlg_str += "crossover = " + str(self._crossover[1])
        else:
            OptiGenAlg_str += (
                "crossover = " + linesep + str(self._crossover[1]) + linesep + linesep
            )
        if self._mutator[1] is None:
            OptiGenAlg_str += "mutator = " + str(self._mutator[1])
        else:
            OptiGenAlg_str += (
                "mutator = " + linesep + str(self._mutator[1]) + linesep + linesep
            )
        OptiGenAlg_str += "p_cross = " + str(self.p_cross) + linesep
        OptiGenAlg_str += "p_mutate = " + str(self.p_mutate) + linesep
        OptiGenAlg_str += "size_pop = " + str(self.size_pop) + linesep
        OptiGenAlg_str += "nb_gen = " + str(self.nb_gen) + linesep
        if self.problem is not None:
            tmp = self.problem.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OptiGenAlg_str += "problem = " + tmp
        else:
            OptiGenAlg_str += "problem = None" + linesep + linesep
        OptiGenAlg_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return OptiGenAlg_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.multi_output != self.multi_output:
            return False
        if other.selector != self.selector:
            return False
        if other.crossover != self.crossover:
            return False
        if other.mutator != self.mutator:
            return False
        if other.p_cross != self.p_cross:
            return False
        if other.p_mutate != self.p_mutate:
            return False
        if other.size_pop != self.size_pop:
            return False
        if other.nb_gen != self.nb_gen:
            return False
        if other.problem != self.problem:
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OptiGenAlg_dict = dict()
        if self.multi_output is None:
            OptiGenAlg_dict["multi_output"] = None
        else:
            OptiGenAlg_dict["multi_output"] = self.multi_output.as_dict()
        if self.selector is None:
            OptiGenAlg_dict["selector"] = None
        else:
            OptiGenAlg_dict["selector"] = [
                dumps(self._selector[0]).decode("ISO-8859-2"),
                self._selector[1],
            ]
        if self.crossover is None:
            OptiGenAlg_dict["crossover"] = None
        else:
            OptiGenAlg_dict["crossover"] = [
                dumps(self._crossover[0]).decode("ISO-8859-2"),
                self._crossover[1],
            ]
        if self.mutator is None:
            OptiGenAlg_dict["mutator"] = None
        else:
            OptiGenAlg_dict["mutator"] = [
                dumps(self._mutator[0]).decode("ISO-8859-2"),
                self._mutator[1],
            ]
        OptiGenAlg_dict["p_cross"] = self.p_cross
        OptiGenAlg_dict["p_mutate"] = self.p_mutate
        OptiGenAlg_dict["size_pop"] = self.size_pop
        OptiGenAlg_dict["nb_gen"] = self.nb_gen
        if self.problem is None:
            OptiGenAlg_dict["problem"] = None
        else:
            OptiGenAlg_dict["problem"] = self.problem.as_dict()
        OptiGenAlg_dict["logger_name"] = self.logger_name
        # The class name is added to the dict fordeserialisation purpose
        OptiGenAlg_dict["__class__"] = "OptiGenAlg"
        return OptiGenAlg_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.multi_output is not None:
            self.multi_output._set_None()
        self.selector = None
        self.crossover = None
        self.mutator = None
        self.p_cross = None
        self.p_mutate = None
        self.size_pop = None
        self.nb_gen = None
        if self.problem is not None:
            self.problem._set_None()
        self.logger_name = None

    def _get_multi_output(self):
        """getter of multi_output"""
        return self._multi_output

    def _set_multi_output(self, value):
        """setter of multi_output"""
        check_var("multi_output", value, "OutputMultiOpti")
        self._multi_output = value

        if self._multi_output is not None:
            self._multi_output.parent = self

    # Optimization results containing every output
    # Type : OutputMultiOpti
    multi_output = property(
        fget=_get_multi_output,
        fset=_set_multi_output,
        doc=u"""Optimization results containing every output""",
    )

    def _get_selector(self):
        """getter of selector"""
        return self._selector[0]

    def _set_selector(self, value):
        """setter of selector"""
        try:
            check_var("selector", value, "list")
        except CheckTypeError:
            check_var("selector", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._selector = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._selector = [None, None]
        elif callable(value):
            self._selector = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    # Selector of the genetic algorithm
    # Type : function
    selector = property(
        fget=_get_selector,
        fset=_set_selector,
        doc=u"""Selector of the genetic algorithm""",
    )

    def _get_crossover(self):
        """getter of crossover"""
        return self._crossover[0]

    def _set_crossover(self, value):
        """setter of crossover"""
        try:
            check_var("crossover", value, "list")
        except CheckTypeError:
            check_var("crossover", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._crossover = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._crossover = [None, None]
        elif callable(value):
            self._crossover = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    # Crossover of the genetic algorithm
    # Type : function
    crossover = property(
        fget=_get_crossover,
        fset=_set_crossover,
        doc=u"""Crossover of the genetic algorithm""",
    )

    def _get_mutator(self):
        """getter of mutator"""
        return self._mutator[0]

    def _set_mutator(self, value):
        """setter of mutator"""
        try:
            check_var("mutator", value, "list")
        except CheckTypeError:
            check_var("mutator", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._mutator = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._mutator = [None, None]
        elif callable(value):
            self._mutator = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    # Mutator of the genetic algorithm
    # Type : function
    mutator = property(
        fget=_get_mutator,
        fset=_set_mutator,
        doc=u"""Mutator of the genetic algorithm""",
    )

    def _get_p_cross(self):
        """getter of p_cross"""
        return self._p_cross

    def _set_p_cross(self, value):
        """setter of p_cross"""
        check_var("p_cross", value, "float", Vmin=0, Vmax=1)
        self._p_cross = value

    # Probability of crossover
    # Type : float, min = 0, max = 1
    p_cross = property(
        fget=_get_p_cross, fset=_set_p_cross, doc=u"""Probability of crossover"""
    )

    def _get_p_mutate(self):
        """getter of p_mutate"""
        return self._p_mutate

    def _set_p_mutate(self, value):
        """setter of p_mutate"""
        check_var("p_mutate", value, "float", Vmin=0, Vmax=1)
        self._p_mutate = value

    # Probability of mutation
    # Type : float, min = 0, max = 1
    p_mutate = property(
        fget=_get_p_mutate, fset=_set_p_mutate, doc=u"""Probability of mutation """
    )

    def _get_size_pop(self):
        """getter of size_pop"""
        return self._size_pop

    def _set_size_pop(self, value):
        """setter of size_pop"""
        check_var("size_pop", value, "int", Vmin=1)
        self._size_pop = value

    # Size of the population
    # Type : int, min = 1
    size_pop = property(
        fget=_get_size_pop, fset=_set_size_pop, doc=u"""Size of the population"""
    )

    def _get_nb_gen(self):
        """getter of nb_gen"""
        return self._nb_gen

    def _set_nb_gen(self, value):
        """setter of nb_gen"""
        check_var("nb_gen", value, "int", Vmin=1)
        self._nb_gen = value

    # Number of generations
    # Type : int, min = 1
    nb_gen = property(
        fget=_get_nb_gen, fset=_set_nb_gen, doc=u"""Number of generations"""
    )

    def _get_problem(self):
        """getter of problem"""
        return self._problem

    def _set_problem(self, value):
        """setter of problem"""
        check_var("problem", value, "OptiProblem")
        self._problem = value

        if self._problem is not None:
            self._problem.parent = self

    # Problem to solve
    # Type : OptiProblem
    problem = property(
        fget=_get_problem, fset=_set_problem, doc=u"""Problem to solve"""
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    # Name of the logger to use
    # Type : str
    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use""",
    )

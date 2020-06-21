# ActMS - python interface

This is a library to enable mental simulation of multiple cognitive models within the Cognitive Architecture ACT-R.

ACT-MS (ACT-R Mental Simulation) is an implementation based on the Python dispatcher included in ACT-R Version 7.13, which facilitates the use of ACT-R commands within a Python environment and vice versa. ACT-MS incorporates multiple functions relevant to coordinate the simultaneous simulation of multiple ACT-R models. An exemplary use case can be found in the below publication [1].

Overall, the library contains methods to: 

- **(1)** - to forward and exchange parameters between the metamodel and the submodels.
- **(2)** - save the exchanged simulation parameters in a dictionary.
- **(3)** - enable utility learning over multiple ACT-R runs by saving the utility of one run respectively.


[1] <cite> new paper </cite> 

![Exemplary Visicon](mentalsimulation.png)


## Installation

```bash
pip install git+https://github.com/seblum/actms
```


## Quick-Start

Take a look at the [examples](examples) folder for an exemplary use case.

```lisp

(p simulate-middle-submodel
  =goal>
    state               simulate-submodel
    action              =actionnumber
  =imaginal>
==>
  =imaginal>
  =goal>
    state               free
    action              =actionnumber
!eval! ("simulate-submodel" "middle-model" =actionnumber)
  )

```

```lisp

  (P action-retour-1
    =goal>
     state              action-1
     action 			1
    ?manual>   
      state             free
    =imaginal>
        response        =duration
   ==>
    +manual>              
      cmd      press-key     
      key      =duration
    -imaginal>
    =goal>
      state 			idle
      action 			idle
!eval! ("return-from-submodel" =duration 1 "retrieve-action" "resultactionone")
    )

```

```python

ms.init_actms()
        ms.writeToProtocol("Session", ses)
        ms.writeToProtocol("timesRun", tr)

        actr.run_until_condition("end-program", True)       

        tmpresult = ms.getProtocol()
        printer = pd.concat([printer, tmpresult])

```

## Files

- **actms.py** - Contains the interface of ACT-MS and methods to load a user data set into the visicon of ACT-R.

- **actr.py** - Contains the dispatcher of ACT-R version 7.13., which is necessary to form a connection between python and ACT-R.


## Example

- **RUN-metamodel.py** 
- **EF-submodel-left.lisp**
- **EF-metamodel.lisp** 

## TODO
Possible additional feature to add:

<<<<<<< HEAD
- [ ] Add more dynamic and additional possibilites to save simulation parameters
- [ ] Add more dynamic read in for data
- [ ] Add debugging support 

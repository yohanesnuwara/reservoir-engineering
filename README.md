# Python Worked Examples and Problems of Worldwide Reservoir Engineering Textbooks

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## SPE Textbook Vol. 8 *Fundamental Principles of Reservoir Engineering* by Brian F. Towler

![brian towler book](https://user-images.githubusercontent.com/51282928/74505368-89a88e80-4f29-11ea-80a6-e563b6237729.jpg)

Original copy of this book can be purchased from [SPE Bookstore](https://store.spe.org/Fundamental-Principles-of-Reservoir-Engineering-P27.aspx)

All examples and problems from the book are worked on Python language.

The book contains **14 units** and **1 Appendix**. In this repo, each unit has 3 folders: 

* `data`: compilation of data in CSV tables for examples and problems
* `functions`: compilation of functions from the Equations in the book to execute certain purposed calculations
* `notebooks`: Jupyter notebooks of worked examples and practice problems

|**No.**|**Chapter Name**|**Link**|
|:--:|:--:|:--:|
|2|Review of Rock and Fluid Properties|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%202%20Review%20of%20Rock%20and%20Fluid%20Properties)|
|3|Reservoir Statics|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%203%20Reservoir%20Statics)|
|4|Volumetrics|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%204%20Volumetrics)|
|5|Material Balance|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%205%20Material%20Balance/notebook)|
|6|Single-Phase-Fluid Flow in Porous Media|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%206%20Single-Phase-Fluid%20Flow%20in%20Porous%20Media)|
|7|Introduction to Well-Test Analysis|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%207%20Introduction%20to%20Well-Test%20Analysis)|
|8|Aquifer Influx|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%208%20Aquifer%20Influx)|
|9|Dry-Gas Reservoirs|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%209%20Dry-Gas%20Reservoirs)|
|10|Gas-Condensate Reservoirs|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%2010%20Gas-Condensate%20Reservoirs/notebook)|
|11|Undersaturated-Oil Reservoirs|[Folder](https://github.com/yohanesnuwara/reservoir-engineering/tree/master/Unit%2011%20Undersaturated-Oil%20Reservoirs/notebook)|
|12|Saturated-Oil Reservoirs|Soon|
|13|Fluid Distribution and Displacement|Soon|
|14|Decline-Curve Analysis|Soon|

**Appendix A** contains values and tabulations for solving certain equations in the book. 

## External Tools that I Use

* [**Online OCR**](https://www.onlineocr.net/): Optical Character Recognition (OCR) online to convert paper Tables from the book (printed) to a digital Excel spreadsheet 
* **Microsoft Excel**: to save the digitized Table as a CSV format 

## Citation BibTex

If you use this repository for a certain purpose, please make this citation

> Y. Nuwara, reservoir-engineering, (2020), GitHub repository, https://github.com/yohanesnuwara/reservoir-engineering

BibTex registry:

```
@misc{Nuwara2020,
  author = {Nuwara, Y.},
  title = {reservoir-engineering},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/yohanesnuwara/reservoir-engineering}},
  commit = {b1a8a2e3de8a9f53febf5ca8452e564bc34c9c76}
}
```

## Friends who Helped Completing the Missing Puzzles

Thanks ... for ...

* **Mark Burgoyne**, (Principal Reservoir Engineer in Santos), helping with solution to solve numerically the transient flow problems (Chapter 5) based on [Klins et al (1988) SPE-15433-PA paper](https://www.onepetro.org/journal-paper/SPE-15433-PA). The code to calculate the aquifer flow [here](https://github.com/yohanesnuwara/reservoir-engineering/blob/master/Unit%206%20Single-Phase-Fluid%20Flow%20in%20Porous%20Media/functions/aquifer_flow.py). Mark's [Monograph-20-Examples](https://github.com/vinomarkus/Monograph-20-Examples) repo has inspired me to create this repo. 

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

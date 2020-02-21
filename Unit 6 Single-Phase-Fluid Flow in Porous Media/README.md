# Important Note for Unit 6

There are 6 **solutions** to solve the 1-phase-flow in porous media in Unit 6. 3 of solutions are in [Part 1 notebook](https://github.com/yohanesnuwara/reservoir-engineering/blob/master/Unit%206%20Single-Phase-Fluid%20Flow%20in%20Porous%20Media/notebook/6_examples_part1.ipynb), and the other last 3 solutions in [Part 2 notebook](https://github.com/yohanesnuwara/reservoir-engineering/blob/master/Unit%206%20Single-Phase-Fluid%20Flow%20in%20Porous%20Media/notebook/6_examples_part2.ipynb).

Most of these solutions are worked, except ones that include calculation using van Everdingen and Hurst **Table** in **Appendix**. Those which are not finished yet are:

* **Example 6.4** Calculation of Wellbore Flow Flowing Pressure with Constant Pressure at Outer Boundary (using **Table A-2**). Interpolation using `scipy.interpolate.griddata` fails. See: [Part 1 notebook](https://github.com/yohanesnuwara/reservoir-engineering/blob/master/Unit%206%20Single-Phase-Fluid%20Flow%20in%20Porous%20Media/notebook/6_examples_part1.ipynb)
* **Example 6.5** Calculation of Well Flow Rate with Constant Flowing Pressure (using **Table A-4** for **finite acting condition**). It's partly worked, only on the **infinite acting condition**. See: [Part 2 notebook](https://github.com/yohanesnuwara/reservoir-engineering/blob/master/Unit%206%20Single-Phase-Fluid%20Flow%20in%20Porous%20Media/notebook/6_examples_part2.ipynb)

**Example 6.3** using **Table A-1** succeeds because it does not need interpolation, only need rounding and `numpy.where` algorithm.

I need **more efficient algorithm** to find values and interpolate values in the tables. Solution will be published very soon.

Refer to: [Tips for Tabulation notebook](https://github.com/yohanesnuwara/reservoir-engineering/blob/master/tips_for_tabulation.ipynb)

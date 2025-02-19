# BioLabSim: Data Analysis for Biotechnology

## Introduction
This Jupyter book is BioLabSim: a collection of workflows to simulate different steps of strain engineering and fermentation in industrial biotechnology. The data is generated from a virtual organism simulation with various models of microbial metabolism, genetics and physiology {cite:p}`Liebal2023`. 

The compute environment works best with Python=3.9.21 (also 3.11.11), Pandas=2.2.2, Numpy=1.26.4, COBRA=0.29.1, Biopython=1.79, (Pip=24.1.2, Jupyter-client=6.1.12, Jinja2=3.1.5, Bokeh=3.6.2, Openpyxl=3.1.5).

The BioLabSim workflows are designed to help students and researchers in biotechnology to learn and practice data analysis in biotechnology. The workflows are based on the Python programming language and Jupyter Notebooks, which provide an interactive environment to write code, visualize data, and generate plots. The workflows cover various topics, including genetics, fermentation, metabolism, and genetic regulation, and are accompanied by additional materials to deepen the understanding of the underlying concepts. By working through these workflows, users can gain hands-on experience in data analysis and computational modeling in biotechnology, enhancing their skills and knowledge in this field.

## How to run the simulations
The simulations can be run in GitHub Codespaces or Google Colab. For Codespaces, login with your account to GitHub. Click on the green `Code` icon on the top of the repository description. Select the register card `Codespaces` and start a new instance. The Codespaces is a remote server space, with *e.g.* VSCode interface, that contains the full repository. You can navigate on the left side through the folder structure and open files to be displayed on the main screen. On the top right of the main screen the kernel can be selected.

For Google Colab, start login to your Google account and navigate to the main page at [https://colab.research.google.com](https://colab.research.google.com). In the `Open notebook` window, click on `GitHub` and enter the name `BioLabSim` in the search field. In the search results you can extract individual Jupyter Notebooks into Google Colab. The kernel is already preset, Python=3.11.11 works fine. Because in Colab Notebooks are retrieved from the GitHub as single files, internal links will stop working. You may need to manually copy over needed files with 
- `os.system('wget https://raw.githubusercontent.com/biolabsim/BioLabSim/refs/heads/master/requirements.txt')`

## Available workflows
|Name |Field |Content |Addition Material|Time, h|Developer|
|:-|:-|:-|:-|:-|:-|
|[Notebook Introduction](./Notebooks/PythonIntroduction.ipynb)|Programming|A tutorial to explore the important features of Jupyter Notebooks.|[Introduction to Jupyter Notebooks](https://mhasoba.github.io/TheMulQuaBio/notebooks/Appendix-JupyIntro.html)|0.5|Stephan Palkovits (RWTH)|
|[RecExpSim](./Notebooks/RecExpSim.ipynb)|Genetics|Simulation of recombinant protein expression and data analyses, including growth characterization, promoter sequence selection, cloning and expression.|$\cdot$ Propterties of mesophilic organisms [overview](https://application.wiley-vch.de/books/sample/3527335153_c01.pdf) (p. 18)<br> $\cdot$ Bacterial promoter architecture [review](https://doi.org/10.3390/biom5031245) (-10 and -35 box)<br>$\cdot$ GC-content [calculations](https://www.genelink.com/Literature/ps/R26-6400-MW.pdf)|3h|[Ulf Liebal](https://www.iamb.rwth-aachen.de/cms/iamb/Das-Institut/Team/Gruppe-Blank/Gruppenleitung/~ivuv/Ulf-Liebal/lidx/1/) (RWTH)<br>Iris Broderius (RWTH)|
|[FermProSim](./Notebooks/FermProSim.ipynb)|Fermentation|Parameter estimation of fermentation with Monod-equation.|$\cdot$ ...|1.5h|Jonathan Sturm (WHS)|
|[GroExpSim-Experiment](./Notebooks/GroExpSim_Nr1.ipynb)|Fermentation|Setup of growth experiments to identify optimal temperature, substrate concentrations, cultivation time, and sampling period.||1.5h|[Ulf Liebal](https://www.iamb.rwth-aachen.de/cms/iamb/Das-Institut/Team/Gruppe-Blank/Gruppenleitung/~ivuv/Ulf-Liebal/lidx/1/) (RWTH)|
|[GroExpSim-Data Analysis](./Notebooks/GroExpSim_Nr2.ipynb)|Fermentation|Data analysis of growth experiment to analyse biomass and substrate rates and yields.||1.5h|[Ulf Liebal](https://www.iamb.rwth-aachen.de/cms/iamb/Das-Institut/Team/Gruppe-Blank/Gruppenleitung/~ivuv/Ulf-Liebal/lidx/1/) (RWTH)|
|[GSMM+FBA_Start](./Notebooks/GSMM+FBA_Start.ipynb)|Metabolism|Introduction to genome scale model constraint based and reconstruction analysis (COBRA). Investigating and modifying existing models||1|[Ulf Liebal](https://www.iamb.rwth-aachen.de/cms/iamb/Das-Institut/Team/Gruppe-Blank/Gruppenleitung/~ivuv/Ulf-Liebal/lidx/1/) (RWTH)<br>Brigida Fabry (RWTH)|
|[GSMM+FBA_YieldsMutants](./Notebooks/GSMM+FBA_YieldsMutants.ipynb)|Metabolism|Analysis of models, FBA.||1|[Ulf Liebal](https://www.iamb.rwth-aachen.de/cms/iamb/Das-Institut/Team/Gruppe-Blank/Gruppenleitung/~ivuv/Ulf-Liebal/lidx/1/) (RWTH)<br>Brigida Fabry (RWTH)|
|[GSMM+FBA_GrowthCorr](./Notebooks/GSMM+FBA_OpolGrowthCorr.ipynb)|Metabolism|Model growth correlation and visualization.||1|[Ulf Liebal](https://www.iamb.rwth-aachen.de/cms/iamb/Das-Institut/Team/Gruppe-Blank/Gruppenleitung/~ivuv/Ulf-Liebal/lidx/1/) (RWTH)|
|[Genetic Logic Gates, vol1](./Notebooks/GenExpMod.ipynb)|Genetics|Introduction to genetic regulation and mathematical modelling with Hill equation.|[Elowitz & Bois, Caltech](https://biocircuits.github.io/chapters/01_intro_to_circuit_design.html)|1.5h|[Ulf Liebal](https://www.iamb.rwth-aachen.de/cms/iamb/Das-Institut/Team/Gruppe-Blank/Gruppenleitung/~ivuv/Ulf-Liebal/lidx/1/) (RWTH)|
|[Genetic Logic Gates, vol2](.//Notebooks/BioMotifSim.ipynb)|Genetics|Investigation of feedforward loops, representation of logic gates with mathematical models|[Elowitz & Bois, Caltech](https://biocircuits.github.io/chapters/04_ffls.html)|1.5h|[Ulf Liebal](https://www.iamb.rwth-aachen.de/cms/iamb/Das-Institut/Team/Gruppe-Blank/Gruppenleitung/~ivuv/Ulf-Liebal/lidx/1/) (RWTH)|
|[Metabolic Engineering Simulation (MetEngSim)](.//Notebooks/MetEngSim.ipynb)|Metabolism| Introduction to gene databases and metabolic maps.||1h|Paula Lanze (RWTH), [Ulf Liebal](https://www.iamb.rwth-aachen.de/cms/iamb/Das-Institut/Team/Gruppe-Blank/Gruppenleitung/~ivuv/Ulf-Liebal/lidx/1/) (RWTH)|
|Industrial Fermentation Simulation (IndFermSim)|Metabolism| Introduction to gene databases and metabolic maps.||1h|Bhavya Dutta (HSRW), Joachin Fensterle (HSRW)|

### How Complex Data Permeates Biotechnology
<!-- ```{margin}
<img src='Figures/Jupyter/FermProSim_Objective.png' alt='Variables in a fermentation'  width='250'/><br>
``` -->
Data analysis plays a crucial role in biotechnology by providing insights essential for optimizing fermentation processes. Effective fermentation necessitates precise control of variables such as nutrient concentrations, pH levels, and temperature. Monitoring and measuring these variables using advanced sensors and analytical tools generate data that informs decision-making and process adjustments. For instance, in microbial fermentation, understanding the dynamics of metabolite production and consumption is pivotal for achieving high yields and product quality {cite:p}`nielsen2016engineering`. Accurate data analysis enables biotechnologists to uncover patterns and correlations in the data, guiding the modification of fermentation conditions to enhance productivity and efficiency {cite:p}`Narayanan2020`. Without robust data analysis, harnessing the potential of biotechnological processes would be severely limited.
<!-- 
```{margin}
<img src='Figures/Jupyter/multi-omics.png' alt='Data diversity'  width='250'/><br>
``` -->
The integration of high-throughput measurement techniques {cite:p}`Wehrs2020` and omics technologies, such as genomics, proteomics, and metabolomics, has significantly elevated the complexity of data in biotechnology {cite:p}`Pinu2019`. These advanced methodologies capture an immense volume of molecular information, offering a comprehensive view of intricate biological processes. However, this expanded scope comes with a challenge – the data becomes more intricate and multifaceted. Traditional analytical methods struggle to cope with the sheer volume and intricacy of omics data, which encompasses intricate molecular interactions across various biological networks. This complexity demands the development and application of novel computational tools and algorithms to extract meaningful insights {cite:p}`Volk2020`. The advent of high-throughput and omics technologies has thus transformed biotechnological research, requiring a paradigm shift in data analysis approaches to fully exploit the potential of these data-rich techniques.

### Improving Biotech with New Computational Methods
<!-- ```{margin}
<img src='Figures/Jupyter/MetaEngSim_Segment_DNAMetabol.png' alt='New methods and analysis types'  width='250'/><br>
``` -->
As biotechnological data becomes increasingly complex and intricate, the demand for sophisticated analysis methods and advanced statistical techniques grows. The intricate nature of modern data, stemming from diverse sources such as omics technologies and high-throughput experiments, requires analytical approaches that can unravel intricate patterns and correlations. Techniques like machine learning, network analysis, and multivariate statistics are now crucial for extracting meaningful insights from such complex datasets  {cite:p}`Oliveira2019`. Moreover, the adoption of FAIR (Findable, Accessible, Interoperable, and Reusable) standards is essential to ensure that intricate biotechnological data remains comprehensible and shareable {cite:p}`Rehnert2022`. These standards facilitate data integration and collaboration, enabling researchers to collectively address intricate challenges and unlock new frontiers in biotechnology.

Paragraph about design-build-test-learn cycles and the automated strain design workflow.

:::{dropdown} Summary
* Data analysis is crucial in biotechnology, guiding effective fermentation through precise measurement of variables, such as nutrient levels and metabolite concentrations, to optimize microbial production systems.
* Integration of high-throughput measurement and omics technologies elevates data complexity, challenging traditional methods and demanding novel computational approaches for meaningful insights.
* Industrial biotechnology's intricate data necessitates advanced analysis methods like machine learning and network analysis, while FAIR standards ensure accessible and collaborative data management.
:::

---

## User Notes

To run BioLabSim directly choose among the following JupyterHubs:

- RWTHjupyter: RWTH Aachen University JupyterHub: [![](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/uliebal/RecExpSim/HEAD)

- RWTHjupyter: RWTH Aachen University JupyterHub: [![](https://jupyter.pages.rwth-aachen.de/documentation/images/badge-launch-rwth-jupyter.svg)](https://jupyter.rwth-aachen.de/hub/spawn?profile=biolabsim)

It is possible to download the examples in BioLabSim and run them locally. This requires the installation of packages to do the simulations, see [Developer Notes](DevopNotes).


(DevopNotes)=
## Developer Notes

### Setup project for local development

```bash

# Setup the python virtual environment next to it. (use Python 3.9)
python3.9 -m venv py39-env

# Activate your environment. (Broad topic that depends on what software and OS is used)
source py39-env/bin/activate

# Clone the repository to a nearby folder.
git clone https://git.rwth-aachen.de/ulf.liebal/biolabsim.git repo-biolabsim

# Enter the newly cloned repository.
cd repo-biolabsim

# Install all required python libraries.
pip install -r requirements.txt

# See the Notebook for examples on how to use the library.
```



## Contacts

*Ulf Liebal*

Institute of Applied Microbiology-iAMB, Aachen Biology and Biotechnology-ABBT, RWTH Aachen University, Worringerweg 1, 52074 Aachen Germany



<!-- Last update: 8 June, 2022

Contact: ulf.liebal@iamb.rwth-aachen.de -->

Licence: See LICENCE file @https://git.rwth-aachen.de/ulf.liebal/biolabsim, or @https://github.com/uliebal/BioLabSim

## References
:::{bibliography}
:::
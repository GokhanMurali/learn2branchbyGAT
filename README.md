# Project Structure

This branch contains the Elsevier template for a journal article. The structure of the project is as follows:
    
    ``` 
    ├── README.md
    ├── code
    ├── data
    ├── manuscript
    │   ├── src
    │   │   ├── figures
    │   │   ├── sections
    │   │   └── tables
    └── out
    ```

## `./code` folder

This folder contains the source code for the data analysis.

## `./data` folder

This folder contains the data used in the analysis. 
The data should be stored in a raw format and should not be modified.

## `./manuscript` folder

This folder contains the source files for the manuscript. The structure of the manuscript folder is as follows:

    ``` 
    ├── manuscript
    │   ├── src
    │   │   ├── figures
    │   │   ├── sections
    │   │   └── tables
    └── out

### `./src` folder

Contains the LaTeX files used to generate the manuscript.
`main.tex` is the source file that your Latex compiler will use to generate the paper.
To keep the code cleaner, the main sections of the paper are all located in the `sections` folder. 
In this way you will experience less merging issues when two or more people are working on the same manuscript.

`figures` and `tables` folders contain the figures and tables used in the manuscript.

### `./out` folder

This folder contains the output files generated by the Latex compiler.
Here you will find the PDF file of the manuscript.

### `./figures` folder

Import them from the `figures` folder using the `\includegraphics{}` command. [Figures - video tutorial](https://youtu.be/jg4t0xFDbdk)

### `./tables` folder

Import them from the `tables` folder using the `\input{}` command. 
* [Tables - Video tutorial](https://youtu.be/-sRYdfYMuhE)
* [How to use include command](https://youtu.be/V_eCCNlBuMo)

### Equations

[Equations - video tutorial](https://youtu.be/V4htbZeDUMU)

### Cite a document

[How to cite a document - video tutorial](https://youtu.be/cetKX6gWAIo)

### Code Listing

[Code listing - video tutorial](https://youtu.be/ByduYnAu2jM)

### Changing template

For your convenience I have already included the Elsevier Latex template at the beginning of the [main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex). Feel free to change that.

# Style guide and useful notes

* I have added the nomenclature. Entries are defined in the `acronyms.tex` file and can be referenced in the text using the \ac{} command. [More info here](https://youtu.be/zPrWS5cnDgc)
* Write each sentence in a new line. To go in a new line (equivalent to using enter in Word) just leave an empty row between two sentences.
* ~ are non-breaking spaces.
* to leave a comment, go in a new line then type `% todo ....` (replace the dots with your comment)
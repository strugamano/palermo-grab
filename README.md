# palermo-grab

**A simple command line application to download content from [Teca Digitale](https://librarsi.comune.palermo.it/librarsidigitale/opac/librarsi/index.jsp) (Biblioteca comunale di Palermo Leonardo Sciascia).**

The application is developed and maintained on [Manjaro Linux](https://manjaro.org/) and can be run on Linux systems. Development of a Windows version can be [requested](mailto:strugamano@proton.me?subject=[GitHub]%20palermo-grab%20windows).

## Installation

1. The following packages have to be installed from the package manager: git, python, python-pip, python-pipenv (most of these are pre-installed on many Linux systems)
2. Open a console somewhere in your home folder (e.g. ~/src) and clone the git repository:
    `git clone https://github.com/strugamano/palermo-grab.git`
3. cd to the downloaded folder: `cd palermo-grab`
4. Run the installation script: `sh install.sh`

## Usage

The application can be started from the palermo-grab directory with the URL of the library website:

`./palermo-grab.sh 'URL'`

Pay attention to the apostrophes around the URL!

The appropriate page for downloading contains the '[Immagini](/readme-site-ref.png)' section on the right side of the page, with links to the images of the desired content (e.g. [this](https://librarsi.comune.palermo.it/librarsidigitale/opaclib?struct:1016=ricerca.parole_tutte%3A4%3D6&nentries=1&fname=none&sort_access=Titolo%2FAnno%3Amin+5036%2Cmin+5031&do_cmd=search_show_cmd&searchForm=opac%2Flibrarsi%2Ffree.jsp&item:1016:Any=ranzano&saveparams=true&resultForward=opac%2Flibrarsi%2Fviewer%2Fviewer.jsp&select_db=solr_teca&db=solr_teca&from=1&mode=idx) page).

The images are downloaded into the *download* directory which should be emptied after every session.

### Updating

The update.sh file prompts the user, then updates the git repository and the Python packages: `./update.sh`

## Reporting errors

Any error can be reported through [e-mail](mailto:strugamano@proton.me?subject=[GitHub]%20palermo-grab%20error) with the exact error message or console screenshot. 

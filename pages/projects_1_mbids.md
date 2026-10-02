---

layout: page
permalink: /projects/musclebids/
header: no

title: "Muscle-BIDS"
subheadline: 'Standardized and automated data processing.'

images:
  - image_id: 'flow'
    image_name: 'flowchart_proc.gif'
    image_title: 'Automated whole leg muscle processing flowchart using muscle BIDS.'
    image_alt: 'Automated whole leg muscle processing flowchart using muscle BIDS.' 

tags: projects

---

## Why Muscle-BIDS

For automated data processing of processing with various tool-boxes data management is important. For this, the muscle MRI community is developing the Muscle BIDS data structure. When data is organized in this way all needed parameters and data sets can automatically be found, which enables automated processing and evaluation of large data sets. Furthermore, each toolbox that is Muscle-BIDS compatible can run its analysis on the same data without the need to restructure the data input. The last advantage is that the output is also standardized which makes the comparison of results and methods more convenient. More about Muscle-Bids can be found [here>>](https://muscle-bids.github.io/).

All data generated within the muscle-atlas projects will be stored in the Muscle-BIDS format. The main processing tool we use ([QMRITools](https://qmritools.com)) for our standardized qMRI muscle studies uses dedicated [Muscle-BIDS compliant scripts](https://www.qmritools.com/bids/) that do not need any user interaction. Muscle-BIDS pipelines developed for the Muscle-Atlas project supports the following steps:

{% include page-image im_id="flow" %}

> - Conversion of DICOM to raw Muscle-BIDS NIfTI
> - Processing of Muscle-BIDS data
    - DTI, IVIM, T2-mapping and Dixon
    - Data merging
> - Analysis of processed Muscle-BIDS data
    - ROI analysis
    - Tract based analysis

## Data structure

To prevent ambiguity most MRI acquisitions are stored in predefined folders. Muscle-BIDS-compliant software will look in these folders for their needed raw source data. The following folders have been defined in Muscle-BIDS. QMRITools uses the following subfolders to store data in the Muscle-BIDS dataset. More about data structures can be found [here>>](https://www.qmritools.com/bids/files_folders/). Within a data structure standardized entities and suffixes are used to identify which files contain what, more information about file naming can be found [here>>](https://www.qmritools.com/bids/ents_suffs/).

- `anat`: Structural imaging for anatomical or diagnostic reference (e.g T1 or T2).
- `dwi`: Diffusion-weighted data (e.g. DTI or IVIM).
- `dix`: Dixon data.
- `quant`: Relaxometry data (e.g. T1 or T2 mapping).
- `seg`: Segmentation labels (e.g. manual segmentations).
- `raw`: Unspecified non-BIDS files.

An example of a folder structure is shown below:

<div style="
  background-color:black; 
  font-family:Roboto Mono,SFMono-Regular,Consolas,Menlo,monospace; 
  line-height: 1.17; 
  padding-top: 25px; 
  padding-bottom: 25px;
  padding-left: 15px;
  padding-right: 15px;
  color: white; 
  font-weight: bold; 
  font-size: 12px">

└─example/<br>
&nbsp;&nbsp;├─sub-cont001/<br>
&nbsp;&nbsp;│&nbsp;├─ses-visit1a/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;├─dix/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;├─quant/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;└─raw/<br>
&nbsp;&nbsp;│&nbsp;├─ses-visit1b/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;├─dix/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;├─dwi/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;├─quant/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;└─raw/<br>
&nbsp;&nbsp;│&nbsp;└─ses-visit2/<br>
&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├─dwi/<br>
&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└─raw/<br>
&nbsp;&nbsp;├─sub-pat0054/<br>
&nbsp;&nbsp;│&nbsp;├─ses-visit1/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;├─dwi/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;├─quant/<br>
&nbsp;&nbsp;│&nbsp;│&nbsp;└─raw/<br>
&nbsp;&nbsp;│&nbsp;└─ses-visit2/<br>
&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├─dix/<br>
&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├─dwi/<br>
&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└─raw/<br>
&nbsp;&nbsp;└─sub-test002/<br>
&nbsp;&nbsp;&nbsp;&nbsp;├─ses-visit1/<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;├─quant/<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;└─raw/<br>
&nbsp;&nbsp;&nbsp;&nbsp;└─ses-visit2/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─dwi/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─quant/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─raw/

</div>

### Other projects

{% include list-pages tag="projects" %}

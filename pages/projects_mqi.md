---

layout: page
permalink: /projects/muscle quality index/
header: no

title: "Muscle quality index"
subheadline: 'Linking muscle MRI measurements to muscle function.'
teaser: "Identify critical factors in multi-parametric qMRI and combine them into a Muscle Quality Index linked to muscle force and function"

tags: projects

images:
  - image_id: 'mqi'
    image_name: 'muscle quality index.png'
    image_title: 'General concept for muscle quality using standardized analysis of quantitative MRI data'
    image_alt: 'General concept for evaluating muscle quality using standardized analysis of quantitative MRI data' 
  - image_id: 'acq'
    image_name: 'acquisition method.png'
    image_title: 'Bilateral acquisition of quantitative muscle MRI data of the whole leg'
    image_alt: 'Bilateral acquisition of quantitative muscle MRI data of the whole leg' 
  - image_id: 'data'
    image_name: 'data collection.png'
    image_title: 'Population based acquisition of quantitative muscle MRI data in normal aging population'
    image_alt: 'Population based acquisition of quantitative muscle MRI data in normal aging population' 
  - image_id: 'proc'
    image_name: 'processing concepts.png'
    image_title: 'Whole leg quantitative muscle processing'
    image_alt: 'Intended processing methods for whole leg quantitative muscle MRI data' 
  - image_id: 'finger'
    image_name: 'muscle fingerprint.png'
    image_title: 'Defining a per muscle finger print to understand disease'
    image_alt: 'Finding muscle finger prints of healhty aging muscle to better understand disease' 

---

The burden of neuromuscular diseases on society is significant and often requires individualized treatment and assessment. Magnetic Resonance Imaging (MRI) is widely used to evaluate these muscle disorders, but the methods applied in clinical practice are frequently limited to qualitative anatomical imaging only. This is a drawback since MRI offers a vast range of quantitative imaging contrasts that provide information about muscle structure, status, and microstructure. The development of quantitative MRI (qMRI) and processing methods is becoming increasingly important in the investigation of muscle injury and disease through both cross-sectional and longitudinal studies.

{% include page-image im_id="mqi" %}

Despite its sensitivity, qMRI parameters often lack specificity and are not directly related to muscle function. The Muscle Quality Index project aims to address this challenge by defining a unique fingerprint for every muscle in a large group of healthy individuals, incorporating qMRI parameters, muscle architecture, and functional measurements. Our multi-parametric approach will detect and characterize deviations from normal, hopefully, with greater specificity than using individual parameters alone, and establish a direct connection between imaging parameters and muscle structure and function.


### The Blind Spot

Commonly used quantitative MRI (qMRI) methods, such as Dixon imaging for fat quantification, water T2-mapping (T2m) for inflammation detection, and diffusion-weighted imaging (DWI) and fiber tractography for muscle microstructure and architecture characterization, are now widely available. However, despite the capability of MRI to visualize large areas of the human body in 3D, the use of these muscle qMRI methods is often limited to a few muscles using localized 2D acquisition. 

{% include page-image im_id="acq" %}

The current qMRI methodology, as shown in the figure below, frequently covers only a small area and analyzes quantitative parameters using region-of-interest (ROI) based averages per muscle. This approach can lead to missed focal lesions and incomplete evaluation of muscle status. To address this challenge, we have developed a whole-leg qMRI acquisition protocol with multiple qMRI contrasts that can be completed within 40 minutes. With this approach, focal lesions will no longer be missed, and variations within a muscle can be more effectively studied.

### The Power Problem

Quantitative MRI (qMRI) parameters are effective in detecting changes in muscle, but most neuromuscular diseases progress slowly, leading to only small changes over the course of 1-2 years. Obtaining large sample sizes for rare muscle diseases is often difficult, even in multi-center studies. Longitudinal studies can provide more statistical power, but every patient presents unique characteristics, leading to large variance within patient groups, which in turn requires larger sample sizes.

{% include page-image im_id="data" %}

There is a pressing need to identify which confounding parameters must be considered in order to reduce sample sizes and eventually enable single-subject evaluation. Even within a healthy population, muscle anatomy and quality can vary greatly, with even greater variability among patients. To address this challenge, we have initiated the [Motion Study](https://www.muscle-atlas.org/projects/motion/), which will scan 160 subjects between the ages of 15 and 60, covering their entire legs. Each participant will also undergo a quantitative evaluation of their function and force. This will provide insights into which confounding factors are essential and inform future studies.

### The Missing Link

In order to study muscle architecture and anatomy from the acquired data, it is necessary to enhance available analysis methods. To achieve this, we will use a 3D-UNET convolutional neural network to annotate the individual muscles and bones in all data. There is significant anatomical variation between human muscles, so we will also employ statistical shape modeling to morph all subjects' muscles to a common atlas space and quantize muscle shape. The combination of muscle segmentations and fiber tractography results from the DWI acquisitions will allow for a subject-specific quantification of muscle architecture.

{% include page-image im_id="proc" %}

### The Muscle Quality Index

By establishing a unique muscle and subject-specific fingerprint that links muscle to function, qMRI measurements will enable a personalized evaluation of muscle abnormalities and changes. This Muscle Quality Index aspires to become usefull for objective and direct assessments of treatment responses in individual subjects. This project will hopefully further research into muscle function and dysfunction and facilitate the translation of these methods into clinical practice. And eventually change the way we analyze and interpret qMRI data to better serve the clinical needs of individual patients across a broad spectrum of muscle diseases.

{% include page-image im_id="finger" %}

<br>
{% include list-pages tag="projects" %}
---

layout: page
permalink: /results/motion418
header: no

title: "Motion_418"
subheadline: 'An overview of the data'

images:
  - image_id: 'outph'
    image_name: 'progress/MOTION418_megre_dix_outph.jpg'
    image_title: 'The out-phase image of the dixon reconstruction for water fat quantification.'
    image_alt: 'The out-phase image of the dixon reconstruction for water fat quantification.'
  - image_id: 'fatfr'
    image_name: 'progress/MOTION418_megre_dix_fatfr.jpg'
    image_title: 'The fat fraction of the lower extremity obtained from the dixon reconstruction for muscle water fat quantification.'
    image_alt: 'The fat fraction of the lower extremity obtained from the dixon reconstruction for muscle water fat quantification.'
  - image_id: 'r2star'
    image_name: 'progress/MOTION418_megre_dix_r2star.jpg'
    image_title: 'The R2 star relaxation time of the lower extremity obtained from the dixon reconstruction for muscle water fat quantification.'
    image_alt: 'The R2 star relaxation time of the lower extremity obtained from the dixon reconstruction for muscle water fat quantification.'
  - image_id: 'snr'
    image_name: 'progress/MOTION418_megre_dix_snr.jpg'
    image_title: 'The SNR distribution of the dixon data.'
    image_alt: 'The SNR distribution of the dixon data.'
  - image_id: 'dbond'
    image_name: 'progress/MOTION418_megre_dix_dbond.jpg'
    image_title: 'Number of double bonds in subcutanious fat.'
    image_alt: 'Number of double bonds in subcutanious fat.'

  - image_id: 't2wat'
    image_name: 'progress/MOTION418_mese_t2_wat.jpg'
    image_title: 'The water part of the acquired multi-echo spin echo data.'
    image_alt: 'The water part of the acquired multi-echo spin echo data.'
  - image_id: 't2w'
    image_name: 'progress/MOTION418_mese_t2_t2w.jpg'
    image_title: 'The water only T2 relaxation time of the lower extremity obtained from multi echo spin echo t2 mapping with EPG based reconstruction.'
    image_alt: 'The water only T2 relaxation time of the lower extremity obtained from multi echo spin echo t2 mapping with EPG based reconstruction.'

  - image_id: 'md'
    image_name: 'progress/MOTION418_dwi_dti_md.jpg'
    image_title: 'IVIM corrected whole leg muscle mean diffusivity obtained from diffusion tensor imaging.'
    image_alt: 'IVIM corrected whole leg muscle mean diffusivity obtained from diffusion tensor imaging.'
  - image_id: 'fa'
    image_name: 'progress/MOTION418_dwi_dti_fa.jpg'
    image_title: 'IVIM corrected whole leg muscle fractional anisotropy obtained from diffusion tensor imaging.'
    image_alt: 'IVIM corrected whole leg muscle fractional anisotropy obtained from diffusion tensor imaging.'
  - image_id: 'snr0'
    image_name: 'progress/MOTION418_dwi_dti_snr0.jpg'
    image_title: 'SNR distribution of the unweighted diffusion data.'
    image_alt: 'SNR distribution of the unweighted diffusion data.'

  - image_id: 'seg2D'
    image_name: 'progress/MOTION418_seg_auto_megre.jpg'
    image_title: 'Overlay of automated muscle segmentation labels on dixon water image.'
    image_alt: 'Overlay of automated muscle segmentation labels on dixon water image.'
  - image_id: 'seg3D'
    image_name: 'progress/MOTION418_seg_auto_megre_vol.jpg'
    image_title: '3D render of automated muscle segmentation labels generated using a CNN UNET.'
    image_alt: '3D render of automated muscle segmentation labels generated using a CNN UNET.'

  - image_id: 'leng'
    image_name: 'progress/MOTION418_dwi_dti_trk_leng.jpg'
    image_title: 'Muscle fiber tract length map based on whole leg DTI based fiber tractography.'
    image_alt: 'Muscle fiber tract length map based on whole leg DTI based fiber tractography.'
  - image_id: 'ang'
    image_name: 'progress/MOTION418_dwi_dti_trk_ang.jpg'
    image_title: 'Muscle fiber tract angle map based on whole leg DTI based fiber tractography.'
    image_alt: 'Muscle fiber tract angle map based on whole leg DTI based fiber tractography.'
  - image_id: 'dens'
    image_name: 'progress/MOTION418_dwi_dti_trk_dens.jpg'
    image_title: 'Muscle fiber tract density map based on whole leg DTI based fiber tractography.'
    image_alt: 'Muscle fiber tract density map based on whole leg DTI based fiber tractography.'
  - image_id: 'tract'
    image_name: 'progress/MOTION418_dwi_dti_trk_tracts.jpg'
    image_title: 'Whole leg 3D fiber tractography of all muscles segmented using a CNN UNET.'
    image_alt: 'Whole leg 3D fiber tractography of all muscles segmented using a CNN UNET.'

tags: subjects
icon: 'progress/MOTION418_seg_auto_megre_vol.jpg'

---

[Back››](/projects/progress/)

### Water-fat quantification

Dixon based water fat quantification, for information [look here>>](/methods/waterfat/).

- Out phase image
{% include page-image im_id="outph" %}

- Fat fraction
{% include page-image im_id="fatfr" %}

- R2 star relaxation
{% include page-image im_id="r2star" %}

- SNR distribution
{% include page-image im_id="snr" %}

- Number of double bonds in subcutanious fat
{% include page-image im_id="dbond" %}

### Water only T2 mapping

Multi echo spin echo T2 relaxation time mapping with EPG reconstruction, for information [look here>>](/methods/t2mapping/).

- Water only signal
{% include page-image im_id="t2wat" %}

- Water only T2 relaxation time
{% include page-image im_id="t2w" %}

### Diffusion tensor imaging

Diffusion weighted imaging with IVIM and DTI fitting to obtain muscle microstructure and muscle architecture, for information [look here>>](/methods/diffusion/).

- Mean diffusivity
{% include page-image im_id="md" %}

- Fractional anisotropy
{% include page-image im_id="fa" %}

- SNR of the unweighted image
{% include page-image im_id="snr0" %}

### Muscle segmentation

Convolution neural network based (UNET) fiber automated muscle segmentation, for information [look here>>](/methods/segmentation/).

- Automated muscle and bone segmentation.
{% include page-image im_id="seg2D" %}

- 3D volume render of automated muscle segmentation.
{% include page-image im_id="seg3D" %}

### Muscle fiber tractography

Whole leg muscle fiber tractography using DTI, for information [look here>>](/methods/tractography/).

- Muscle fiber length map
{% include page-image im_id="leng" %}

- Muscle fiber angle map
{% include page-image im_id="ang" %}

- Muscle fiber density map
{% include page-image im_id="dens" %}

- 3D volume renders of muscle fiber tractography
{% include page-image im_id="tract" %}

### List of scanned participants

{% include list-progress.txt tag="subjects" %}

### Other projects

{% include list-pages tag="projects" %}
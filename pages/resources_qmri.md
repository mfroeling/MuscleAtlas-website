---

layout: page
permalink: /resources/qmritools/
header: no

title: "QMRITools"
subheadline: 'Processing of muscle quantitative MRI data.'
teaser: "If you used it, please cite us"

tags: resources

images:
  - image_id: 'over'
    image_name: 'overview.png'
    image_title: 'Overview of QMRITools functionality'
    image_alt: 'Overview of QMRITools functionality' 
  - image_id: 'proc'
    image_name: 'processing.png'
    image_title: 'Quantitative muscle MRI processing and analysis'
    image_alt: 'Quantitative muscle MRI processing and analysis'
  - image_id: 'app'
    image_name: 'applications of QMRITools.png'
    image_title: 'applications of QMRITools'
    image_alt: 'applications of QMRITools'

---

<p align="center">
<a href="https://www.wolfram.com/language/" target="_blank" style="text-decoration: none; border-bottom: none;">
<img alt="wolfram language" title="wolfram language" src="/assets/images/wolfram_language.png"></a>
<a href="http://www.wolfram.com/mathematica/" target="_blank" style="text-decoration: none; border-bottom: none;">
<img alt="Wolfram Mathematica" title="Wolfram Mathematica" src="/assets/images/wolfram_mathematica.png"></a>
<a href="https://marketplace.visualstudio.com/items?itemName=WolframResearch.wolfram" target="_blank" style="text-decoration: none; border-bottom: none;">
<img alt="visual studio code" title="visual studio code" src="/assets/images/visual-studio-code.png"></a>
<a href="https://www.eclipse.org/" target="_blank" style="text-decoration: none; border-bottom: none;">
<img alt="eclipse" title="eclipse" src="/assets/images/eclipse.png"></a>
<a href="https://www.wolfram.com/workbench/" target="_blank" style="text-decoration: none; border-bottom: none;">
<img alt="wolfram workbench" title="wolfram workbench" src="/assets/images/wolfram_workbench.png"></a>
<a href="https://community.wolfram.com/groups/-/m/t/1661539" target="_blank" style="text-decoration: none; border-bottom: none;">
<img alt="Wolfram Community" title="Wolfram Community" src="/assets/images/community.png"></a>
</p>

`QMRITools` is a collection of tools and functions for processing
quantitative MRI data. The toolbox is developed for the [Wolfram
language](https://www.wolfram.com/language/) and runs in the latest version of
[Wolfram Mathematica](http://www.wolfram.com/mathematica/). The toolbox does not provide a GUI and its primary goal is to allow for fast batch data processing, and
facilitate development and prototyping of new functions. The core of the
toolbox contains various functions for data manipulation and restructuring.

{% include page-image im_id="app" %}

The toolbox was developed mostly in the context of quantitative muscle
([Froeling et al. 2012](https://onlinelibrary.wiley.com/doi/10.1002/jmri.23608){:target="_blank"}), nerve and cardiac magnetic resonance imaging. The library of functions grows along with the research it is used for and started as a toolbox to analyze DWI data of muscle. Since then it has grown to include many other features such as cardiac analysis
(tagging and T1 mapping), dixon reconstruction, EPG modeling and fitting, j-coupling
simulations and more. It currently contains over 450 custom functions (over 30.000 lines of code) complete with more than 750 documentation pages and demonstrations for each toolbox.

{% include page-image im_id="proc" %}

### Awards and media

During the 2023 ISMRM in Toronto QMRITools was awarded received the "Best Open Source Tool Award" from the Quantitative MRI study group.

{% include page-image im_id="award" %}

If you want to learn more about the workings of QMRITools you can watch a live discussion with the
Wolfram academic outreach team about <a href="https://www.youtube.com/live/wupxxiPJkxU?si=22BV_HSSa5u7Ds3D" target="_blank">QMRITools</a>
and the role of computational Wolfram technology. A more in depth explanation of <a href="https://www.youtube.com/live/LVUBupORthA?si=UjoNpM2szsrgB7xx" target="_blank">the paclet functionality</a> was presented to the Wolfram R&D Team.

### Referencing

When using the toolbox please cite one of the following references:

1. Froeling M: *QMRTools: a Mathematica toolbox for quantitative MRI analysis*. J Open Source Softw 2019; 4:1204.
   [link](https://joss.theoj.org/papers/ef8bfb6c31499845d353b6a5af0d6300){:target="_blank"}
2. Froeling M, et al.: *Reproducibility of diffusion tensor imaging in human forearm muscles at 3.0 T in a clinical setting*. Magn Reson Med 2010; 64:1182-1190.
   [link](https://onlinelibrary.wiley.com/doi/full/10.1002/mrm.22477){:target="_blank"}
3. Froeling M, et al.: *Diffusion-tensor MRI reveals the complex muscle architecture of the human forearm*. J Magn Reson Imaging 2012; 36:237-248.
   [link](https://onlinelibrary.wiley.com/doi/10.1002/jmri.23608){:target="_blank"}
4. Schlaffke L, et al.: *Multi‐center evaluation of stability and reproducibility of quantitative MRI measures in healthy calf muscles*. NMR Biomed. 2019;32:e4119
   [link](https://onlinelibrary.wiley.com/doi/full/10.1002/nbm.4119){:target="_blank"}

{% include page-image im_id="app" %}

{% include list-pages tag="projects" %}

---
pageClass: projects-page
---

# Work

Here are some works of mine :books:

## Projects

<ProjectCard image="/projects/WisdomStore.png">  
  
  **一站式人工智能视觉分析软件**（2023）
  
  - WisdomStore是一个支持本地离线部署使用的零代码一站式图像智能分析平台，可在本地环境下进行图像数据标注、智能模型训练、智能模型推理等识别结果统计表征。
  - 目前图像标注功能已包括：框形标注、涂鸦标注、多边形标注（包括弧度）、智能标注（魔术棒点击、画框式标注）。
  - 目前模型训练和推理功能已包括：目标检测、图像分割、实例分割。
  
  [[WisdomStore](http://wisdomstore.tech/zhihe/index.html)] [[Download](http://wisdomstore.tech/zhihe/download.html)] [[Doc](http://wisdomstore.tech/zhihe/help.html)]

</ProjectCard>

<ProjectCard image="/projects/MicroStitch.png">  
  
  **显微图像拼接软件**（2022）
  
  - MicroStitch软件可实现微观图像数据的高速、自动和精准拼接。
  - 通过集成最先进的图像特征提取和匹配技术，融合GPU加速和多进程加速方法，能够对任意数量输入、任意拍摄顺序的序列图像自动化快速地计算图像间的位移关系，并利用图像融合方法生成高质量高分辨的全景图像。
  
  [[MicroStitch](http://microstitch.tech/)] [[Download](http://microstitch.tech/)] [[Doc](https://microstitch.tech/micro/help.html)]

</ProjectCard>

## Publications

<ProjectCard>

  **FedST: Federated Style Transfer Learning for Non-IID Image Segmentation**

  Federated learning collaboratively trains machine learning models among different clients while keeping data privacy and has become the mainstream for breaking data silos. However, the non-independently and identically distribution (i.e., Non-IID) characteristic of different image domains among different clients reduces the benefits of federated learning and has become a bottleneck problem restricting the accuracy and generalization of federated models. In this work, we propose a novel federated image segmentation method based on style transfer, FedST, by using a denoising diffusion probabilistic model to achieve feature disentanglement and image synthesis of cross-domain image data between multiple clients. Thus it can share style features among clients while protecting structure features of image data, which effectively alleviates the influence of the Non-IID phenomenon. Experiments prove that our method achieves superior segmentation performance compared to state-of-art methods among four different Non-IID datasets in objective and subjective assessment.

  Ma B, Yin X, Tan J, ***Chen Y*** et al. FedST: Federated Style Transfer Learning for Non-IID Image Segmentation[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2024, 38(5): 4053-4061.

  [[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/28199)] [[Code](https://github.com/YoferChen/FedST)]

</ProjectCard>


<ProjectCard>

  **Cam-PC: A Novel Method for Camouflaging Point Clouds to Counter Adversarial Deception in Remote Sensing**
  
  Synthetic aperture LiDAR can generate point cloud data, which is widely used in 3-D scene reconstruction. However, existing point cloud object recognition methods are vulnerable to adversarial attacks, and such attacks are difficult to transfer to the physical world. Even if adversarial perturbations are added to physical objects, they are easily detectable by other sensors. Our proposed method includes two modules, R-D and D-R, which generate more concealed adversarial point cloud samples by modifying digital and physical features. The R-D module maps real-world entities to point cloud data in the digital world and generates adversarial samples by modifying signal amplitude values. The D-R module constructs adversarial objects by modifying the surface diffuse reflectance of the target object based on ray tracing and correspondences between digital and physical features. Our method is evaluated through experiments on attack effectiveness, robustness after subsampling and transferability, demonstrating its effectiveness, and achieving new state-of-the-art performance.

  Wei B, Huang T, Zhang X, Liang J, Li Y, Cao C, Li D, ***Chen Y***, et al. Cam-PC: A Novel Method for Camouflaging Point Clouds to Counter Adversarial Deception in Remote Sensing[J]. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2023.

  [[Paper](https://ieeexplore.ieee.org/document/10285331)] 

</ProjectCard>


<ProjectCard>

  **Adversarial attacks on deep-learning-based radar range profile target recognition**
  
  Target recognition based on a high-resolution range profile (HRRP) has always been a research hotspot in the radar signal interpretation field. Deep learning has been an important method for HRRP target recognition. However, recent research has shown that optical image target recognition methods based on deep learning are vulnerable to adversarial samples. Whether HRRP target recognition methods based on deep learning can be attacked remains an open question. In this paper, four methods of generating adversarial perturbations are proposed. Algorithm 1 generates the nontargeted fine-grained perturbation based on the binary search method. Algorithm 2 generates the targeted fine-grained perturbation based on the multiple-iteration method. Algorithm 3 generates the nontargeted universal adversarial perturbation (UAP) based on aggregating some fine-grained perturbations. Algorithm 4 generates the targeted universal perturbation based on scaling one fine-grained perturbation. These perturbations are used to generate adversarial samples to attack HRRP target recognition methods based on deep learning under white-box and black-box attacks. The experiments are conducted with actual radar data and show that the HRRP adversarial samples have certain aggressiveness. Therefore, HRRP target recognition methods based on deep learning have potential security risks.

  Huang T, ***Chen Y***, Yao B, et al. Adversarial attacks on deep-learning-based radar range profile target recognition[J]. Information Sciences, 2020, 531: 159-176.
  
  [[Paper](https://www.sciencedirect.com/science/article/abs/pii/S0020025520302450)] 

</ProjectCard>

<style lang="stylus">

.projects-page
  background-color #fafbfc

</style>
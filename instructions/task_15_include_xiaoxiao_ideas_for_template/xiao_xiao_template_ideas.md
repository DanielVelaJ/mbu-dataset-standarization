# Xiaoxiao initial ideas for templates
## Domain-agnostic

1. Classification
    
    **easy:** `Q: Is {} present?  A: {yes/no}`
    
    **hard:** `Q: what is the primary diagnosis? A: {label}`
    
    **hard:** `Q: what is the severity grade? A: {grade}` 
    
    `What kind of examination is this image?`
    
    `Is there any abnormality?`
    

  

1. Detection 
    
     **easy:** `Q: Is a {target} present in the {region/side}?  A: {yes/no}`
    
     **hard:** `Q: where is the {target}? A: {A: left-top, B: right-top, C: left-bottom, D: right-bottom} or {bbox}`  
    
    **hard:** `Q: what {entity} is shown in the red box? A:{lable}`
    
    Other format of question
    
    ! location/position, scale/proportion
    
2. Segmentation
    
    same to b Detection
    
    **hard:**  `Q: what proportion of the image is {target}? A: {%}` A less than 25% B 50% C 75% D ,,,
    
    showing class and mask on the image, ask  (pair for comparison) : MLLM  ~~CLIP~~ 
    converting  to binary yes/no
    
3. Keypoints
4. VQA
5. Counting
    
    

level 1, level 2, level-3, mixed-all,

## Pathology 
1. Classification
    1. cell/tissue
        
        `What {tissue type} is shown? {lable}
        Is {e.g., **tumor**} present? {Yes/No}`
        
        `Which {cell type} dominates? {label}`
        
        `Is there necrosis/stroma/inflammation? {Yes/No}` 
        
    2. grading/scoring
        
        `What is the {grade/score}? {lable}`
        
2. Detection/Segmentation
    1. ratio
        
        `What percentage of tissue is tumor? {%}` A 0~25% B C D 
        
    2.  cell/tissue 
        
        `What tissue type is shown in the red box? {lable}
         It {e.g., **tumor**} present in the red box? {Yes/No}`
        
        `Which cell type dominates? {label}`
        
        `Is there necrosis/stroma/inflammation in the red box? ? {Yes/No}`

## Radiology 
1. Classification
    1. modality/view
        
        `What is the modality? {Chest X-ray|CT|MRI|US|…}
         What is the view? {AP|PA|Lateral|Axial|Coronal|Sagittal}`
        
    2. findings
        
        `Is {finding} present? {Yes/No}`
        
        `Which primary finding is present? {Label}`
        
        `What is the severity grade of {finding}? {0–4}`
        
2. detection/segmentation
    1. anomaly detection，x-ray
        
        `Which side/zone/lobe shows {finding}?  {left|right|zone}`
        
        or `is the {finding} show in the bbox? {Yes/No}`
        
         `Where is the {device/nodule}?  {bbox}`  
        
        or `is the {device/nodule} in the bbox? {Yes/No}`
        
        `Is there {*pleural effusion*, *cardiomediastinal silhouette, …*}? {Yes/No}` 
        
    2. counting (segmentation)
        
        `How many nodules are present? {number}`

## Surgery
1. phase/step
    
    `Which surgical phase is shown? {label}`  
    
    or `Is this the {phase} phase? {yes/no}`
    
    `Has the {step/action} been completed? {yes/no}`
    
2. action / triplet (verb–instrument–target)
    
    `What action is being performed?  → {verb}
    Which instrument is interacting with anatomy?  → {instrument}
    What is the verb‑instrument‑target? → {verb}/{instrument}/{target}`
    
3. instrument
    
    `Which instrument is dominant? {lable}`
    
    or `Is a {instrument} visible/used? {yes/No}`
    
4. anatomy
    
    `Which anatomical structure is in focus? {stucture}`
    
    or `Is {structure} identified? {yes/No}`
    
5. safety/checklist
    
    ? ask Kun
    

---

# Opthalmology
fundus, optical coherence tomography, slit-lamp , slo, fpp , oct , ffa ,ous

# Dermathology
1. diagnosis/type (classification)
    
    `What is the lesion type? {label}`
    
    or `Is the lesion {malignant}? {yes/no}`
    
2. ABCDE?
3. detection/segmentation
4. location
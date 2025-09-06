//Unified Biomedical VQA Datum Schema (v1.0)
# Data Standardization Pipeline

**Input:** <dataset information, image_lists, labels_lists>

**Output:** <canonical Datum JSONL>
```python
{
  "header": {
    "image_id": "P_0000001.jpg",          // required
    "image_name": "P_0000001.jpg",        // required
    "domain": "Dermatology",              // required
    "subdomain": null                     // optional
    "category": "melanoma"                //<label_name|null> classfication
  },
  
//---------------------------------------------
  "dataset": {
    "name": "<dataset>",
    "dataset_id": "<string>",
    "tasks": ["<Classification|Segmentation|Detection|Landmarks|Describe|Ask&Answer|Counting|Grounding|Retrieval>"] ,
    "split": "<train|val|test|other>",
    "institution": "<string|null>",
    "license": "<SPDX id|URL|string|null>",
    "path": "<dataset_name/imagexxx.png>"
  },
  
  "quality": {
    "expert_involved": "<yes|no|unknown>",
    "qc_passed": "<yes|no|unknown>", //quality control
    "notes": "<string|null>"
  },
 
//---------------------------------------------
  "imaging": {
    "modality": "<CXR|CT|MRI|US|Fundus|OCT|WSI|Photo|Endoscopy|Echo|Other>",
    "submodality": "<Axial|Coronal|Sagittal|B-mode|Doppler|T1|T2|...|null>",
    "frames": <int|1>,  // for radiology data
    "view": "<AP|PA|Lateral|Axial|Coronal|Sagittal|PLAX|A4C|...|null>", // Radiology data have this feature
    "body_part": "<head|neck|chest|abdomen|pelvis|upper_limb|lower_limb|skin|oral|dental|cardiac|fetal|other|null>",  
    "eye_part": "<macula|disc|anterior|posterior|...|null>" // Ophthalmology domain
  },

  "geometry": {
    "bbox": [[x1, y1, x2, y2], ...],               // optional, relative [0,1]
    "polygons": [[[x, y], ...], ...],              // optional, relative [0,1]
    "image_size": [<W>, <H>]                       // required if pixel coords
  },

//---------------------------------------------
  "questions-and-answers": [
    {
      "qa_id": "<string>", //1，2，3，...
      "task": "<Classification|Segmentation|Detection|Landmarks|Describe|Ask&Answer|Counting|Grounding|Retrieval>",
      "question": "<string>",
      "answer": "<string|number|bbox|list>",
      "answer_type": "<yes_no|single_label|multi_label|ordinal|number|span|bbox|options>",
      "options": ["<optional list for MCQ>"], //ToDo
      "difficulty": "<easy|medium|hard>", //ToDo
      "uncertainty": "<certain|uncertain|unknown>",
      "answer_confidence": <number 0-1|null>, 
      "rationale": "<optional short reasoning or rule used to construct this Q/A>",
      "provenance": {
        "original_label": "<label_name or id|null>",
        "rule_id": "<template-id or script|null>",
        "annotation_id": "<geometry>,<bbox>,<ind>" , //"Uncertain, documenting the relevant source for reference"
        "created_by": "<human|program>"
      }
    }
  ],
//---------------------------------------------
  "domain-specific": {
     // To Do
  },

  "version": "v1.0"
} 
```
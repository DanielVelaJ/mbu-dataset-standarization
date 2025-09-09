# Surgery Surgical Landmark Quality Assessment Template

## Template Overview

**Template ID**: `surgery_landmarks_multiple_easy_1`  
**Task Type**: Multiclass classification  
**Difficulty**: Easy  
**Question Pattern**: Surgical landmark visibility evaluation  
**Medical Domain**: Surgery (anatomical landmark detection)  
**Domain-knowledge summary**: Requires specialized surgical anatomy knowledge for intraoperative landmark identification. Must understand critical anatomical reference points, surgical navigation landmarks, vascular and neural anatomy, tissue plane relationships, and ability to assess landmark visibility and quality for surgical guidance and safety during operative procedures.

## Template Description

This template converts landmark detection datasets into MCVQA format by asking questions about the quality and visibility of anatomical landmarks in surgical images. While original landmark tasks produce coordinate locations, this template evaluates the model's ability to assess landmark visibility and identification quality through multiple choice questions.

The template is designed for surgery datasets with landmark annotations, testing the model's understanding of anatomical landmark recognition and surgical navigation requirements.

## Question Generation Pattern

### Question Format
```
"What best describes the visibility of key anatomical landmarks in this surgical field?"
```

### Answer Format
Multiclass choice with landmark visibility options:
- A. All landmarks clearly visible and identifiable
- B. Most landmarks visible with good identification
- C. Some landmarks obscured, partial identification
- D. Few landmarks visible, poor identification
- E. Landmarks not identifiable, inadequate exposure

### Template Variables
- `{landmark_count}`: Number of critical landmarks in the field
- `{visibility_quality}`: Clarity and definition of landmark structures
- `{anatomical_exposure}`: Adequacy of surgical exposure for landmark identification
- `{navigation_utility}`: Usefulness for surgical navigation and orientation

### Clinical Context
- **Surgical Navigation**: Landmarks provide spatial orientation and reference points
- **Safety Navigation**: Critical for avoiding vital structures and ensuring procedural safety
- **Procedural Planning**: Landmarks guide surgical approach and technique selection
- **Training Value**: Landmark identification essential for surgical education

## Mapping to Datum Schema

```json
{
  "qa_id": "1",
  "task": "Classification",
  "question": "What best describes the visibility of key anatomical landmarks in this surgical field?",
  "answer": "A",
  "answer_type": "single_label",
  "options": [
    "All landmarks clearly visible and identifiable",
    "Most landmarks visible with good identification",
    "Some landmarks obscured, partial identification", 
    "Few landmarks visible, poor identification",
    "Landmarks not identifiable, inadequate exposure"
  ],
  "difficulty": "easy",
  "uncertainty": "certain",
  "answer_confidence": 0.9,
  "rationale": "Surgical field shows excellent exposure with all critical anatomical landmarks clearly visible and easily identifiable",
  "provenance": {
    "original_label": "excellent_visibility",
    "rule_id": "surgery_landmarks_multiple_easy_1",
    "annotation_id": "landmark_visibility",
    "created_by": "program"
  }
}
```

## Dataset Requirements

### Primary Requirements
- **Images**: Surgical images with anatomical landmark annotations
- **Labels**: Landmark visibility or quality assessment data
- **Quality**: Clear visualization of anatomical structures and reference points

### Compatible Datasets

**Available in MBU Metadata:**
- `nanxiao176/SurgicalVideoEndoNeRFTracking` - Surgical video with 2D/3D landmark tracking (tracked_2d_pts.pkl, tracked_3d_pts.pkl)

**General Categories:**
- Surgical navigation landmark datasets
- Anatomical reference point collections
- Surgical training landmark databases
- Intraoperative guidance datasets
- Augmented reality surgical reference sets

### Minimum Standards
- **Image Quality**: Sufficient resolution for landmark identification
- **Annotation Quality**: Expert validation by surgeons familiar with surgical anatomy
- **Data Distribution**: Range of visibility conditions from excellent to poor

## Template Usage Rules

### Question Construction Rules
1. Focus on landmark visibility and identification quality
2. Reference surgical navigation and orientation needs
3. Consider educational and training applications
4. Emphasize practical surgical utility

### Answer Assignment Rules
1. Map excellent landmark visibility → "All landmarks clearly visible and identifiable"
2. Map good landmark visibility → "Most landmarks visible with good identification"
3. Map moderate visibility → "Some landmarks obscured, partial identification"
4. Map poor visibility → "Few landmarks visible, poor identification"
5. Map inadequate exposure → "Landmarks not identifiable, inadequate exposure"

### Quality Control Guidelines
1. Ensure assessment reflects actual landmark identification utility
2. Verify relevance to surgical navigation and safety
3. Cross-validate with expert anatomical assessment
4. Review for educational and training value

## Examples

### Example 1: Optimal Anatomical Exposure
**Image**: Surgical field with perfectly exposed anatomical landmarks  
**Question**: "What best describes the visibility of key anatomical landmarks in this surgical field?"  
**Answer**: A. All landmarks clearly visible and identifiable  
**Rationale**: Surgical exposure provides excellent visualization of all critical anatomical landmarks with clear identification capability

### Example 2: Good Surgical View
**Image**: Well-exposed surgical field with most landmarks visible  
**Question**: "What best describes the visibility of key anatomical landmarks in this surgical field?"  
**Answer**: B. Most landmarks visible with good identification  
**Rationale**: Surgical field shows good exposure with majority of landmarks clearly visible for navigation purposes

### Example 3: Partially Obscured Field
**Image**: Surgical view with some landmarks hidden by tissue or instruments  
**Question**: "What best describes the visibility of key anatomical landmarks in this surgical field?"  
**Answer**: C. Some landmarks obscured, partial identification  
**Rationale**: Several landmarks are obscured by overlying tissue or instruments, limiting complete anatomical assessment

### Example 4: Poor Exposure
**Image**: Surgical field with limited anatomical landmark visibility  
**Question**: "What best describes the visibility of key anatomical landmarks in this surgical field?"  
**Answer**: D. Few landmarks visible, poor identification  
**Rationale**: Inadequate surgical exposure results in poor landmark visibility affecting navigation and orientation

### Example 5: Inadequate Visualization
**Image**: Surgical field with no clear anatomical reference points  
**Question**: "What best describes the visibility of key anatomical landmarks in this surgical field?"  
**Answer**: E. Landmarks not identifiable, inadequate exposure  
**Rationale**: Surgical field lacks adequate exposure for landmark identification, requiring improved visualization

## Implementation Notes

### Technical Considerations
- Correlate assessment with actual landmark detection algorithm performance
- Consider varying surgical approaches and anatomical regions
- Account for different imaging modalities and surgical equipment
- Handle occlusion by instruments, tissue, or bleeding

### Clinical Validation
- Align with surgical navigation and anatomy requirements
- Cross-reference with surgical training curricula
- Validate against expert surgeon landmark assessment
- Consider augmented reality and navigation system needs

### Dataset-Specific Adaptations
- **Procedure-specific datasets**: Focus on relevant landmarks for each procedure
- **Navigation datasets**: Emphasize landmarks critical for surgical guidance
- **Training datasets**: Include educational examples of landmark identification
- **Safety datasets**: Prioritize landmarks essential for complication avoidance

### Quality Assurance
- Regular validation against landmark detection system performance
- Expert review by surgeons experienced in anatomical navigation
- Monitoring for consistency across different surgical procedures
- Updates based on advancing surgical navigation technology and techniques

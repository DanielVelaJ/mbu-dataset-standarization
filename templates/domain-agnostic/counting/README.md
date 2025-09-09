# Domain-Agnostic Counting Templates

## 🏷️ Taxonomy Mapping
**Official Taxonomy Sub-Category**: `Counting`  
**Parent Category**: Vision  
**Repository Path**: `templates/domain-agnostic/counting/`

## 📁 Template Inventory

### **Current Status: ❌ MISSING (Low Priority)**

| Subdirectory | Leaf Node | Planned Templates | Dataset Availability | Status |
|--------------|-----------|-------------------|---------------------|---------|
| `direct/` | Direct count labels — an integer count per image | Future consideration | 🔍 **0 datasets found** | ❌ **Not Planned** |
| `density/` | Density or point map counting — point annotations or density map | Future consideration | 🔍 **0 datasets found** | ❌ **Not Planned** |

### **Why Low Priority**:
- **No compatible datasets found** in our metadata analysis
- **Limited clinical applications** compared to other missing categories
- **Technical complexity** requires specialized counting methodologies

### **Future Template Functionality** (If datasets become available):
- **Direct Count**: Integer count questions ("How many {objects} are in this image?")
- **Density Count**: Spatial density analysis with point annotations
- **Question Pattern**: "Count the number of {target_objects}" or "Mark and count {objects}"
- **Answer Format**: Integer count or spatial point coordinates with count
- **Clinical Use**: Cell counting, lesion enumeration, structure quantification

## 📋 Sub-Categories

### 1. **Direct Count Labels** (`direct/`)
- **Definition**: Output an integer count of targets in the image
- **Output**: Integer count
- **Examples**: Mitosis count per slide, cell count per field
- **Recognition**: "Count of cells/lesions per image"

### 2. **Density or Point Map Counting** (`density/`)
- **Definition**: Predict density map or annotated points for counting
- **Output**: Density map or point coordinates
- **Examples**: Cell counting with dot annotations, spatial density analysis
- **Recognition**: "Point annotations" or "density maps" for counting

## Clinical Applications (Future)

**Potential Uses**:
- **Pathology**: Cell counting in histological samples
- **Radiology**: Lesion enumeration in screening
- **Research**: Quantitative analysis of medical structures
- **Quality Control**: Automated counting for standardization

**Medical Specialties**:
- Pathology (cell counting, mitosis detection)
- Radiology (lesion counting, structure enumeration)
- Research (quantitative medical analysis)

## Implementation Notes

**Current Status**: No templates planned due to lack of compatible datasets in our collection.

**Future Considerations**:
- Templates will be created when relevant counting datasets become available
- Focus on clinically meaningful counting applications
- Integration with existing vision templates for comprehensive coverage

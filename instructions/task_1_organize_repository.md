# Task 1: Organize repository
Please read all of the context files and all of the instructions files and help me define a structure for our repository code. I was thinking that since we will be doing a lot of dataset conversion we could have some sort of separation of concerns to have 
loaders (one for each dataset) and perhaps a way to get the output questions applying a specific template or something like that. I don't know what would be the best architecture to organize this so that it follows best modern practices and is yet simple and neat. 

- Please propose an architecture and explain it. Do not start implementing it until we have discussed it and agreed on the best approach.

## Progress and Decisions Made

### Architecture Decisions (Completed)

**✅ Repository Structure Defined**
- Created `docs/architecture.md` with complete architecture documentation
- Chose simple, modular approach over complex abstractions
- Defined clear separation of concerns with 5 core components

**✅ Key Design Decisions:**
1. **No Registries**: Using simple dictionaries instead of registry pattern - registries add unnecessary complexity for our current scale (27 components initially)
2. **Absolute Imports**: Using absolute imports throughout for better debugging and clarity
3. **Manual Dataset Downloads**: Keeping download as separate preprocessing step, not in loaders
4. **Simple File Structure**: Starting with 5 core files, will split later if needed

**✅ Core Components Defined:**
- `loaders.py`: Dataset-specific parsing (BaseLoader, ChestXray14Loader, etc.)
- `templates.py`: Question generation (BaseTemplate, BinaryTemplate1, etc.) 
- `convert.py`: Main orchestrator with LOADERS/TEMPLATES dicts
- `datum.py`: Data structures (RawDataPoint, QuestionAnswer, Datum)
- `utils.py`: Helper functions

**✅ Data Flow Pipeline:**
```
Raw Dataset → Loader → RawDataPoint → Template → QuestionAnswer + Datum Sections → Validator → JSONL Output
```

**✅ Clarifications Made:**
- **Datum**: The complete JSON output object matching the unified schema
- **QuestionAnswer**: Individual Q&A pairs within the datum's questions_and_answers array
- **Dataset Downloading**: Separate preprocessing step, not embedded in loaders
- **Template Compatibility**: Templates can validate compatibility with datasets

**✅ Enhanced Label Standardization (Latest):**
- **StandardizedAnnotations**: Unified interface that all loaders produce for templates
- **Task Type Field**: `task_type` field ("classification-binary", "classification-multiclass", "classification-multilabel") for quick identification
- **Cross-Task Compatibility**: Same label structure works for binary, multi-class, and multi-label tasks
- **Template Validation**: Templates declare supported task types for automatic compatibility checking
- **Provenance Tracking**: Original labels preserved alongside standardized format

### Next Steps
- ✅ **Repository Structure Created**: Complete `src/` directory structure with base classes and placeholders
- ✅ **Base Classes Implemented**: BaseLoader, BaseTemplate, and core data structures (StandardizedAnnotations, RawDataPoint, QuestionAnswer, Datum)
- ✅ **Architecture Documented**: Developer-friendly documentation in `docs/architecture.md` with clear explanations and examples
- ✅ **Data Flow Clarified**: Complete walkthrough showing how data moves from raw dataset to final JSONL
- ✅ **Domain-First Organization**: Templates organized by domain with proper naming convention and BaseTemplate domain attribute
- Create concrete loader and template implementations once datasets and template designs are chosen
- Start with one example loader and template to test the approach
- Validate against the datum schema from `instructions/datum_schema.md`

## Repository Structure Created ✅

```
src/mbu_dataset_standardization/
├── __init__.py          # Package initialization with public API
├── datum.py            # Core data structures and schema validation
├── loaders.py          # BaseLoader class (concrete implementations TODO)
├── templates.py        # BaseTemplate class (concrete implementations TODO)
├── convert.py          # Main conversion orchestrator (implementation TODO)
└── utils.py            # Helper functions (implementations TODO)
```

**Key Features Implemented:**
- ✅ Complete `StandardizedAnnotations` with `task_type` field for quick identification
- ✅ **Pydantic models** for automatic validation and JSON serialization (instead of dataclasses)
- ✅ Abstract base classes with clear interfaces
- ✅ Clean, minimal code - no unnecessary validators or boilerplate
- ✅ Manual registries (LOADERS/TEMPLATES dicts) instead of complex registry pattern
- ✅ Absolute imports throughout codebase
- ✅ Minimal utils.py - implement only what's needed
- ✅ Ready for concrete implementations once datasets are chosen

**Design Decision: Pydantic over Dataclasses**
- Better JSON serialization with built-in `model_dump_json()` and field aliases
- Automatic validation on object creation 
- Schema compliance without custom serialization code
- Critical for data quality across 500+ medical datasets

**Design Decision: Domain-First Template Organization**
- Templates organized by domain first: `domain-agnostic/` and `domain-specific/{domain}/`
- Naming convention: `{domain}_{task}_{subtype}_{difficulty}.md`
- Examples: `agnostic_classification_binary_1.md`, `radiology_classification_binary_1.md`
- Enables medical domain expertise while maintaining general-purpose templates
- BaseTemplate class includes `domain` attribute for template identification
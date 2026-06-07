# SOX Password Control Documentation Assistant

A comprehensive web application for SOX management testing of password security controls across in-scope systems, servers, operating systems, databases, and applications.

## Overview

This application helps SOX/ICFR management testing teams:
- Document password security control testing
- Collect structured evidence
- Assess evidence quality and identify gaps
- Track exceptions and approvals
- Generate management testing documentation
- Produce audit-ready reports

## Key Features

✅ **Project Management**: Create and manage SOX testing projects
✅ **Control Definition**: Define password security control parameters
✅ **Asset Population**: Import or manually enter in-scope systems and components
✅ **Password Policy**: Define and manage password policy requirements
✅ **Evidence Upload**: Upload and classify evidence files
✅ **Evidence Quality Assessment**: Automated IPE and quality checks
✅ **Testing Matrix**: Map evidence to control parameters
✅ **Exception Management**: Track exceptions and approvals
✅ **Follow-up Tracking**: Generate follow-up request sheets
✅ **Documentation**: Generate professional SOX workpapers
✅ **AI/ML Assistance**: Intelligent evidence classification and gap detection
✅ **Export Capabilities**: Excel, Word, PDF, and ZIP exports

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: SQLite (local)
- **Data Processing**: Pandas, NumPy
- **Document Generation**: python-docx, openpyxl
- **ML/AI**: scikit-learn
- **File Processing**: Pillow, PyPDF2

## Installation

### Prerequisites
- Python 3.9+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/vikaskkatiyar-lab/Security-review-control.git
cd Security-review-control
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the application:
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Usage

### Workflow

1. **Project Setup**: Create a new testing project with basic metadata
2. **Control Definition**: Define the password security control being tested
3. **Asset Population**: Upload or manually enter in-scope systems
4. **Password Policy**: Enter password policy requirements
5. **Evidence Upload**: Upload evidence files (screenshots, exports, policies, approvals)
6. **Evidence Mapping**: Map evidence to specific assets and parameters
7. **Quality Review**: Review automated quality assessments and IPE checks
8. **Testing Matrix**: Document password configuration for each asset
9. **Exception Log**: Track exceptions and gaps
10. **Exception Approvals**: Upload and validate exception approvals
11. **Follow-ups**: Generate follow-up request sheets
12. **Documentation**: Generate management testing workpapers
13. **Export**: Download outputs in Excel, Word, PDF formats

### Core Pages

- **Home**: Dashboard with project summary and readiness status
- **Project Setup**: Create and manage testing projects
- **Control Definition**: Define control attributes and testing approach
- **Asset Population**: Manage in-scope systems and components
- **Password Policy**: Define password policy requirements
- **Evidence Upload**: Upload and classify evidence files
- **Evidence Mapping**: Link evidence to assets and parameters
- **Evidence Quality Review**: Automated IPE and completeness checks
- **Testing Matrix**: Document password configurations and test results
- **Exception Log**: Track exceptions with risk ratings and status
- **Exception Approvals**: Manage exception approvals and compensating controls
- **Follow-Up Tracker**: Track and manage follow-up requests
- **Documentation Generator**: Create professional SOX workpapers
- **Executive Summary**: Generate high-level summary reports
- **Export Centre**: Download reports and project data

## File Structure

```
sox_password_control_assistant/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python runtime version
├── README.md                       # This file
├── data/                           # Data storage
│   └── projects.db                 # SQLite database
├── evidence/                       # Uploaded evidence files
├── exports/                        # Generated exports
├── templates/                      # Document templates
├── src/
│   ├── __init__.py
│   ├── database.py                 # Database operations
│   ├── schemas.py                  # Data models
│   ├── rules.py                    # Rule engine for testing logic
│   ├── evidence_assessment.py      # Evidence quality assessment
│   ├── ml_assistant.py             # ML/AI assistance
│   ├── document_generator.py       # Word document generation
│   ├── excel_exporter.py           # Excel export functionality
│   ├── audit_trail.py              # Audit trail logging
│   └── utils.py                    # Utility functions
└── pages/
    ├── 01_Project_Setup.py
    ├── 02_Control_Definition.py
    ├── 03_Asset_Population.py
    ├── 04_Password_Policy.py
    ├── 05_Evidence_Upload.py
    ├── 06_Evidence_Mapping.py
    ├── 07_Evidence_Quality_Review.py
    ├── 08_Testing_Matrix.py
    ├── 09_Exception_Log.py
    ├── 10_Exception_Approvals.py
    ├── 11_Follow_Up_Tracker.py
    ├── 12_Documentation_Generator.py
    ├── 13_Executive_Summary.py
    └── 14_Export_Centre.py
```

## Data Model

### Entities

- **Project**: Testing project metadata
- **Control**: Password security control definition
- **Asset**: In-scope systems and components
- **PasswordPolicy**: Password policy requirements
- **Evidence**: Uploaded evidence files
- **EvidenceAssessment**: Quality and IPE assessment
- **TestResult**: Password configuration testing results
- **Exception**: Identified exceptions and gaps
- **ExceptionApproval**: Exception approvals and compensating controls
- **FollowUp**: Follow-up requests
- **AuditTrail**: Activity log

## AI/ML Features

The application includes intelligent assistance for:

1. **Evidence Type Classification**: Automatically classify evidence files (screenshot, export, policy, approval, SOC extract)
2. **Evidence Quality Scoring**: Assess evidence completeness and quality
3. **Missing Information Detection**: Identify likely missing elements
4. **Similar Exception Clustering**: Group repeated exceptions
5. **Follow-up Wording Suggestion**: Draft follow-up request text
6. **Testing Narrative Suggestion**: Generate workpaper narrative
7. **Reviewer Risk Flags**: Highlight items needing senior review
8. **Evidence-to-Asset Matching**: Suggest asset mappings

**Important**: All AI suggestions are labeled and editable. Human review and approval is mandatory. AI outputs are not automatically applied.

## Rule Engine

The application includes a rule-based testing engine that automatically:

- Compares actual configurations to policy requirements
- Identifies configuration gaps
- Flags evidence quality issues
- Creates exceptions based on defined rules
- Validates exception approvals
- Generates follow-up requests

Example rules:
- If password length < policy requirement → Exception
- If complexity disabled and policy requires → Exception
- If evidence date outside testing period → IPE issue
- If evidence missing system name → Follow-up required
- If exception approval expired → Keep open

## Security & Privacy

- **Local Storage Only**: All data stored locally in SQLite database
- **No External APIs**: No cloud calls or external dependencies in first version
- **Evidence Privacy**: Uploaded evidence files stored securely in local folder
- **Audit Trail**: Complete activity log maintained
- **No Hardcoded Secrets**: Configuration-driven approach

## Outputs

The application generates downloadable outputs:

1. **Asset Population Template** (Excel)
2. **Password Policy Template** (Excel)
3. **Evidence Tracker** (Excel)
4. **Testing Matrix** (Excel)
5. **Exception Log** (Excel)
6. **Follow-up Tracker** (Excel)
7. **Management Testing Workpaper** (Word)
8. **Executive Summary** (PDF/Word)
9. **Full Project Export** (ZIP)

## Testing the Application

### Quick Start

1. Create a new project with basic metadata
2. Define a password security control
3. Upload the asset population template and add sample systems
4. Enter password policy requirements
5. Upload sample evidence files
6. Map evidence to assets
7. Review evidence quality assessment
8. Run testing matrix
9. Add sample exceptions
10. Generate documentation
11. Export results

### Sample Data

The application includes helper functions to generate sample data for testing:
- Use the "Generate Sample Data" option on the Home page
- This creates sample projects, assets, policies, evidence, and results

## Known Limitations

1. **First Version**: This is Version 1.0. Some advanced features may be enhanced in future releases.
2. **PDF Generation**: Uses Word to PDF conversion; ensure Word is installed for direct PDF generation.
3. **File Size**: Evidence upload limited to available disk space; recommend organizing by project.
4. **Concurrent Users**: Single-user local application; not suitable for multi-user deployment without modifications.
5. **Evidence Search**: Limited to local database; no full-text search across evidence content.
6. **AI Models**: Uses simple scikit-learn models; consider upgrading to transformer-based models for better accuracy.

## Recommended Next Enhancements

### Phase 2
- [ ] Multi-user support with role-based access control
- [ ] Cloud storage integration (AWS S3, Azure Blob)
- [ ] Advanced AI/ML with transformer models
- [ ] Full-text search across evidence
- [ ] Workflow automation and alerts
- [ ] Integration with issue tracking systems
- [ ] API for third-party integrations
- [ ] Advanced reporting and dashboards

### Phase 3
- [ ] Mobile app for field evidence capture
- [ ] Real-time collaboration features
- [ ] Integration with security scanning tools
- [ ] Automated evidence collection from systems
- [ ] Multi-project portfolio view
- [ ] Regulatory compliance mappings
- [ ] Risk heat maps and trend analysis

## Support & Troubleshooting

### Common Issues

**Issue**: Database locked error
- **Solution**: Close other instances of the app and try again

**Issue**: Evidence file not uploading
- **Solution**: Check file size and format; ensure evidence folder exists

**Issue**: Slow performance with large datasets
- **Solution**: Consider exporting old projects; optimize database queries

### Logs

Audit trail is maintained in the database. Access via:
- Pages > (any page) > View Audit Trail

## Contributing

For feedback, bugs, or feature requests, please create an issue in the repository.

## License

Internal use only. Proprietary application for SOX management testing.

## Contact

For questions or support, contact the SOX control documentation team.

---

**Version**: 1.0.0
**Last Updated**: 2026-06-07
**Status**: Production Ready

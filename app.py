import streamlit as st
import os
from datetime import datetime
from pathlib import Path

# Ensure data and evidence directories exist
Path("data").mkdir(exist_ok=True)
Path("evidence").mkdir(exist_ok=True)
Path("exports").mkdir(exist_ok=True)
Path("templates").mkdir(exist_ok=True)

from src.database import init_db, get_project, get_all_projects
from src.audit_trail import log_activity

# Page config
st.set_page_config(
    page_title="SOX Password Control Assistant",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
if 'db_initialized' not in st.session_state:
    init_db()
    st.session_state.db_initialized = True

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 20px;
    }
    .stat-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 10px 0;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        margin-top: 5px;
    }
    .alert-info {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #2196f3;
        margin: 10px 0;
    }
    .alert-warning {
        background-color: #fff3e0;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #ff9800;
        margin: 10px 0;
    }
    .alert-success {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #4caf50;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def render_home():
    """Render the home/dashboard page"""
    
    st.markdown('<div class="main-header">🔐 SOX Password Control Documentation Assistant</div>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    Welcome to the SOX Password Control Documentation Assistant. This application helps you:
    - Document password security control testing
    - Collect and assess evidence
    - Track exceptions and approvals
    - Generate management testing documentation
    
    **Getting Started:**
    1. Create a new project in the Project Setup page
    2. Define your control in Control Definition
    3. Add in-scope systems in Asset Population
    4. Enter password policy requirements
    5. Upload and map evidence
    6. Generate documentation
    """)
    
    st.divider()
    
    # Get active projects
    projects = get_all_projects()
    
    if projects:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="stat-box">
                <div class="stat-number">""" + str(len(projects)) + """</div>
                <div class="stat-label">Projects Created</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Summary statistics
        st.subheader("Quick Statistics")
        
        if projects:
            selected_project = st.selectbox(
                "Select a project for detailed view:",
                options=projects,
                format_func=lambda x: f"{x['project_name']} ({x['entity']})"
            )
            
            if selected_project:
                col1, col2, col3, col4 = st.columns(4)
                
                project_id = selected_project['id']
                
                # Placeholder statistics (to be populated from database queries)
                with col1:
                    st.markdown("""
                    <div class="stat-box">
                        <div class="stat-number">-</div>
                        <div class="stat-label">In-Scope Assets</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div class="stat-box">
                        <div class="stat-number">-</div>
                        <div class="stat-label">Evidence Files</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown("""
                    <div class="stat-box">
                        <div class="stat-number">-</div>
                        <div class="stat-label">Open Exceptions</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    st.markdown("""
                    <div class="stat-box">
                        <div class="stat-number">-</div>
                        <div class="stat-label">Follow-ups</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Project details
                st.subheader("Project Details")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Project Name**: {selected_project['project_name']}")
                    st.write(f"**Entity**: {selected_project['entity']}")
                    st.write(f"**Financial Year**: {selected_project['financial_year']}")
                
                with col2:
                    st.write(f"**Tester**: {selected_project['tester_name']}")
                    st.write(f"**Reviewer**: {selected_project['reviewer_name']}")
                    st.write(f"**Status**: {selected_project.get('status', 'Draft')}")
    else:
        st.info("📋 No projects yet. Create your first project in the **Project Setup** page.")
    
    st.divider()
    
    # Help section
    st.subheader("📚 Application Guide")
    
    with st.expander("How to use this application"):
        st.markdown("""
        ### Workflow Overview
        
        **Phase 1: Project Setup**
        - Create a new testing project with entity, period, and team information
        - Define your control and testing scope
        
        **Phase 2: Asset & Policy Definition**
        - Upload or manually enter in-scope systems
        - Define password policy requirements
        - Map systems to policy requirements
        
        **Phase 3: Evidence Collection**
        - Upload evidence files (screenshots, exports, policies)
        - Classify and map evidence to assets and parameters
        - System performs automated quality checks
        
        **Phase 4: Testing & Assessment**
        - Review testing matrix results
        - Compare actual vs. policy requirements
        - Identify exceptions and gaps
        
        **Phase 5: Exception Management**
        - Track exceptions with risk ratings
        - Upload and validate exception approvals
        - Document compensating controls
        
        **Phase 6: Documentation**
        - Generate follow-up request sheets
        - Create management testing workpapers
        - Export results in Excel, Word, PDF
        
        ### Key Features
        
        ✅ **Structured Evidence Assessment**: Automated IPE checks
        ✅ **AI-Assisted Gap Detection**: ML-based missing information detection
        ✅ **Professional Documentation**: SOX-compliant workpapers
        ✅ **Exception Tracking**: Complete audit trail
        ✅ **Flexible Exports**: Multiple output formats
        """)
    
    with st.expander("Data Privacy & Security"):
        st.markdown("""
        ### Security Measures
        
        🔒 **Local Storage Only**: All data stored locally in SQLite database
        🔒 **No External APIs**: No cloud calls or external dependencies
        🔒 **Evidence Privacy**: Uploaded files stored in secure local folder
        🔒 **Audit Trail**: Complete activity log maintained
        🔒 **No Secrets**: No hardcoded credentials
        
        ### Important Warnings
        
        ⚠️ **Confidential Information**: Uploaded evidence may contain sensitive system configuration details
        ⚠️ **Access Control**: Ensure appropriate access controls on local file system
        ⚠️ **Backup**: Regularly backup the data/ and evidence/ folders
        """)

def main():
    """Main application entry point"""
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("## Navigation")
        page = st.radio(
            "Select a page:",
            options=[
                "Home",
                "Project Setup",
                "Control Definition",
                "Asset Population",
                "Password Policy",
                "Evidence Upload",
                "Evidence Mapping",
                "Evidence Quality Review",
                "Testing Matrix",
                "Exception Log",
                "Exception Approvals",
                "Follow-Up Tracker",
                "Documentation Generator",
                "Executive Summary",
                "Export Centre",
                "Settings"
            ],
            label_visibility="collapsed"
        )
        
        st.divider()
        st.markdown("### About")
        st.markdown("""
        **Version**: 1.0.0
        **Purpose**: SOX Management Testing
        **Focus**: Password Security Controls
        """)
    
    if page == "Home":
        render_home()
    elif page == "Project Setup":
        from pages.pages_01_project_setup import render_project_setup
        render_project_setup()
    elif page == "Control Definition":
        from pages.pages_02_control_definition import render_control_definition
        render_control_definition()
    elif page == "Asset Population":
        from pages.pages_03_asset_population import render_asset_population
        render_asset_population()
    elif page == "Password Policy":
        from pages.pages_04_password_policy import render_password_policy
        render_password_policy()
    elif page == "Evidence Upload":
        from pages.pages_05_evidence_upload import render_evidence_upload
        render_evidence_upload()
    elif page == "Evidence Mapping":
        from pages.pages_06_evidence_mapping import render_evidence_mapping
        render_evidence_mapping()
    elif page == "Evidence Quality Review":
        from pages.pages_07_evidence_quality_review import render_evidence_quality_review
        render_evidence_quality_review()
    elif page == "Testing Matrix":
        from pages.pages_08_testing_matrix import render_testing_matrix
        render_testing_matrix()
    elif page == "Exception Log":
        from pages.pages_09_exception_log import render_exception_log
        render_exception_log()
    elif page == "Exception Approvals":
        from pages.pages_10_exception_approvals import render_exception_approvals
        render_exception_approvals()
    elif page == "Follow-Up Tracker":
        from pages.pages_11_follow_up_tracker import render_follow_up_tracker
        render_follow_up_tracker()
    elif page == "Documentation Generator":
        from pages.pages_12_documentation_generator import render_documentation_generator
        render_documentation_generator()
    elif page == "Executive Summary":
        from pages.pages_13_executive_summary import render_executive_summary
        render_executive_summary()
    elif page == "Export Centre":
        from pages.pages_14_export_centre import render_export_centre
        render_export_centre()
    elif page == "Settings":
        st.title("Settings")
        st.info("Settings page - to be implemented")

if __name__ == "__main__":
    main()

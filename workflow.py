class WorkflowManager:
    def __init__(self):
        import streamlit as st
        if "workflow_state" not in st.session_state:
            st.session_state["workflow_state"] = "ingest"
        self._state = st.session_state["workflow_state"]

    @property
    def state(self):
        import streamlit as st
        return st.session_state.get("workflow_state", "ingest")

    def advance(self, next_state):
        import streamlit as st
        st.session_state["workflow_state"] = next_state

    def reset(self):
        import streamlit as st
        st.session_state["workflow_state"] = "ingest"
        st.session_state.pop("data", None)
        st.session_state.pop("qc_report", None)
        st.session_state.pop("analysis_results", None)

    @property
    def data(self):
        import streamlit as st
        return st.session_state.get("data", None)

    @data.setter
    def data(self, value):
        import streamlit as st
        st.session_state["data"] = value

    @property
    def qc_report(self):
        import streamlit as st
        return st.session_state.get("qc_report", None)

    @qc_report.setter
    def qc_report(self, value):
        import streamlit as st
        st.session_state["qc_report"] = value

    @property
    def analysis_results(self):
        import streamlit as st
        return st.session_state.get("analysis_results", None)

    @analysis_results.setter
    def analysis_results(self, value):
        import streamlit as st
        st.session_state["analysis_results"] = value

from preswald import text, connect, get_df, table, slider, query, plotly
import plotly.express as px

# — Page Header —
text("# Global Cancer Patients Explorer")
text("Interactive dashboard for 2015–2024 cancer patient data")

# — Load Data —
connect()
df = get_df("sample_csv")

table(df, title="Full Dataset")

# determine number of cancer types for sizing
cancer_types = df["Cancer_Type"].unique()
n_types = len(cancer_types)

# — Fig 1: Treatment Cost vs Age
fig1 = px.scatter(
    df,
    x="Age",
    y="Treatment_Cost_USD",
    color="Cancer_Type",
    facet_row="Cancer_Type",
    hover_data=["Gender", "Cancer_Stage", "Survival_Years"],
    title="💉 Treatment Cost vs Age by Cancer Type"
)
fig1.update_traces(marker=dict(size=8, opacity=0.7, line=dict(width=0.5)))
fig1.update_layout(
    template="plotly_white",
    height=200 * n_types,
    width=800,
    margin=dict(t=60, l=50, r=50, b=40),
    showlegend=False
)
plotly(fig1)

# — Fig 2: Air Pollution vs Severity 
fig2 = px.scatter(
    df,
    x="Air_Pollution",
    y="Target_Severity_Score",
    color="Cancer_Type",
    facet_row="Cancer_Type",
    hover_data=["Age", "Gender", "Cancer_Stage"],
    title="🌫️ Air Pollution vs Severity Score by Cancer Type"
)
fig2.update_traces(marker=dict(size=8, opacity=0.7, line=dict(width=0.5)))
fig2.update_layout(
    template="plotly_white",
    height=200 * n_types,
    width=800,
    margin=dict(t=60, l=50, r=50, b=40),
    showlegend=False
)
plotly(fig2)

# — Fig 3: Alcohol Use vs Severity
fig3 = px.scatter(
    df,
    x="Alcohol_Use",
    y="Target_Severity_Score",
    color="Cancer_Type",
    facet_row="Cancer_Type",
    hover_data=["Age", "Gender", "Cancer_Stage"],
    title="🍷 Alcohol Use vs Severity Score by Cancer Type"
)
fig3.update_traces(marker=dict(size=8, opacity=0.7, line=dict(width=0.5)))
fig3.update_layout(
    template="plotly_white",
    height=200 * n_types,
    width=800,
    margin=dict(t=60, l=50, r=50, b=40),
    showlegend=False
)
plotly(fig3)

# - Fig 4: Smoking vs Severity
fig4 = px.scatter(
    df,
    x="Smoking",
    y="Target_Severity_Score",
    color="Cancer_Type",
    facet_row="Cancer_Type",
    hover_data=["Age", "Gender", "Cancer_Stage"],
    title="🚬 Smoking vs Severity Score by Cancer Type"
)
fig4.update_traces(marker=dict(size=8, opacity=0.7, line=dict(width=0.5)))
fig4.update_layout(
    template="plotly_white",
    height=200 * n_types,
    width=800,
    margin=dict(t=60, l=50, r=50, b=40),
    showlegend=False
)
plotly(fig4)

# — Fig 5: Genetic Risk vs Severity 
fig5 = px.scatter(
    df,
    x="Genetic_Risk",
    y="Target_Severity_Score",
    color="Cancer_Type",
    facet_row="Cancer_Type",
    hover_data=["Age", "Gender", "Cancer_Stage"],
    title="🧬 Genetic Risk vs Severity Score by Cancer Type"
)
fig5.update_traces(marker=dict(size=8, opacity=0.7, line=dict(width=0.5)))
fig5.update_layout(
    template="plotly_white",
    height=200 * n_types,
    width=800,
    margin=dict(t=60, l=50, r=50, b=40),
    showlegend=False
)
plotly(fig5)


# - Severity Threshold slider
sev_thresh = slider(
    "Severity Threshold",
    min_val=0,
    max_val=10,
    default=5
)
filtered = df[df["Target_Severity_Score"] > sev_thresh]
table(filtered, title=f"🟠 Severity > {sev_thresh} (Slider)")



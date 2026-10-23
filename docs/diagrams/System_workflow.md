flowchart TD

    A[Start] --> B[Vehicle Data Input]

    B --> C[CSV Vehicle Data]
    C --> D[Data Preprocessing]

    D --> E[Vehicle Tracking]

    E --> F[Fleet Monitoring]
    E --> G[Driver Monitoring]
    E --> H[Fuel Prediction]
    E --> I[Route Optimization]

    F --> J{Vehicle Status}
    J -->|Active| K[Monitor Speed & Location]
    J -->|Inactive| L[Show Inactive Vehicle]

    G --> M[Monitor Driver Activity]
    M --> N[Detect Driving Behaviour]

    H --> O[AI Prediction Model]
    O --> P[Predict Fuel Consumption]

    I --> Q[Analyze Route Data]
    Q --> R[Suggest Optimized Route]

    K --> S[Dashboard]
    L --> S
    N --> S
    P --> S
    R --> S

    S --> T[Display Reports]
    T --> U[End]
# Risk Analysis

After the risks are identified in the first phase of risk assessment process, they should be analyzed. Analysis is done to understand possibility and consequences of each risk. Information like historical data and theoretical analysis about each risk should gathered to gain greater understanding of the risk.

### Analysis Methods 

Risks can be assessed by using different methodologies. In this documentation the methods are based on quolitative, semi-quontitave and quontitave methodologies. 

In **quolitative**, potential losses caused by risk are determined using different metrics like vulnerabilities related to the risk or controls that reduce effectiveness of the risk. After risk is identified using those metrics, it can be assessed in a matrix using importance and occurring possibility as metrics. CIRA and CORAS are methodologies using qualitative approach.

**Semi-quantitative** methods are used to describe the relative risk scale. This approach tries to combine benefits of quolitative and quontitative methodologies to decrease disadvantages of the two. Risks can be classified into different rankings like low, medium, high etc. Minimum of these ranking levels is 3. Risk-Level matrix with two metrics; impact and threat likelihood is created using these levels. Each level equals to certain number of points e.g. medium level impact could be 10 points and critical level impact could be 100 points. Higher impact and likelihood mean greater points. Table below contains example of Risk-Level matrix.

|                       | Impact                | Impact                    | Impact                   | Impact                     |
|-----------------------|-----------------------|---------------------------|--------------------------|----------------------------|
| **Threat Likelihood** | Low (10)              | Medium (50)               | High (75)                | Critical (100)             |
| Critical (1.0)        | Low (1.0 x 10 = 10)   | Medium (1.0 x 50 = 50)    | High (1.0 x 75 = 75)     | Critical (1.0 x 100 = 100) |
| High (0.75)           | Low (0.75 x 10 = 7.5) | Medium (0.75 x 50 = 37.5) | High (0.75 x 75 = 56.25) | High (0.75 x 100 = 75)     |
| Medium (0.5)          | Low (0.5 x 10 = 5)    | Medium (0.5 x 50 = 25)    | Medium (0.5 x 75 = 37.5) | Medium (0.5 x 100 = 50)    |
| Low (0.1)             | Low (0.1 x 10 = 1)    | Low (0.1 x 50 = 5)        | Low (0.1 x 75 = 7.5)     | Low (0.1 x 100 = 10)       |

As seen from the table above, each risk has rating between 1-100. The rating can be used to reflect seriousness of the risk and should be taken to account when doing [risk evaluation](../Risk Evaluation/).

**Quantitative** risk assessment offers more mathematical and objective approach compared to qualitative methods. Quantitative approaches are Monte Carlo method, historical simulation method, IS, ISRAM and Delphi method.

### References

<ul>
    <li>https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/administrative/securityrule/rafinalguidancepdf.pdf</li>
    <li>http://www.madrid.org/cs/StaticFiles/Emprendedores/Analisis_Riesgos/pages/pdf/metodologia/4AnalisisycuantificaciondelRiesgo%28AR%29_en.pdf</li>
    <li>http://www.jcomputers.us/vol12/jcp1201-06.pdf</li>
    <li>http://anale.feaa.uaic.ro/anale/resurse/50_I02_Radu.pdf</li>
    <li>https://www.projectpractical.com/quantitative-risk-analysis/</li>
<ul>

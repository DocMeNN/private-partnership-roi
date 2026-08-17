from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from calculator import calculate
from assumptions import SCALING_LEVELS


HOST = "127.0.0.1"
PORT = 8501


def money(value):
    return f"₦{value:,.0f}"


def num(value):
    return f"{value:,.0f}"


def pct(value):
    return f"{value:.1f}%"


class DashboardHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        query = parse_qs(urlparse(self.path).query)

        def get_number(name, default):

            try:
                return float(query.get(name, [default])[0])

            except (ValueError, TypeError):

                return float(default)


        chews = int(get_number("chews", 10))

        patients_per_chew = get_number(
            "patients_per_chew",
            10
        )

        subscription = get_number(
            "subscription",
            15000
        )

        chew_salary = get_number(
            "chew_salary",
            110000
        )


        if chews < 1:
            chews = 1


        # =========================================================
        # CORE MODEL
        # =========================================================

        patients = int(
            chews * patients_per_chew
        )


        monthly_revenue = (
            patients * subscription
        )

        annual_revenue = (
            monthly_revenue * 12
        )


        monthly_chew_cost = (
            chews * chew_salary
        )

        annual_chew_cost = (
            monthly_chew_cost * 12
        )


        monthly_contribution = (
            monthly_revenue
            - monthly_chew_cost
        )

        annual_contribution = (
            annual_revenue
            - annual_chew_cost
        )


        result = calculate(chews)

        setup_cost = result[
            "confirmed_setup_cost"
        ]


        # =========================================================
        # FINANCIAL INTERPRETATION
        # =========================================================

        revenue_per_chew = (
            monthly_revenue / chews
            if chews else 0
        )


        revenue_per_patient = (
            monthly_revenue / patients
            if patients else 0
        )


        contribution_per_chew = (
            monthly_contribution / chews
            if chews else 0
        )


        contribution_per_patient = (
            monthly_contribution / patients
            if patients else 0
        )


        setup_cost_per_chew = (
            setup_cost / chews
            if chews else 0
        )


        setup_cost_per_patient = (
            setup_cost / patients
            if patients else 0
        )


        contribution_margin = (
            (monthly_contribution / monthly_revenue) * 100
            if monthly_revenue else 0
        )


        if monthly_contribution > 0:

            preliminary_payback_months = (
                setup_cost / monthly_contribution
            )

        else:

            preliminary_payback_months = 0


        # =========================================================
        # SCALE TABLE
        # =========================================================

        scenario_rows = ""


        for level in SCALING_LEVELS:

            level_result = calculate(level)

            level_patients = int(
                level * patients_per_chew
            )


            level_monthly_revenue = (
                level_patients
                * subscription
            )


            level_annual_revenue = (
                level_monthly_revenue
                * 12
            )


            level_monthly_chew_cost = (
                level * chew_salary
            )


            level_contribution = (
                level_monthly_revenue
                - level_monthly_chew_cost
            )


            level_margin = (
                (
                    level_contribution
                    / level_monthly_revenue
                ) * 100
                if level_monthly_revenue
                else 0
            )


            active = (
                " class='active'"
                if level == chews
                else ""
            )


            scenario_rows += f"""
            <tr{active}>

                <td>{num(level)}</td>

                <td>{num(level_patients)}</td>

                <td>{money(level_monthly_revenue)}</td>

                <td>{money(level_result['confirmed_setup_cost'])}</td>

                <td>{money(level_contribution)}</td>

                <td>{pct(level_margin)}</td>

            </tr>
            """


        # =========================================================
        # HTML
        # =========================================================

        html = f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>
EasePal Care — Private Partnership ROI Dashboard
</title>


<style>

* {{
    box-sizing: border-box;
}}


body {{
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: #f3f6f8;
    color: #17212b;
}}


.header {{
    background: #123b5d;
    color: white;
    padding: 25px 40px;
}}


.header h1 {{
    margin: 0;
    font-size: 25px;
}}


.header p {{
    margin: 7px 0 0;
    opacity: .85;
}}


.container {{
    max-width: 1500px;
    margin: auto;
    padding: 30px;
}}


.layout {{
    display: grid;
    grid-template-columns: 320px 1fr;
    gap: 24px;
}}


.card {{
    background: white;
    border-radius: 10px;
    padding: 24px;
    margin-bottom: 24px;
    box-shadow: 0 2px 10px rgba(0,0,0,.07);
}}


.card h2 {{
    margin-top: 0;
    color: #123b5d;
}}


.card h3 {{
    color: #123b5d;
    margin-top: 26px;
}}


label {{
    display: block;
    margin-top: 17px;
    margin-bottom: 6px;
    font-weight: bold;
    font-size: 13px;
}}


input {{
    width: 100%;
    padding: 11px;
    border: 1px solid #ccd5dc;
    border-radius: 6px;
    font-size: 15px;
}}


button {{
    width: 100%;
    margin-top: 22px;
    padding: 13px;
    border: none;
    border-radius: 6px;
    background: #123b5d;
    color: white;
    font-weight: bold;
    cursor: pointer;
}}


.kpis {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
}}


.kpi {{
    background: #f8fafb;
    border: 1px solid #e2e8ed;
    border-radius: 8px;
    padding: 17px;
}}


.kpi-label {{
    font-size: 11px;
    color: #66737e;
    text-transform: uppercase;
    font-weight: bold;
}}


.kpi-value {{
    margin-top: 8px;
    font-size: 20px;
    font-weight: bold;
    color: #123b5d;
}}


.interpretation {{
    background: #f8fafb;
    border-left: 4px solid #123b5d;
    padding: 17px;
    margin-top: 15px;
    line-height: 1.6;
    font-size: 13px;
}}


.warning {{
    margin-top: 18px;
    padding: 15px;
    background: #fff8df;
    border-left: 4px solid #d6a900;
    font-size: 12px;
    line-height: 1.6;
}}


.tbd {{
    background: #fff8df;
    border: 1px solid #ead58a;
    padding: 15px;
    border-radius: 7px;
    font-size: 12px;
    line-height: 1.7;
}}


table {{
    width: 100%;
    border-collapse: collapse;
}}


th,
td {{
    padding: 11px 10px;
    border-bottom: 1px solid #e5eaee;
    text-align: right;
    font-size: 12px;
}}


th:first-child,
td:first-child {{
    text-align: left;
}}


th {{
    background: #edf3f7;
    color: #123b5d;
}}


tr.active {{
    background: #e5f1f7;
    font-weight: bold;
}}


.formula {{
    background: #f3f6f8;
    padding: 13px;
    border-radius: 6px;
    margin-top: 10px;
    font-family: Consolas, monospace;
    font-size: 12px;
}}


.footer {{
    text-align: center;
    padding: 25px;
    color: #697780;
    font-size: 11px;
}}


@media(max-width: 900px) {{

    .layout {{
        grid-template-columns: 1fr;
    }}

    .kpis {{
        grid-template-columns: repeat(2, 1fr);
    }}

    .container {{
        padding: 15px;
    }}

}}

</style>

</head>


<body>


<div class="header">

<h1>
EasePal Care — Private Partnership ROI & Scaling Dashboard
</h1>

<p>
Version 1.0 • Financial Scaling & Partnership Decision Tool
</p>

</div>


<div class="container">


<div class="layout">


<!-- INPUTS -->

<div>

<div class="card">

<h2>Model Inputs</h2>

<form method="GET">


<label>
Number of CHEWs
</label>

<input
type="number"
name="chews"
min="1"
value="{chews}"
>


<label>
Patients per CHEW
</label>

<input
type="number"
name="patients_per_chew"
min="1"
value="{patients_per_chew}"
>


<label>
Private Subscription / Patient / Month (₦)
</label>

<input
type="number"
name="subscription"
min="0"
value="{subscription}"
>


<label>
CHEW Remuneration / Month (₦)
</label>

<input
type="number"
name="chew_salary"
min="0"
value="{chew_salary}"
>


<button type="submit">
CALCULATE
</button>

</form>

</div>


<div class="card">

<h2>Core Assumptions</h2>

<p>
<strong>CHEW : Patient ratio</strong>
<br>
1 : {num(patients_per_chew)}
</p>

<p>
<strong>Subscription</strong>
<br>
{money(subscription)} / patient / month
</p>

<p>
<strong>CHEW remuneration</strong>
<br>
{money(chew_salary)} / month
</p>


<div class="warning">

<strong>Model limitation:</strong>

<br><br>

Contribution and payback are
<strong>preliminary</strong> because several
operating cost categories remain TBD.

</div>

</div>

</div>


<!-- MAIN -->

<div>


<!-- PRIMARY KPIs -->

<div class="card">

<h2>
Selected Scenario — {num(chews)} CHEWs
</h2>


<div class="kpis">


<div class="kpi">

<div class="kpi-label">
Patients
</div>

<div class="kpi-value">
{num(patients)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Monthly Revenue
</div>

<div class="kpi-value">
{money(monthly_revenue)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Annual Revenue
</div>

<div class="kpi-value">
{money(annual_revenue)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Confirmed Setup Cost
</div>

<div class="kpi-value">
{money(setup_cost)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Monthly CHEW Cost
</div>

<div class="kpi-value">
{money(monthly_chew_cost)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Monthly Contribution
</div>

<div class="kpi-value">
{money(monthly_contribution)}
</div>

</div>


</div>

</div>


<!-- UNIT ECONOMICS -->

<div class="card">

<h2>
Unit Economics
</h2>


<div class="kpis">


<div class="kpi">

<div class="kpi-label">
Revenue / CHEW / Month
</div>

<div class="kpi-value">
{money(revenue_per_chew)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Revenue / Patient / Month
</div>

<div class="kpi-value">
{money(revenue_per_patient)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Contribution / CHEW
</div>

<div class="kpi-value">
{money(contribution_per_chew)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Contribution / Patient
</div>

<div class="kpi-value">
{money(contribution_per_patient)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Setup Cost / CHEW
</div>

<div class="kpi-value">
{money(setup_cost_per_chew)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Setup Cost / Patient
</div>

<div class="kpi-value">
{money(setup_cost_per_patient)}
</div>

</div>


</div>


<div class="formula">

Revenue / CHEW =
Patients per CHEW × Subscription

</div>


<div class="formula">

Setup Cost / Patient =
Confirmed Setup Cost ÷ Total Patients

</div>


</div>


<!-- PROFITABILITY -->

<div class="card">

<h2>
Preliminary Financial Performance
</h2>


<div class="kpis">


<div class="kpi">

<div class="kpi-label">
Contribution Margin
</div>

<div class="kpi-value">
{pct(contribution_margin)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Annual Contribution
</div>

<div class="kpi-value">
{money(annual_contribution)}
</div>

</div>


<div class="kpi">

<div class="kpi-label">
Preliminary Payback
</div>

<div class="kpi-value">

{
    f"{preliminary_payback_months:.1f} months"
    if monthly_contribution > 0
    else "N/A"
}

</div>

</div>


</div>


<div class="interpretation">

<strong>Management interpretation:</strong>

<br><br>

At the selected scale of
<strong>{num(chews)} CHEWs</strong>,
the model produces approximately
<strong>{money(monthly_revenue)}</strong>
in monthly subscription revenue.

After the currently modelled CHEW remuneration
of <strong>{money(monthly_chew_cost)}</strong>,
the preliminary monthly contribution is
<strong>{money(monthly_contribution)}</strong>.

</div>


<div class="warning">

<strong>Important:</strong>

This is NOT yet a final ROI, IRR, NPV or investment
return calculation.

The contribution currently excludes all unresolved
TBD operating costs.

The payback indicator is therefore a
<strong>preliminary model signal only</strong>.

</div>

</div>


<!-- SCALE -->

<div class="card">

<h2>
Scaling Economics
</h2>


<table>

<thead>

<tr>

<th>CHEWs</th>

<th>Patients</th>

<th>Monthly Revenue</th>

<th>Setup Cost</th>

<th>Monthly Contribution</th>

<th>Contribution Margin</th>

</tr>

</thead>


<tbody>

{scenario_rows}

</tbody>

</table>


</div>


<!-- FORMULAS -->

<div class="card">

<h2>
Financial Logic
</h2>


<div class="formula">

Patients =
CHEWs × Patients per CHEW

</div>


<div class="formula">

Monthly Revenue =
Patients × Subscription Price

</div>


<div class="formula">

Monthly Contribution =
Monthly Revenue − Monthly CHEW Cost

</div>


<div class="formula">

Contribution Margin =
Monthly Contribution ÷ Monthly Revenue

</div>


<div class="formula">

Preliminary Payback =
Confirmed Setup Cost ÷ Monthly Contribution

</div>


</div>


<!-- TBD -->

<div class="card">

<h2>
Outstanding Financial Inputs
</h2>


<div class="tbd">

The following remain <strong>TBD</strong>
and must be validated before the model can be
described as a complete investment ROI model:

<br><br>

• Deployment logistics

<br>
• Clinical supervision

<br>
• Technology / platform

<br>
• Monitoring & Evaluation

<br>
• Shared management overhead

<br>
• Business development

<br>
• CHEW replacement / attrition

<br>
• Contingency

<br>
• Other operating costs

</div>

</div>


</div>

</div>


</div>


<div class="footer">

EasePal Care • Private Partnership ROI & Scaling Dashboard • V1.0

</div>


</body>

</html>
"""


        data = html.encode("utf-8")


        self.send_response(200)

        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )

        self.send_header(
            "Content-Length",
            str(len(data))
        )

        self.end_headers()

        self.wfile.write(data)


    def log_message(self, format, *args):
        return


if __name__ == "__main__":

    server = HTTPServer(
        (HOST, PORT),
        DashboardHandler
    )

    print()
    print("=" * 70)
    print(" EASEPAL CARE — ROI DASHBOARD V1")
    print("=" * 70)
    print()
    print(
        f"Dashboard: http://{HOST}:{PORT}"
    )
    print()
    print("Press CTRL+C to stop.")
    print()

    server.serve_forever()

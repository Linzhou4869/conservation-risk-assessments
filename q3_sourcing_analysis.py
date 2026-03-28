#!/usr/bin/env python3
"""
Q3 Sourcing Review - Cost-Benefit Analysis
Fixed Parameters Analysis
"""

import json
from datetime import datetime
from pathlib import Path

# Fixed Parameters
PARAMS = {
    "base_fabric_cost": 12.00,
    "logistics": 3.50,
    "duty_rate": 0.08,  # 8%
    "target_margin": 0.15,  # 15%
    "cost_threshold": 17.50  # Flag if exceeds this
}

# Scenarios to analyze
SCENARIOS = [
    {
        "name": "Baseline - Current Supplier",
        "fabric_cost_adj": 1.0,
        "logistics_adj": 1.0,
        "duty_adj": 1.0,
        "volume_discount": 0.0,
        "quality_yield": 0.98
    },
    {
        "name": "Scenario A - Alternative Supplier (Vietnam)",
        "fabric_cost_adj": 0.92,
        "logistics_adj": 1.15,
        "duty_adj": 0.85,
        "volume_discount": 0.03,
        "quality_yield": 0.96
    },
    {
        "name": "Scenario B - Alternative Supplier (Bangladesh)",
        "fabric_cost_adj": 0.85,
        "logistics_adj": 1.25,
        "duty_adj": 0.90,
        "volume_discount": 0.05,
        "quality_yield": 0.94
    },
    {
        "name": "Scenario C - Premium Supplier (Italy)",
        "fabric_cost_adj": 1.35,
        "logistics_adj": 1.10,
        "duty_adj": 1.0,
        "volume_discount": 0.0,
        "quality_yield": 0.99
    },
    {
        "name": "Scenario D - Bulk Order (10K+ units)",
        "fabric_cost_adj": 0.88,
        "logistics_adj": 0.95,
        "duty_adj": 1.0,
        "volume_discount": 0.08,
        "quality_yield": 0.97
    },
    {
        "name": "Scenario E - Rush Production",
        "fabric_cost_adj": 1.20,
        "logistics_adj": 1.50,
        "duty_adj": 1.0,
        "volume_discount": 0.0,
        "quality_yield": 0.95
    },
]

def calculate_landed_cost(scenario, params):
    """Calculate total landed cost for a scenario."""
    base_fabric = params["base_fabric_cost"] * scenario["fabric_cost_adj"]
    logistics = params["logistics"] * scenario["logistics_adj"]
    duty_rate = params["duty_rate"] * scenario["duty_adj"]
    
    # Duty is applied to (fabric + logistics)
    subtotal = base_fabric + logistics
    duty_amount = subtotal * duty_rate
    
    # Apply volume discount
    pre_discount = subtotal + duty_amount
    volume_discount = pre_discount * scenario["volume_discount"]
    
    total_landed_cost = pre_discount - volume_discount
    
    # Calculate effective cost per good unit (accounting for yield)
    effective_cost = total_landed_cost / scenario["quality_yield"]
    
    # Calculate required selling price for target margin
    required_price = total_landed_cost / (1 - params["target_margin"])
    
    return {
        "base_fabric_cost": round(base_fabric, 2),
        "logistics_cost": round(logistics, 2),
        "duty_amount": round(duty_amount, 2),
        "duty_rate_used": round(duty_rate * 100, 2),
        "subtotal_before_discount": round(pre_discount, 2),
        "volume_discount": round(volume_discount, 2),
        "total_landed_cost": round(total_landed_cost, 2),
        "effective_cost_per_good_unit": round(effective_cost, 2),
        "required_selling_price": round(required_price, 2),
        "quality_yield": scenario["quality_yield"] * 100,
        "exceeds_threshold": total_landed_cost > params["cost_threshold"]
    }

def generate_report(results, params):
    """Generate markdown report."""
    report = []
    report.append("# Q3 Sourcing Review - Cost-Benefit Analysis")
    report.append("")
    report.append(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S GMT+8')}")
    report.append("")
    report.append("## Fixed Parameters")
    report.append("")
    report.append("| Parameter | Value |")
    report.append("|-----------|-------|")
    report.append(f"| Base Fabric Cost | ${params['base_fabric_cost']:.2f} |")
    report.append(f"| Logistics | ${params['logistics']:.2f} |")
    report.append(f"| Duty Rate | {params['duty_rate']*100:.1f}% |")
    report.append(f"| Target Margin | {params['target_margin']*100:.1f}% |")
    report.append(f"| Cost Threshold (Flag) | ${params['cost_threshold']:.2f} |")
    report.append("")
    report.append("## Executive Summary")
    report.append("")
    
    flagged = [r for r in results if r["cost_data"]["exceeds_threshold"]]
    viable = [r for r in results if not r["cost_data"]["exceeds_threshold"]]
    
    report.append(f"- **Total Scenarios Analyzed:** {len(results)}")
    report.append(f"- **Viable Scenarios (≤${params['cost_threshold']:.2f}):** {len(viable)}")
    report.append(f"- **⚠️ Flagged Scenarios (>${params['cost_threshold']:.2f}):** {len(flagged)}")
    report.append("")
    
    if viable:
        best = min(viable, key=lambda x: x["cost_data"]["total_landed_cost"])
        report.append(f"- **💰 Recommended:** {best['scenario_name']} @ ${best['cost_data']['total_landed_cost']:.2f}/unit")
    report.append("")
    
    report.append("## Detailed Analysis")
    report.append("")
    
    for result in results:
        report.append(f"### {result['scenario_name']}")
        report.append("")
        
        cost = result["cost_data"]
        status = "⚠️ **FLAGGED**" if cost["exceeds_threshold"] else "✅ Within Threshold"
        report.append(f"**Status:** {status}")
        report.append("")
        
        report.append("| Cost Component | Amount |")
        report.append("|----------------|--------|")
        report.append(f"| Base Fabric Cost | ${cost['base_fabric_cost']:.2f} |")
        report.append(f"| Logistics | ${cost['logistics_cost']:.2f} |")
        report.append(f"| Duty ({cost['duty_rate_used']:.1f}%) | ${cost['duty_amount']:.2f} |")
        report.append(f"| **Subtotal** | ${cost['subtotal_before_discount']:.2f} |")
        report.append(f"| Volume Discount | -${cost['volume_discount']:.2f} |")
        report.append(f"| **Total Landed Cost** | **${cost['total_landed_cost']:.2f}** |")
        report.append(f"| Effective Cost (per good unit, {cost['quality_yield']:.0f}% yield) | ${cost['effective_cost_per_good_unit']:.2f} |")
        report.append(f"| Required Selling Price ({params['target_margin']*100:.0f}% margin) | ${cost['required_selling_price']:.2f} |")
        report.append("")
    
    report.append("## Comparison Matrix")
    report.append("")
    report.append("| Scenario | Landed Cost | Effective Cost | Status |")
    report.append("|----------|-------------|----------------|--------|")
    
    sorted_results = sorted(results, key=lambda x: x["cost_data"]["total_landed_cost"])
    for result in sorted_results:
        cost = result["cost_data"]
        status = "⚠️ FLAGGED" if cost["exceeds_threshold"] else "✅"
        report.append(f"| {result['scenario_name']} | ${cost['total_landed_cost']:.2f} | ${cost['effective_cost_per_good_unit']:.2f} | {status} |")
    
    report.append("")
    report.append("## Recommendations")
    report.append("")
    
    if flagged:
        report.append("### ⚠️ Scenarios Requiring Review")
        report.append("")
        for r in flagged:
            report.append(f"- **{r['scenario_name']}**: ${r['cost_data']['total_landed_cost']:.2f} exceeds threshold by ${r['cost_data']['total_landed_cost'] - params['cost_threshold']:.2f}")
        report.append("")
    
    report.append("### Strategic Considerations")
    report.append("")
    report.append("1. **Cost vs. Quality Trade-off:** Lower landed cost scenarios may have reduced quality yield, affecting effective cost per good unit.")
    report.append("2. **Volume Leverage:** Bulk ordering (Scenario D) shows significant savings through volume discounts.")
    report.append("3. **Geographic Diversification:** Alternative suppliers offer cost savings but may introduce logistics complexity.")
    report.append("4. **Risk Mitigation:** Consider dual-sourcing to balance cost optimization with supply chain resilience.")
    report.append("")
    report.append("---")
    report.append("*Report generated by Q3 Sourcing Review Analysis*")
    
    return "\n".join(report)

def main():
    print("=" * 60)
    print("Q3 SOURCING REVIEW - COST-BENEFIT ANALYSIS")
    print("=" * 60)
    print()
    
    print("Fixed Parameters:")
    print(f"  Base Fabric Cost: ${PARAMS['base_fabric_cost']:.2f}")
    print(f"  Logistics: ${PARAMS['logistics']:.2f}")
    print(f"  Duty Rate: {PARAMS['duty_rate']*100:.1f}%")
    print(f"  Target Margin: {PARAMS['target_margin']*100:.1f}%")
    print(f"  Cost Threshold: ${PARAMS['cost_threshold']:.2f}")
    print()
    
    results = []
    for scenario in SCENARIOS:
        print(f"Analyzing: {scenario['name']}...")
        cost_data = calculate_landed_cost(scenario, PARAMS)
        results.append({
            "scenario_name": scenario["name"],
            "cost_data": cost_data
        })
        
        status = "⚠️ FLAGGED" if cost_data["exceeds_threshold"] else "✅ OK"
        print(f"  Landed Cost: ${cost_data['total_landed_cost']:.2f} [{status}]")
    
    print()
    print("Generating report...")
    
    # Generate and save report
    report = generate_report(results, PARAMS)
    
    workspace = Path("/mnt/afs_toolcall/zhoulin3/.openclaw/workspaces/gendata-worker-33")
    report_path = workspace / "q3_sourcing_review_report.md"
    report_path.write_text(report)
    
    # Also save JSON data for further analysis
    json_path = workspace / "q3_sourcing_review_data.json"
    json_path.write_text(json.dumps({
        "parameters": PARAMS,
        "scenarios": SCENARIOS,
        "results": results,
        "generated_at": datetime.now().isoformat()
    }, indent=2))
    
    print()
    print("=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"Report saved to: {report_path}")
    print(f"Data saved to: {json_path}")
    print()
    
    # Summary
    flagged = [r for r in results if r["cost_data"]["exceeds_threshold"]]
    if flagged:
        print("⚠️  FLAGGED SCENARIOS (exceeds $17.50 threshold):")
        for r in flagged:
            print(f"   - {r['scenario_name']}: ${r['cost_data']['total_landed_cost']:.2f}")
    else:
        print("✅ All scenarios within threshold.")

if __name__ == "__main__":
    main()

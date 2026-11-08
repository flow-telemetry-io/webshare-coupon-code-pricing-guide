#!/usr/bin/env python3
"""
Webshare Proxy Pricing & Coupon Savings Calculator 2026.
Calculates datacenter & residential bandwidth budgets and volume tier discounts.
"""
import argparse

def calculate_webshare_costs(bandwidth_gb, price_per_gb, annual_discount_percent):
    monthly_base = bandwidth_gb * price_per_gb
    annual_discount = monthly_base * (annual_discount_percent / 100.0)
    effective_monthly = monthly_base - annual_discount
    annual_total = effective_monthly * 12.0
    annual_savings = annual_discount * 12.0
    return {
        "monthly_base": monthly_base,
        "effective_monthly": effective_monthly,
        "annual_total": annual_total,
        "annual_savings": annual_savings
    }

def main():
    parser = argparse.ArgumentParser(description="Webshare Proxy Pricing & Savings Calculator")
    parser.add_argument("--gb", type=float, default=50.0, help="Monthly bandwidth in GB (default: 50)")
    parser.add_argument("--rate", type=float, default=4.50, help="Base rate per GB in USD (default: $4.50)")
    parser.add_argument("--annual-discount", type=float, default=30.0, help="Annual billing discount percentage (default: 30%%)")
    args = parser.parse_args()

    res = calculate_webshare_costs(args.gb, args.rate, args.annual_discount)
    print(f"Monthly Base Cost:       ${res['monthly_base']:.2f}")
    print(f"Effective Monthly (1y):  ${res['effective_monthly']:.2f}")
    print(f"Annual Total Prepaid:    ${res['annual_total']:.2f}")
    print(f"Annual Savings:          ${res['annual_savings']:.2f}")

if __name__ == "__main__":
    main()

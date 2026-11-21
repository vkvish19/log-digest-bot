# Log & Error Digest CLI (`log-digest-bot`)

A lightweight, zero-dependency Python utility that parses noisy server/application logs, normalizes dynamic IDs (such as `tx_id` or `order_id`), clusters recurring `ERROR` signatures by frequency, and generates a clean Markdown incident summary.

## Quick Start

1. Ensure Python 3.8+ is installed.
2. Run the digest generator against the included sample log:

```bash
python main.py
```

---
---

# Expected Output

## Daily Log & Error Digest
- **Total Lines Scanned:** 9
- **Total Errors Found:** 6
- **Unique Error Signatures:** 3

## Top Recurring Issues
1. **[3x]** `ERROR [PaymentGateway] TimeoutException: Upstream bank API did not respond within 5000ms (tx_id=*)`
2. **[2x]** `ERROR [OrderWorker] NullPointerException: Cannot invoke "Order.getItems()" because "order" is null (order_id=*)`
3. **[1x]** `ERROR [DBPool] SQLException: Connection pool exhausted (active=*, max=*)`
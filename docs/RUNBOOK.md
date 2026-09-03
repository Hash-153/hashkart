# NovaMart SRE Incident Response & Production Operations Runbook

This runbook outlines operational procedures, P0/P1 emergency response playbooks, database failover procedures, and telemetry monitoring guidelines for the NovaMart engineering team.

---

## 1. Incident Severity Definitions & Response SLAs

| Severity | Definition | Target Triage | Target Resolution | Escalation Contact |
| :--- | :--- | :--- | :--- | :--- |
| **P0 - Blocker** | Core checkout, payment gateway, or login completely down across the platform. | < 5 Minutes | < 30 Minutes | VP Eng, SRE On-Call, Lead Architect |
| **P1 - Critical** | Severe performance degradation (p99 latency > 2.5s), flash sale inventory lock starvation, or 3PL logistics dispatch blockage. | < 15 Minutes | < 2 Hours | Senior SRE On-Call, Engineering Lead |
| **P2 - Major** | Non-critical service failure (e.g. recommendation feed down, review submissions failing, export reports delayed). | < 1 Hour | < 8 Hours | Domain Tech Lead |
| **P3 - Minor** | UI visual glitches, minor copy errors, analytics delay. | < 4 Hours | Next Deployment | Domain Engineering Team |

---

## 2. Emergency Playbooks

### Playbook 1: PostgreSQL Aurora Primary High CPU (>90%) or Connection Exhaustion
1. **Identify Slow Queries via Pg_stat_activity**:
   ```sql
   SELECT pid, now() - query_start AS duration, query, state 
   FROM pg_stat_activity 
   WHERE state != 'idle' 
   ORDER BY duration DESC LIMIT 10;
   ```
2. **Terminate Blocking / Long-Running Queries**:
   ```sql
   SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid = <slow_pid>;
   ```
3. **Trigger Read-Replica Load Shedding**:
   Ensure all `SELECT` catalog and search traffic is strictly routed to the Aurora reader endpoint: `novamart-aurora-pg-cluster.cluster-ro-c7k2910.ap-south-1.rds.amazonaws.com`.
4. **Scale Connection Pool**: Increase `max_overflow` in backend configuration if connections are saturated.

---

### Playbook 2: Redis Cluster Cache Failure or Memory Eviction Spikes
1. **Inspect Redis Memory Usage & Hit Ratio**:
   ```bash
   redis-cli -h $REDIS_HOST -p 6379 info memory
   redis-cli -h $REDIS_HOST -p 6379 info stats
   ```
2. **Execute Cache Warm-Up Script**:
   If Redis cluster was restarted, warm up top 5,000 product details and active flash sales:
   ```bash
   python scripts/warm_cache.py --concurrency=10
   ```
3. **Emergency Rate Limiter Bypass**:
   If Redis is unreachable, token bucket middleware automatically falls back to in-memory local dict to avoid dropping customer traffic.

---

### Playbook 3: Flash Sale Stock Race Condition or Overselling Alert
1. **Audit Claimed vs Available Units**:
   ```sql
   SELECT item_id, allocated_stock_units, claimed_units 
   FROM flash_sale_items 
   WHERE claimed_units > allocated_stock_units;
   ```
2. **Force Freeze Flash Sale Item**:
   ```sql
   UPDATE flash_sale_items SET claimed_units = allocated_stock_units WHERE id = <item_id>;
   ```
3. **Notify Customers & Issue Courtesy SuperCoins**:
   Run compensation script to award 500 SuperCoins to impacted users.

---

## 3. Disaster Recovery & Database Restoration

To restore from an S3 Point-in-Time backup archive:
```bash
python scripts/db_backup_restore.py restore \
  --db-url "$DATABASE_URL" \
  --file "s3://novamart-db-backups/daily/novamart_prod_latest.dump"
```

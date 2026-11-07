# Engineering Debt Register

Rows are ordered by path, then by line number. Regenerate rather than edit by hand.

### 🧾 Open Engineering Debt

- [ ] `src/ledger_core/allocate.py:18` → drop the legacy allocation table after the migration window
- [ ] `src/ledger_core/audit.py:11` → sample only settled entries in the audit sweep
- [ ] `src/ledger_core/ingest.py:31` → validate the batch envelope before enqueueing entries
- [ ] `src/ledger_core/ingest.py:40` → attach producer sequence numbers to replays
- [ ] `src/ledger_core/reconcile.py:12` → normalize account keys before joining trial balances
- [ ] `src/ledger_core/reconcile.py:20` → normalize account keys before joining trial balances
- [ ] `src/ledger_core/report.py:13` → cache the fx rate snapshot per batch
- [ ] `src/ledger_core/report.py:18` → move report scheduling into the export service
- [ ] `src/ledger_core/settle.py:18` → collapse duplicated rounding guards into one helper
- [ ] `src/ledger_core/util.py:29` → replace ad-hoc retry loop with shared backoff helper
- [ ] `vendor/lib_v1/alpha.py:17` → partition journal writes by account range
- [ ] `vendor/lib_v1/beta.py:20` → route all currency conversion through the shared fx service
- [ ] `vendor/lib_v1/gamma.py:15` → reject positive fee adjustments during replay
- [ ] `vendor/lib_v2/alpha.py:26` → partition journal writes by account range
- [ ] `vendor/lib_v2/beta.py:26` → route all currency conversion through the shared fx service
- [ ] `vendor/lib_v2/gamma.py:24` → reject positive fee adjustments during replay
- [ ] `vendor/lib_v2/gamma.py:26` → throttle replayed fee adjustments per tenant

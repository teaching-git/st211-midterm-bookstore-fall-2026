# AI_USAGE.md -- Declaration and audit

Group: <name>   Members: <names>

## D3.1 Declaration (required)
| AI tool | How we used it |
|---|---|
| | |

## D3.2 Audit of the supplied ai_review/ test set (graded core)
Run EACH test in ai_review/ against the shipped app and record real evidence.

| Test | What it claims to catch | Does it actually? | Evidence (command + real output) | Verdict |
|---|---|---|---|---|
| test_cart_total_sums_items | | | | genuine / passes anyway / invented bug |
| test_login_rejects_wrong_password | | | | |
| test_search_finds_exact_title | | | | |
| test_import_returns_count | | | | |
| test_register_duplicate_returns_false | | | | |
| test_checkout_empty_returns_none | | | | |
| test_add_to_cart_returns_true_for_known_product | | | | |
| test_search_is_limited_to_ten_results | | | | |

## D3.3 Verdict (a few short paragraphs)
- Which failure mode was most common in the supplied set?
- Why is a test that passes against buggy code more dangerous than one that crashes?
- What will you check in future before trusting a generated test?

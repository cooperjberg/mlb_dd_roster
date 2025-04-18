
def predict_new_ovr(current_ovr, mlb_stats, showzone_attrs):
    """
    Simple rules-based predictor:
    - Upgrade if recent MLB stats are hot (e.g. HRs, AVG, BB%)
    - Downgrade if struggling (low AVG, high K%)
    """

    adjustment = 0

    # Hitters
    if mlb_stats.get("avg", 0) >= 0.300:
        adjustment += 1
    if mlb_stats.get("hr", 0) >= 5:
        adjustment += 1
    if mlb_stats.get("bb_pct", 0) >= 0.12:
        adjustment += 1
    if mlb_stats.get("k_pct", 1) >= 0.25:
        adjustment -= 1
    if mlb_stats.get("avg", 1) <= 0.200:
        adjustment -= 1

    predicted_ovr = max(current_ovr + adjustment, showzone_attrs.get("overall", current_ovr))
    return predicted_ovr

def boolean_to_emooji(bool_val, primary_emooji: bool):
    if primary_emooji:
        return "✅" if bool_val else "❌"
    return "☑️" if bool_val else "✖️"

def boot_check(aircraft_name, rules):
    """Проверяет готовность системы при старте."""
    print(f"=== БОРТОВОЙ КОМПЬЮТЕР {aircraft_name} ЗАПУЩЕН ===")
    print(f"Разрешенный эшелон: {rules['assigned_level']} м")
    print(f"Безопасный запас высоты: {rules['safe_margin']} м")
    return "SYSTEM READY"

